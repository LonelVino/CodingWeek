from cell_mvp import Cell
from ant_mvp import Ant


NBR_OF_ANT_CREATED = 5


def create_empty_map(size):
    '''
    Creates a new empty map

    Parameters
    -------
    size
        Tuple (y,x) where first int is number of rows and second int is number of columns
    '''
    new_map = []
    for i in range(size[0]):
        map_row = []
        for j in range(size[1]):
            map_row.append(Cell(i,j,set(),Cell.OTHER))
        new_map.append(map_row)
    return new_map


def add_nest(coordinates,map):
    '''
    Adds nest to the map

    Parameters
    -------
    coordinate
        Tuple (y,x), coordinates of the node to be changed to nest
    map
        List of lists of cells, on which nest is to be added

    Returns
    -------
    new_map
        Map updated with nest
    '''
    new_map = map[:]
    y, x = coordinates[0], coordinates[1]
    try:
        new_map[y][x].type = Cell.NEST
    except:
        raise ValueError('Indice outside of the map')
    return new_map


def add_food(coordinates,map,size=(1,1),food_amount=10):
    '''
    Adds food to the map

    Parameters
    -------
    coordinate
        Tuple (y,x), the left top coordinates of the node to be changed to food
    map
        List of lists of cells, on which food is to be added
    size
        Tuple (y,x), the size of the food to be added, default to be (1,1)
    food_amound
        Integer, the amount of food in food cell created
    
    Returns
    -------
    new_map
        Map updated with food
    '''
    new_map = map[:]
    size_y, size_x, y, x = size[0], size[1], coordinates[0], coordinates[1]
    map_rows, map_cs = len(new_map), len(new_map[0])
    try:
        if y + size_y <= map_rows and x + size_x <= map_cs:
            for i in range(size_y):
                for j in range(size_x):
                    new_map[y + i][x + j].type = Cell.FOOD
                    new_map[y + i][x + j].food_amount = food_amount
        else:
            raise ValueError('Indice outside of the map')
    except:
        raise ValueError('Indice outside of the map')
    return new_map


def add_obstacle(coordinates,map,size=(1,1)):
    '''
    Adds obstacle to the map

    Parameters
    -------
    coordinate
        Tuple (y,x), the left top coordinate of the node to be changed to obstacle
    map
        List of lists of cells, on which obstacle is to be added
    size
        Tuple (y,x), the size of the obstacle to be added, default to be (1,1)

    Returns
    -------
    new_map
        Map updated with obstacle
    '''
    new_map = map[:]
    size_y, size_x, y, x = size[0], size[1], coordinates[0], coordinates[1]
    map_rows, map_cs = len(new_map), len(new_map[0])
    try:
        if y + size_y <= map_rows and x + size_x <= map_cs :
            for i in range(size_y):
                for j in range(size_x):
                    new_map[y + i][x + j].type = Cell.OBSTACLE
        else:
            raise ValueError('Indice outside of the map')
    except:
        raise ValueError('Indice outside of the map')
    return new_map


def update_map(map,all_ants):
    '''
    Updates the map with the set of ants on it

    Parameters
    -------
    map
        List of lists of cells as map to be updated
    all_ants
        Set of instances of all ants on map
    
    Returns
    -------
    new_map
        Map updated with next generation of ant positions
    '''
    new_map = map[:]

    # Get the size of the map
    len_y = len(new_map)
    len_x = len(new_map[0])
    
    # Delete all old ants
    for y in range(len_y):
        for x in range(len_x):
            new_map[y][x].delete_all_ant()
    
    # Add ants to their respective cells
    for ant in all_ants:
        ant.cell.add_ant(ant)
    
    # Calculate the new number of pheromone
    for y in range(len_y):
        for x in range(len_x):
            new_map[y][x].update_pheromone()
    
    return new_map


def create_ant(map,nest_coordinates,old_all_ants,number_of_ant=NBR_OF_ANT_CREATED):
    '''
    Create the ant at the given coordinate

    Parameter
    -------
    map
        List of lists of cells as map on which ant is created
    nest_coordinate
        Tuple (y,x), coordinates on which the ant should be created
    old_all_ants
        Set of all the already created ants
    number_of_ant
        Integer, the number of ants to be created, default to be NBR_OF_ANT_CREATED

    Returns
    -------
    new_all_ants
        Set of all ants including created ants
    '''
    y, x  = nest_coordinates[0], nest_coordinates[1]

    try:
        cell = map[y][x] # The cell on which ants are to be created
        new_all_ants = old_all_ants
        if cell.type == Cell.NEST:
            for i in range(number_of_ant):
                ant = Ant(cell)
                cell.add_ant(ant)
                new_all_ants = new_all_ants.union({ant})
    except:
        raise ValueError('Indice outside of the map')

    return new_all_ants