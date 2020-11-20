from cell_mvp import Cell
from ant_mvp import Ant
from map_mvp import *


def create_initial_data(map_size,nest_coordinates,food_coordinates,food_size=(1,1),ant_set=set(),number_of_ant=NBR_OF_ANT_CREATED,ant_limit=2000):
    '''
    Creates map with one nest cell and one food cell

    Parameters
    -------
    map_size
        Tuple (y,x) where first int is number of rows and second int is number of columns
    nest_coordinates
        Tuple (y,x), coordinates of the node to be changed to nest
    food_coordinates
        Tuple (y,x), the left top coordinates of the node to be changed to food
    food_size
        Tuple (y,x), the size of the food to be added, default to be (1,1)
    ant_set
        Set of ants before current round of simulation
    number_of_ant
        Integer of the number of ants to be created
    ant_limit
        Integer of maximum limit of ants on map

    Returns
    -------
    list
        map
            List of lists of cells
        nest_coordinates
            Tuple (y,x), coordinates on which ants should be created
        ant_set
            Unchanged as before
        number_of ant
            Unchanged as before
        ant_limit
            Unchanged as before

    '''
    new_map = add_food(food_coordinates,add_nest(nest_coordinates,create_empty_map(map_size)),food_size)
    return [new_map,nest_coordinates,ant_set,number_of_ant,ant_limit]


def generate(data):
    '''
    Simulates one round of ACO

    Parameters
    -------
    list
        map
            List of lists of cells on which the next round is to be simulated
        nest_coordinates
            Tuple (y,x), coordinates on which ants should be created
        ant_set
            Set of ants before current round of simulation
        number_of_ant
            Integer of the number of ants to be created
        ant_limit
            Integer, maximum number of ants that can be on the map at the same time
    
    Returns
    -------
    list
        new_map
            List of lists of cells as the generated map
        nest_coordinates
            Unchanged from before
        new_ant_set
            Set of ants after current round of simulation
        number_of_ant
            Unchanged from before
        ant_limit
            Unchanged from before
    '''
    new_ant_set = data[2] 
    for spawn in range(data[3]):
        if len(data[2]) < data[4]:
            new_ant_set = create_ant(
                data[0], data[1], new_ant_set, data[3])
    for ant in new_ant_set:
        ant.move_ant(data[0])
    new_map = update_map(data[0],new_ant_set)
    return [new_map,data[1],new_ant_set,data[3],data[4]]


def aco_simulate(data, generations):
    '''
    Stimulates several rounds of ACO

    Parameters
    -------
    list
        map
            List of lists of cells on which the next round is to be simulated
        nest_coordinates
            Tuple (y,x), coordinates on which ants should be created
        ant_set
            Set of ants before current round of simulation
        number_of_ant
            Integer of the number of ants to be created
        ant_limit
            Integer, maximum number of ants that can be on the map at the same time
    Generations
        Integer of the number of generations 
    
    Returns
    -------
    list
        new_map
            List of lists of cells as the generated map
        nest_coordinates
            Unchanged from before
        new_ant_set
            Set of ants after current round of simulation
        number_of_ant
            Unchanged from before
        ant_limit
            Unchanged from before
    '''
    for i in range(generations):
        data = generate(data)
    return data
