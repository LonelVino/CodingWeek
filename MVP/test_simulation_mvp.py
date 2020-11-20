from simulation_mvp import *


def run_generate(data,generations,print_interval):
    '''
    Runs generate for a given number of rounds

    Parameters
    -------
    starting list
        map
            List of lists of cells on which the next round is to be simulated
        nest_coordinates
            Tuple (y,x), coordinates on which ants should be created
        ant_set
            Set of ants before current round of simulation
        
    generations
        Integer of the number of generations
    
    '''
    print("\nSTARTING MAP")
    for row in data[0]:
        print([(row[col].type,len(row[col].ants),round(row[col].pheromone)) for col in range(len(row))])
    for r in range(generations):
        data = generate(data)
        if (r + 1) % print_interval == 0:
            print("\nNEXT MAP ROUND " + str(r + 1))
            for row in data[0]:
                print([(row[col].type,len(row[col].ants),round(row[col].pheromone)) for col in range(len(row))])


def run_single_ant(data,generations):
    '''
    Runs generate for a given number of rounds

    Parameters
    -------
    starting list
        map
            List of lists of cells on which the next round is to be simulated
        nest_coordinates
            Tuple (y,x), coordinates on which ants should be created
        ant_set
            Set of ants before current round of simulation
        
    generations
        Integer of the number of generations
    
    '''
    food_round = []
    return_round = []
    print("\nSTARTING MAP")
    for row in data[0]:
        #print([(row[col].type,len(row[col].ants),row[col].pheromone) for col in range(len(row))])
        print([(row[col].type,len(row[col].ants)) for col in range(len(row))])
    for r in range(generations):
        print("\nNEXT MAP ROUND " + str(r + 1))
        data = generate(data)
        for ant in data[2]:
            if ant.cell.type == 'F':
                food_round.append(r + 1)
                print("Ant has landed on food cell!")
            if ant.cell.type == 'N':
                return_round.append(r + 1)
                print("Ant has returned to nest cell!")
        for row in data[0]:
            #print([(row[col].type,len(row[col].ants),row[col].pheromone) for col in range(len(row))])
            print([(row[col].type,len(row[col].ants)) for col in range(len(row))])
    print('\nFood round:', food_round)
    print('Return round:', return_round)


if __name__ == '__main__':
    
    # Track movement of single ant without ant creation generated over n generations on map with obstacles
    track1 = False
    number_generations = 100
    if track1:
        simulation_data = create_initial_data([7,7],[0,0],[6,6])
        simulation_data[2] = create_ant(simulation_data[0],simulation_data[1],simulation_data[2],1)
        simulation_data[3] = 0
        simulation_data[0] = add_obstacle([0,1],simulation_data[0],size=(6,1))
        simulation_data[0] = add_obstacle([1,5],simulation_data[0],size=(6,1))
        run_single_ant(simulation_data,number_generations)
    
    # Track movement of all ants generated over n generations on map without obstacles
    track2 = True
    number_generations = 50
    print_interval = 10
    if track2:
        simulation_data = create_initial_data([7,7],[0,0],[6,6])
        run_generate(simulation_data,number_generations,print_interval)
    
    # Track movement of all ants generated over n generations on map with 2 rectangular obstacles
    track3 = False
    number_generations = 30
    print_interval = 1
    if track3:
        simulation_data = create_initial_data([7,7],[0,0],[6,6])
        simulation_data[0] = add_obstacle([0,1],simulation_data[0],size=(6,1))
        simulation_data[0] = add_obstacle([1,5],simulation_data[0],size=(6,1))
        '''
        Map looks like this:
        N | . . . . .
        . | . . . | .
        . | . . . | .
        . | . . . | .
        . | . . . | .
        . | . . . | .
        . . . . . | F

        Optimal path by ants would theroetically be:
        N | . . . @ .
        @ | . . @ | @
        @ | . @ . | @
        @ | . @ . | @
        @ | . @ . | @
        @ | @ . . | @
        . @ . . . | F
        '''
        run_generate(simulation_data,number_generations,print_interval)