'''
Date: 2020-11-12 21:31:20
LastEditors: Lonel Vino
LastEditTime: 2020-11-12 22:10:48
'''
from tkinter import *
import numpy as np
from generate_universe import *
from simulation import *
import time

def interface_graph_game():
    '''
    1.(Controller part) Define parameters to generate a graphical game world
    2.(View part) Generate a graphical game world by widget Canvas
    '''

    def remove(row, col):
        '''
        Removal of the circle found in table 2

        Parameters
        --------
        row
            int of the x_position of cell to be deleted
        col
            int of the y_position of cell to be deleted
        '''
        table1[row][col].delete(table2[row][col])
        

    def create(row, col):
        '''
        Creation of a circle in table 2

        Parameters
        -------
        row
            int of the x_position of cell to be created
        col
            int of the y_position of cell to be created

        '''
        table1[row][col].delete(table2[row][col])
        table1[row][col].create_rectangle(width_rec*(1 - 1/1.1), height_rec*(1 - 1/1.1), width_rec/1.1, height_rec/1.1)
        table2[row][col] = table1[row][col].create_oval(width_rec*(1 - 1/1.5), height_rec*(1 - 1/1.5), width_rec/1.5, height_rec/1.5, outline='black', fill='red')
        

    def getParameters():
        '''
        (Controller part) Define parameters to generate a graphical game world
        
        Return
        -------
        Parameters to generate the graphical universe 
        '''
        
        window = Tk()

        # Define the universe size
        num_rows_univ = StringVar()
        Row = Label(window, text="Enter the number of rows of your universe")
        reponse1 = Entry(window, textvariable=num_rows_univ, width=10)
        Row.pack()
        reponse1.pack()
        num_cols_univ = StringVar()
        Col = Label(
            window, text="Enter the number of cols of your universe")
        reponse2 = Entry(window, textvariable=num_cols_univ, width=10)
        Col.pack()
        reponse2.pack()

        # Define the seed to be planted
        seed = StringVar()
        demande_seed = Label(
            window, text="Give the name of the seed you want to plant")
        reponse3 = Entry(window, textvariable=seed, width=10)
        demande_seed.pack()
        reponse3.pack()

        # Define the seed position in the universe
        x_start = StringVar()
        X_start = Label(
            window, text="Enter the row in the box at the top left of your seed")
        reponse4 = Entry(window, textvariable=x_start, width=10)
        X_start.pack()
        reponse4.pack()
        y_start = StringVar()
        Y_start = Label(
            window, text="Enter the column in the box at the top left of your seed")
        reponse5 = Entry(window, textvariable=y_start, width=10)
        Y_start.pack()
        reponse5.pack()

        # Define the interations of game_of_life
        interations = StringVar()
        n_generations = Label(window, text="Enter the desired number of steps")
        reponse6 = Entry(window, textvariable=interations, width=10)
        n_generations.pack()
        reponse6.pack()

        # Define the interval of 2 updates
        interval = IntVar()
        Interval = Label(
            window, text="Enter the interval interval between two displays")
        reponse7 = Entry(window, textvariable=interval, width=10)
        Interval.pack()
        reponse7.pack()

        bouton_quit = Button(window, text="Valide", command=window.destroy)
        bouton_quit.pack()

        window.mainloop()

        # Combine all parameters into a list
        parameters = [int(num_rows_univ.get()), int(num_cols_univ.get()), seed.get(), int(x_start.get()), int(y_start.get()), int(interations.get()), interval.get()]
        return parameters

    '''
    (View part) Generate a graphical game world by widget Canvas
    Use 2 tables to express the graphical View, table1 used to generate rectangle Window (Universe), table2 used to generate circle Window (Living cells)
    '''

    # Initialize the universe
    params = getParameters()
    universe = generate_universe(size=(params[0], params[1]))
    seed = create_seed(type_seed=params[2])
    universe = add_seed_to_universe(seed, universe, params[3], params[4])

    new_universe = universe

    root = Tk()

    num_rows_univ, num_cols_univ = np.shape(universe)
    width_rec, height_rec = 600 / num_rows_univ, 600 / num_cols_univ

    table1 = list(range(num_rows_univ))
    table2 = list(range(num_rows_univ))

    for row in range(num_rows_univ):
        table1[row] = list(range(num_cols_univ))
        table2[row] = list(range(num_cols_univ))

        for col in range(num_cols_univ):
            table1[row][col] = Canvas(root, height=height_rec, width=width_rec)
            # Creation of a canvas put in an array with row, col indices

            table1[row][col].grid(row=row, column=col)
            # Creation of the row box, col of the grid in which we put the previous canvas

            if universe[row][col] != 0:
                table2[row][col] = table1[row][col].create_oval(width_rec*(1 - 1/1.5), height_rec*(1 - 1/1.5), width_rec/1.5, height_rec/1.5, outline='black', fill='red')
                # Creation of a circle in the previous canvas put in the table with the indices row, col

                table1[row][col].create_rectangle(width_rec*(1 - 1/1.1), height_rec*(1 - 1/1.1), width_rec/1.1, height_rec/1.1)
                # Draw a rectangle
            else:
                table1[row][col].create_rectangle(width_rec*(1 - 1/1.1), height_rec*(1 - 1/1.1), width_rec/1.1, height_rec/1.1)
                # Draw a rectangle

    root.update()
    times = params[6] / 1000
    for i in range(params[5]):
        univers, new_universe = new_universe,generation(new_universe)
        for row in range(num_rows_univ):
            for col in range(num_cols_univ):
                if univers[row][col] != new_universe[row][col]:
                    # We look at the points that will be modified between two stages
                    if new_universe[row][col] == 1:
                        # If in the box we have a 1, then we must draw a circle
                        time.sleep(times)
                        create(row, col)
                        # We use the time.sleep () function in order to be able to see the modifications between each step
                        # We use create to draw a circle
                    else:
                        # If we have a 0 in our box, we want to remove the circle that was present in the previous state
                        time.sleep(times)
                        remove(row, col)
                        # Similarly, the remove function allows you to remove a circle in the boxes concerned
        root.update()
        # We update to see the changes on our interface
    root.mainloop()

interface_graph_game()



