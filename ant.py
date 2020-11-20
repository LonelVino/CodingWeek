from random import choices
from cell import *


class Ant(object):
    '''
    The class of Ant

    Attributes
    -------
    cell
        Cell instance on which ant is positioned on the map
    history
        List of cells already travelled, with the last entry being the latest
    carry_food
        Boolean of whether the ant is carrying food
    pheromone_deposit_amount
        Integer of the amount of pheromone deposited by ant on cell
    '''

    def __init__(self,starting_cell):
        '''
        Creates ant at nest position; Does not return anything

        Parameters
        -------
        starting_cell
            Cell instance of nest on map
        
        '''
        self.cell = starting_cell
        self.history = [starting_cell]
        self.carry_food = False
        self.pheromone_deposit_amount = 0
    
    def __str__(self):
        '''
        Prints ( Coordinates of ant , Ant's current action ) when print(ant_instance) is used
        '''
        if self.carry_food:
            if self.cell.type == Cell.FOOD:
                action = 'Picking up food from source'
            else:
                action = 'Returning to nest for food deposition'
        else:
            if self.cell.type == Cell.NEST:
                action = 'Preparing to leave nest'
            else:
                action = 'Finding food source'
        return '((' + str(self.cell.position_y) + ',' + str(self.cell.position_x) + '), ' + action + ')'

    def probabilistic_selection(self,Map):
        '''
        Generate the next move based on pheromone levels
        
        Parameters
        -------
        map
            Lists of lists of cells generated

        Returns
        --------
        next cell
            Cell([neighbour_y,neighbour_x]) as next cell to be moved to
        '''
        map = Map.map()
        num_rows, num_cols = len(map), len(map[0])
        possible_movements = []
        weights_list = []
        last_resort = None
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0:
                    continue # Do not include selected cell itself
                neighbour_y = self.cell.position_y + i
                neighbour_x = self.cell.position_x + j
                if neighbour_y < 0 or neighbour_y >= num_rows or neighbour_x < 0 or neighbour_x >= num_cols:
                    continue    # Neighbour cells outside the map are not considered
                if map[neighbour_y][neighbour_x].type == Cell.FOOD:
                    return map[neighbour_y][neighbour_x] # Food cell is automatically chosen
                if map[neighbour_y][neighbour_x].type in [Cell.OBSTACLE,Cell.NEST]:
                    if map[neighbour_y][neighbour_x].type == Cell.NEST:
                        last_resort_nest = map[neighbour_y][neighbour_x]
                    continue # Obstacle and nest cells are skipped
                try:
                    if map[neighbour_y][neighbour_x] == self.history[-4:-1]:
                        last_resort = map[neighbour_y][neighbour_x]
                        continue # Ant will not go back to any 3 cells it traveled before
                except:
                    try:
                        if map[neighbour_y][neighbour_x] == self.history[-3:-1]:
                            last_resort = map[neighbour_y][neighbour_x]
                            continue # Ant will not go back to any 2 cells it traveled before
                    except:
                        try:
                            if map[neighbour_y][neighbour_x] == self.history[-3:-1]:
                                last_resort = map[neighbour_y][neighbour_x]
                                continue # Ant will not go back to any 2 cells it traveled before
                        except:
                            if map[neighbour_y][neighbour_x] == self.history[-2]:
                                last_resort = map[neighbour_y][neighbour_x]
                                continue # Ant will not go back to the cell it traveled just before
                possible_movements.append(map[neighbour_y][neighbour_x])
                weights_list.append(map[neighbour_y][neighbour_x].pheromone)
        if possible_movements == []: # Implemented so that ants have a way out when they reach a dead end
            if last_resort != None:
                possible_movements.append(last_resort)
                weights_list.append(last_resort.pheromone)
            else:
                possible_movements.append(last_resort_nest)
                weights_list.append(last_resort_nest.pheromone)
        return choices(possible_movements, weights=tuple(weights_list), k=1)[0]

    def move_ant(self,map):
        '''
        Moves ant to new self depending on carry food status or probabilistic selection;
        Does not return anything
        '''
        if self.carry_food:
            if self.cell.type == Cell.FOOD:
                self.remove_from_history() # Last entry in self.history has to be removed first since it is the food cell itself
            self.cell = self.remove_from_history() # When an ant is carrying food, it goes back the same way it came from
            self.pheromone_deposit_amount = min(10,len(self.history)) # Ants will deposit at least 10 pheromones on cell, otherwise it is proportional to the path travelled
            if self.cell.type == Cell.NEST:
                self.toggle_carry_food() # Ants will drop their food upon reaching the nest
                self.history = [self.cell]
        else:
            self.cell = self.probabilistic_selection(map) # When an ant is searching for food, it chooses its next move based on pheromone level
            self.add_to_history()
            if self.cell.type == Cell.FOOD:
                self.toggle_carry_food() # Ants pick up food from food cell

    def add_to_history(self):
        '''
        Adds ant's own cell into history list; Does not return anything
        '''
        self.history.append(self.cell)

    def remove_from_history(self):
        '''
        Removes last cell in history list and returns it
        '''
        return self.history.pop()

    def toggle_carry_food(self):
        '''
        Changes carry food status to opposite
        '''
        if self.cell.type == Cell.NEST:
            self.carry_food = False
        elif self.cell.type == Cell.FOOD:
            self.carry_food = True
        else:
            pass