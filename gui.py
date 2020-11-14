
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial

from animation import animate
from animation import universe_dict
from generate_universe import *
from simulation import game_life_simulate
from dict_seed import dict_seed

import matplotlib.pyplot as plt
import numpy as np
import time

CANVAS_HEIGHT = 700
CANVAS_WIDTH = 700
NoStop=True

def gui():
    #Get the root of gui

    tk=Tk()
    gameoflife=Toplevel(tk)
    gameoflife.title('Game of life Conway')
    #animation parties
    simulation = Canvas(gameoflife,height=CANVAS_HEIGHT,width=CANVAS_WIDTH)
    #animate(universe_size,seed,seed_position,cmap='Greys',n_generations=30,interval=300,save=False,writer='ffmpeg')
    

    #Pack each frame
    simulation.pack()
    gameoflife.mainloop()

def adapt_universe(tk,canvas,universe,color_line='gray',color_background='white',draw_grill=False):

    stop(canvas)

    num_rows_univ,num_cols_univ = universe.shape
    WIDTH_OF_CELL = np.floor(min((CANVAS_HEIGHT)/num_rows_univ,(CANVAS_WIDTH)/num_cols_univ))
    grid_reel_width = num_cols_univ * WIDTH_OF_CELL
    grid_reel_height = num_rows_univ * WIDTH_OF_CELL

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
    return (dict_lines,dict_rec,WIDTH_OF_CELL)
    
def display_universe(tk,canvas,universe,graphical_grid,color_background='white',color_foreground='black'):
    num_rows_univ,num_cols_univ = universe.shape
    dict_lines=graphical_grid[0]
    dict_rec=graphical_grid[1]
    WIDTH_OF_CELL = graphical_grid[2]

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
                
def display_animation(tk,canvas,universe,n_generations=None,interval=10,color_line='gray',color_background='white',color_foreground='black',draw_grill=True):
    global NoStop
    graphical_grid=adapt_universe(tk,canvas,universe,color_line=color_line,color_background=color_background,draw_grill=draw_grill)
    NoStop=True
    if n_generations is None:
        k=0
        while NoStop:
            graphical_grid=display_universe(tk,canvas,game_life_simulate(universe,k,universe_dict),graphical_grid,color_background=color_background,color_foreground=color_foreground)
            time.sleep(interval/1000)
            k += 1
    elif isinstance(n_generations,int):
        for k in range(0,n_generations):
            graphical_grid=display_universe(tk,canvas,game_life_simulate(universe,k,universe_dict),graphical_grid,color_background=color_background,color_foreground=color_foreground)
            time.sleep(interval/1000)

def begin(tk,canvas,universe_x_val,universe_y_val,position_x_val,position_y_val,seed):
    global NoStop
    NoStop=True
    try:
        val_universe_x=int(universe_x_val.get())
        val_universe_y=int(universe_y_val.get())
        val_position_x=int(position_x_val.get())
        val_position_y=int(position_y_val.get())
    except:
        messagebox.showwarning('Warning','Only number accept')
    seed = create_seed(type_seed = seed.get())
    universe = generate_universe(size=(val_universe_x,val_universe_x))
    universe = add_seed_to_universe(seed, universe,x_start=val_position_x, y_start=val_position_x)
    display_animation(tk,canvas,universe)

def stop(canvas):
    global NoStop
    NoStop=False
    canvas.delete('all')

def welcome(tk,canvas):
    seed = create_seed(type_seed = "gun")
    universe = generate_universe(size=(75,75))
    universe = add_seed_to_universe(seed, universe,x_start=10, y_start=0)
    display_animation(tk,canvas,universe)

def destroy(tk):
    tk.destroy()

def gui(color_background='white'):
    gameoflife = Tk()
    gameoflife.title('Game of life Conway')

    #1.Animation Frames
    simulation = Canvas(gameoflife)

    #2.Control Frames
    control=Frame(gameoflife,bg=color_background)

    #2.1 Universe Label
    universe_label=Label(control,text='Universe Size(x,y)',bg=color_background)

    #2.2 Universe entry
    universe_frame=Frame(control)
    universe_x_val=StringVar(universe_frame)
    universe_y_val=StringVar(universe_frame)
    universe_x=Entry(universe_frame,textvariable=universe_x_val)
    universe_y=Entry(universe_frame,textvariable=universe_y_val)
    universe_x.grid(row=0,column=0)
    universe_y.grid(row=0,column=1)

    #2.3 Position label
    position_label=Label(control,text='Position of seed(x,y)',bg=color_background)

    #2.4 Position entry
    position_frame=Frame(control)
    position_x_val=StringVar(position_frame)
    position_y_val=StringVar(position_frame)
    position_x=Entry(position_frame,textvariable=position_x_val)
    position_y=Entry(position_frame,textvariable=position_y_val)
    position_x.grid(row=0,column=0)
    position_y.grid(row=0,column=1)

    #2.5 Seed label
    seed_label=Label(control,text='Seed',bg=color_background)

    #2.6 Seed cblist
    seed=StringVar(control)
    seed_cblist=ttk.Combobox(control,textvariable=seed) 
    seed_cblist["values"]=list(dict_seed.keys())
    seed_cblist.current(2)

    #2.7 Begin button
    begin_button = Button(control,text='Begin',command=partial(begin,gameoflife,simulation,universe_x_val,universe_y_val,position_x_val,position_y_val,seed))
    
    #2.8 Stop button
    stop_button = Button(control,text='Stop',command=partial(stop,simulation))
    quit_button = Button(control,text='Quit',command=partial(destroy,gameoflife))

    universe_label.grid(row=0,column=0)
    universe_frame.grid(row=1,column=0)
    position_label.grid(row=2,column=0)
    position_frame.grid(row=3,column=0)
    seed_label.grid(row=4,column=0)
    seed_cblist.grid(row=5,column=0)
    begin_button.grid(row=6,column=0)
    stop_button.grid(row=7,column=0)
    quit_button.grid(row=8,column=0)

    simulation.grid(row=0,column=0,sticky='EWNS')
    control.grid(row=0,column=1,sticky='EWNS')

    #welcome(gameoflife,simulation)
    gameoflife.grid_columnconfigure(0, weight=1)
    gameoflife.grid_rowconfigure(0, weight=1)
    gameoflife.mainloop()



if __name__ == '__main__':
    gui()
