class Cell(object):
    '''
    The class of Cell

    Attributes
    -------
    position_x
        Integer, the position of x of this cell (or column of cell)
    position_y
        Integer, the position of y of this cell (or row of cell)
    ants
        Set, all of the Ants on this cell 
    type
        String, the type of cell, with FOOD/NEST/OBSTACLE/OTHER(AUTRE) mapping to 'F'/'N'/'O'/'A' respectively
    pheromone
        Float, the total level of pheromone
    '''
    # Constants
    RATIO_EVAPORATION = 0.1  # The ratio of evaporation
    INITIAL_PHEROMONE = 1  # The minimum pheromone level for each cell

    # Marker of type
    FOOD = 'F'
    NEST = 'N'
    OBSTACLE = 'O'
    OTHER = 'A'

    MAX_PHEROMONE = 50 # Max pheromone is set so that there will not be to much phenomone to evaporate once food source is depleted

    def __init__(self, position_y, position_x, ants=set(), type_of_cell='A'):
        '''
        Creates cell at given position; Does not return anything 

        Parameters
        -------
        position_x, position_y
            Integer of the position of this cell
        ants 
            Set of all of the Ants on this cell, defaults to be empty set
        type_of_cell
            String of the type of the cell, with FOOD/NEST/OBSTACLE/OTHER mapping to 'F'/'N'/'O'/'A', defaults to be 'A'
        '''
        self.position_x = position_x
        self.position_y = position_y
        self.ants = ants
        self.type = type_of_cell
        self.pheromone = self.INITIAL_PHEROMONE
        self.food_amount = 0

    def __str__(self):
        '''
        Prints ( Coordinates of cell , Cell type, Cell's pheromone level ) when print(ant_instance) is used
        '''
        return '((' + str(self.position_y) + ',' + str(self.position_x) + '),' + str(self.type) + ',' + str(self.pheromone) + ')'

    def def_type(self, type_to_define):
        '''
        Defines/Changes the type of the cell; Does not return anything

        Parameters
        -------
        type_to_define
            String of the type of the cell, with FOOD/NEST/OBSTACLE/OTHER mapping to 'F'/'N'/'O'/'A'
        '''
        self.type = type_to_define
        if type_to_define != self.FOOD:
            self.food_amount = 0

    def add_ant(self, ant_to_add):
        '''
        Adds an Ant to the cell; Does not return anything

        Parameters
        --------
        ant_to_add
            Ant instance, the Ant to be added
        '''
        self.ants = self.ants.union({ant_to_add})

    def delete_ant(self, ant_to_delete):
        '''
        Add an ant in this cell

        Parameters
        --------
        ant_to_delete
            Ant instance, the Ant to be deleted

        Returns
        --------
        Success
            Boolean, whether the operation is successful
        '''
        if ant_to_delete in self.ants:
            try:
                self.ants = self.ants.difference({ant_to_delete})
                return True
            except:
                return False
        else:
            return False

    def delete_all_ant(self):
        '''
        Deletes all Ants in the cell

        Returns
        --------
        Success
            Boolean, whether the operation is successful
        '''
        try:
            self.ants = set()
            return True
        except:
            return False

    def update_pheromone(self):
        '''
        Updates the total pheromone level
        
        Returns
        ------
        Cell
            Cell instance, with pheromone level updated
        '''
        pheromone_deposited = sum([ant.pheromone_deposit_amount for ant in self.ants if ant.carry_food])
        if self.type == self.OTHER:
            self.pheromone = min(max(self.INITIAL_PHEROMONE, (1 - self.RATIO_EVAPORATION)
                             * self.pheromone + pheromone_deposited),self.MAX_PHEROMONE)
        elif self.type == self.FOOD:
            if self.food_amount <= 0:
                self.type = self.OTHER
            else:
                self.food_amount -= len([ant for ant in self.ants if ant.carry_food])

    def update(self, ants):
        '''
        Updates the set of ants on cell and the total pheromone level
        
        Returns
        ------
        Cell
            Cell instance, with set of ants and pheromone level updated
        '''
        self.ants = ants
        self.update_pheromone()
        return self

    def have_ant(self):
        '''
        Judges whether there is at least an Ant on cell

        Returns
        -------
        have_boolean
            Boolean, True for have and False for not
        '''
        if len(self.ants) > 0:
            return True
        else:
            return False