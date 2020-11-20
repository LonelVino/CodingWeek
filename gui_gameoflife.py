from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial

from animation import animate
from animation import universe_dict
from generate_universe import *
from simulation import reset_universe_dict
from simulation import game_life_simulate
from dict_seed import dict_seed


import matplotlib.pyplot as plt
import numpy as np
import time

CANVAS_HEIGHT = 700
CANVAS_WIDTH = 700
NoStop=True # boolean used to decide whether stop the animation
universe_dict={}


def adapt_universe(tk,canvas,universe,color_line='gray',color_background='white',draw_grill=False):
    '''
    To create a graphical grid which satisfies the size of universe
    '''
    stop(canvas)

    # Calculat the size
    num_rows_univ,num_cols_univ = universe.shape
    WIDTH_OF_CELL = np.floor(min((CANVAS_HEIGHT)/num_rows_univ,(CANVAS_WIDTH)/num_cols_univ))
    grid_reel_width = num_cols_univ * WIDTH_OF_CELL
    grid_reel_height = num_rows_univ * WIDTH_OF_CELL

    # Draw the grill
    dict_lines={}
    dict_rec={}
    if draw_grill:
        for i in range(0,num_rows_univ + 1):
            line=canvas.create_line(i*WIDTH_OF_CELL ,0 ,i*WIDTH_OF_CELL,grid_reel_height,fill=color_line,width=1)
            line_name="line_verticle_"+str(i)
            dict_lines[line_name]=line
        for i in range(0,num_cols_univ + 1):
            canvas.create_line(0,i*WIDTH_OF_CELL ,grid_reel_width ,i*WIDTH_OF_CELL ,fill=color_line,width=1)
            line_name="line_horizental_"+str(i)
            dict_lines[line_name]=line

    canvas.grid(row=0,column=0)
    tk.update()

    #returns the para and the dictionary for the graphical grid
    return (dict_lines,dict_rec,WIDTH_OF_CELL)
    
def display_universe_canvas(tk,canvas,universe,graphical_grid,color_background='white',color_foreground='black'):
    '''
    To display the universe in canvas
    '''
    #Basic parameters
    num_rows_univ,num_cols_univ = universe.shape
    dict_lines=graphical_grid[0]
    dict_rec=graphical_grid[1]
    WIDTH_OF_CELL = graphical_grid[2]

    #Draw the live cell
    for k in dict_rec.values():
        canvas.delete(k)
    for i in range(0,num_rows_univ):
        for j in range(0,num_cols_univ):
            if universe[i,j] == 1:
                rectangle=canvas.create_rectangle(i*WIDTH_OF_CELL ,j*WIDTH_OF_CELL ,(i+1)*WIDTH_OF_CELL ,(j+1)*WIDTH_OF_CELL ,fill=color_foreground)
                rectangle_name='rec_'+str(i)+'_'+str(j)
                dict_rec[rectangle_name]=rectangle
    tk.update()
    return (dict_lines,dict_rec,WIDTH_OF_CELL)
                
def display_animation(tk,canvas,universe,n_generations=None,interval=25,color_line='gray',color_background='white',color_foreground='black',draw_grill=True):
    '''
    To display the animation from the universe provided
    '''
    global NoStop
    graphical_grid=adapt_universe(tk,canvas,universe,color_line=color_line,color_background=color_background,draw_grill=draw_grill)
    NoStop=True
    if n_generations is None or n_generations == 0:
        k=0
        while NoStop:
            a=game_life_simulate(universe,k,universe_dict)
            graphical_grid=display_universe_canvas(tk,canvas,a,graphical_grid,color_background=color_background,color_foreground=color_foreground)
            time.sleep(interval/1000)
            k += 1
    elif isinstance(n_generations,int):
        for k in range(0,n_generations):
            graphical_grid=display_universe_canvas(tk,canvas,game_life_simulate(universe,k,universe_dict),graphical_grid,color_background=color_background,color_foreground=color_foreground)
            time.sleep(interval/1000)

def begin(tk,canvas,universe_x_val,universe_y_val,position_x_val,position_y_val,seed_val,n_generation_val,interval_val):
    '''
    Function of the start buttom
    '''
    global NoStop
    NoStop=True

    #get value
    try:
        val_universe_x=universe_x_val.get()
        val_universe_y=universe_y_val.get()
        val_position_x=position_x_val.get()
        val_position_y=position_y_val.get()
        try:
            val_n_generation=n_generation_val.get()
        except:
            val_n_generation=None
        val_interval=interval_val.get()
    except:
        messagebox.showwarning('Warning','Only number accept or size')

    # Put seed in the universe
    seed = create_seed(type_seed = seed_val.get())
    universe = generate_universe(size=(val_universe_x,val_universe_y))
    try:
        universe = add_seed_to_universe(seed, universe,x_start=val_position_x, y_start=val_position_y)
    except:
        messagebox.showwarning('Warning','Size smaller than the seed')
    display_animation(tk,canvas,universe,n_generations=val_n_generation,interval=val_interval)
    
def stop(canvas):
    '''
    Function of the stop buttom
    '''
    global NoStop
    NoStop=False
    reset_universe_dict(universe_dict)
    canvas.delete('all')

def welcome(tk,canvas):
    '''
    Function of the welcome(with nothing entered)
    '''
    seed = create_seed(type_seed = "gun")
    universe = generate_universe(size=(75,75))
    universe = add_seed_to_universe(seed, universe,x_start=10, y_start=0)
    display_animation(tk,canvas,universe)

def destroy(tk,canvas):
    '''
    Function of the quit buttom
    '''
    stop(canvas)
    tk.destroy()

def change_generation(generation_entry,generation_check_val):
    '''
    Function of the checkbottom of generation
    '''
    generation_entry.delete(0, 'end')
    if generation_check_val.get() == 0:
        generation_entry.configure(state=NORMAL)
    else:
        generation_entry.configure(state=DISABLED)
        
def gui(color_background='white'):
    '''
    gui main function
    '''
    gameoflife = Tk()
    gameoflife.title('Game of life Conway')
    

    #1.Animation Frames
    simulation = Canvas(gameoflife)
    gameoflife.protocol('WM_DELETE_WINDOW', partial(destroy,gameoflife,simulation))

    #2.Control Frames
    control=Frame(gameoflife,bg=color_background)

    #2.1 Universe Label
    universe_label=Label(control,text='Universe Size(x,y)',bg=color_background)

    #2.2 Universe entry
    universe_frame=Frame(control)
    universe_x_val=IntVar(universe_frame)
    universe_y_val=IntVar(universe_frame)
    universe_x=Entry(universe_frame,textvariable=universe_x_val)
    universe_y=Entry(universe_frame,textvariable=universe_y_val)
    universe_x.grid(row=0,column=0)
    universe_y.grid(row=0,column=1)

    #2.3 Position label
    position_label=Label(control,text='Position of seed(x,y)',bg=color_background)

    #2.4 Position entry
    position_frame=Frame(control)
    position_x_val=IntVar(position_frame)
    position_y_val=IntVar(position_frame)
    position_x=Entry(position_frame,textvariable=position_x_val)
    position_y=Entry(position_frame,textvariable=position_y_val)
    position_x.grid(row=0,column=0)
    position_y.grid(row=0,column=1)

    #2.5 Seed label
    seed_label=Label(control,text='Seed',bg=color_background)

    #2.6 Seed cblist
    seed_val=StringVar(control)
    seed_cblist=ttk.Combobox(control,textvariable=seed_val) 
    seed_cblist["values"]=list(dict_seed.keys())
    seed_cblist.current(0)
    
    #2.7 generation label
    generation_label=Label(control,text='Number of generations',bg=color_background)

    #2.8 Number of generations
    generation_frame=Frame(control)
    n_generation_val=IntVar(generation_frame)
    generation_entry=Entry(generation_frame,textvariable=n_generation_val,state=DISABLED,bg=color_background)
    generation_check_val=IntVar(generation_frame,value=1)
    generation_check=Checkbutton(generation_frame, text="INFINITE", variable=generation_check_val,command=partial(change_generation,generation_entry,generation_check_val),bg=color_background)
    generation_check.grid(row=0,column=0)
    generation_entry.grid(row=0,column=1)

    #2.9 Interval label
    interval_label=Label(control,text='Interval',bg=color_background)

    #2.10 Interval entry
    interval_val=IntVar(control,value=25)
    interval_entry=Entry(control,textvariable=interval_val,bg=color_background)

    #2.11 Begin button,Stop button,Quit button
    begin_button = Button(control,text='Begin',command=partial(begin,gameoflife,simulation,universe_x_val,universe_y_val,position_x_val,position_y_val,seed_val,n_generation_val,interval_val))
    stop_button = Button(control,text='Stop',command=partial(stop,simulation))
    quit_button = Button(control,text='Quit',command=partial(destroy,gameoflife,simulation))

    universe_label.grid(row=0,column=0)
    universe_frame.grid(row=1,column=0)
    position_label.grid(row=2,column=0)
    position_frame.grid(row=3,column=0)
    seed_label.grid(row=4,column=0)
    seed_cblist.grid(row=5,column=0)
    generation_label.grid(row=6,column=0)
    generation_frame.grid(row=7,column=0)
    interval_label.grid(row=8,column=0)
    interval_entry.grid(row=9,column=0)
    begin_button.grid(row=10,column=0)
    stop_button.grid(row=11,column=0)
    quit_button.grid(row=12,column=0)

    simulation.grid(row=0,column=0,sticky='EWNS')
    control.grid(row=0,column=1,sticky='EWNS')

    gameoflife.grid_columnconfigure(0, weight=1)
    gameoflife.grid_rowconfigure(0, weight=1)
    welcome(gameoflife,simulation)
    gameoflife.mainloop()



if __name__ == '__main__':
    gui()