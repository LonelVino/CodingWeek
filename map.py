from cell import Cell
from ant import Ant

import math as m
import random as r
from random import randint


class Map(object):
    '''
    NB: In this file, all of the parameters has been defined as PRIVATE VARIABLE
    as once they are created, they can't be changed random, they can change it only by predefined function!
    '''
    # Map dimension
    __map = [] # The map itself
    __len_y = 0 # The length y of the map
    __len_x = 0 # The length x of the map
    
    ### Ants in map
    __all_ants = [] # The list of all of ants
    __numAnts = 2000 # Maximum limit for number of ants TODO：do a change
    __numAnts_spawn_per_round = 10 # Number of ants spawned per round

    ### Nest in map
    __numNest = 1 # Amount of nest cells in map
    __nestList = []
    
    ### Food in map
    __foodList = []
    __numFood = 10 # Amount of food cells in map
    __min_food_dis = 20 # Minimum distance to food on each side
    __max_food_dis = 100 # Maximum distance to food on each side
    __init_food_amount = 50  # Initial amount of food

    ### Obstacles in map
    __numObstacles = 1000
    __freeSpace = 8 # Free space left around nest and food

    def __init__(self,size,numAnts = 2000,numAnts_spawn_per_round = 10,init_food_amount = 50,random_create=True,
    numNest = 1,numFood = 10, min_food_dis = 20,max_food_dis = 100,numObstacles = 1000, freeSpace = 8,
    nest_coordinates=[],nums_ants_nest=[],food_coordinates=[],food_sizes=[],food_amounts=[],
    obstacle_coordinates=[],obstacle_sizes=[]):
        '''
        Creates a new empty map, either randomly or user-defined

        Common Parameters
        -------
        size
            Tuple (y,x), where first int is number of rows and second int is number of columns
        numAnts
            Integer for maximum limit for number of ants
        numAnts_spawn_per_round
            Integer for number of ants spawned per round
        random_create
            Boolean, True enables random creation, False indicates user-defined creation

            Parameters useful ONLY for random creation
            --------
            numNest 
                Integer, number of nest cells, default to be 1
            numFood
                Integer, number of food cells, default to be 10
            min_food_dis
                Integer, minimun food distance, default to be 20
            max_food_dis
                Integer, maximum food distance, default to be 100
            numObstacles
                Integer, number of Obstacles, default to be 1000
            freeSpace
                Integer, space to leave around nest and food, default to be 8

            Parameters useful ONLY for user-defined creation
            --------
            nest_coordinates
                List of tuple[(y1,x1),(y2,x2),..], list of nest coordinates, default to be []
            nums_ants_nest
                List of Integer[num1,num2...], list of number at each ant, default to be uniform distribution
            food_coordinates
                List of tuple[(y1,x1),(y2,x2),..], list of food coordinates, default to be []
            food_sizes
                List of tuple[(size_y1,size_x1),(size_y2,size_x2),..], list of food sizes, default to be (1,1) for each
            food_amounts
                List of Integer[num1,num2...], list of food amount, default to be self.__init_food_amount
            obstacle_coordinates
                List of tuple[(y1,x1),(y2,x2),..], list of obstacle coordinates, default to be []
            obstacle_sizes
                List of tuple[(size_y1,size_x1),(size_y2,size_x2),..], list of obstacle sizes, default to be (1,1) for each
        '''
        # Common part
        self.__len_y = size[0]
        self.__len_x = size[1]
        self.__create_empty_map(size)
        self.__numAnts = numAnts
        self.__all_ants = []
        self.__numAnts_spawn_per_round = numAnts_spawn_per_round

        if random_create:
            # Random creation
            self.__numNest= numNest
            self.__numFood = numFood
            self.__min_food_dis = min_food_dis
            self.__max_food_dis = max_food_dis
            self.__init_food_amount = init_food_amount
            self.__numObstacles = numObstacles
            self.__freeSpace = freeSpace

            self.__random_add_nest()
            self.__random_add_food()
            self.__random_add_obstacle()

        else:
            # User-defined creation
            self.__nestList = []
            for i in range(len(nest_coordinates)):
                if nums_ants_nest == []:
                    self.__add_nest(nest_coordinates[i],int(numAnts/len(nest_coordinates)))
                else:
                    self.__add_nest(nest_coordinates[i],nums_ants_nest[i])
            self.__numNest=len(nest_coordinates)

            self.__foodList = []
            for i in range(len(food_coordinates)):
                if food_amounts == []:
                    if food_sizes == []:
                        self.__add_food(food_coordinates[i])
                    else:
                        self.__add_food(food_coordinates[i],food_size=food_sizes[i])
                else:
                    if food_sizes == []:
                        self.__add_food(food_coordinates[i],food_amount=food_amounts[i])
                    else:
                        self.__add_food(food_coordinates[i],food_size=food_sizes[i],food_amount=food_amounts[i])
            self.__numFood = len(food_coordinates)

            for i in range(len(obstacle_coordinates)):
                    if obstacle_sizes == []:
                        self.__add_obstacle(obstacle_coordinates[i])
                    else:
                        self.__add_obstacle(obstacle_coordinates[i],size=obstacle_sizes[i])
            self.__numObstacles = len(obstacle_coordinates)

    def __str__(self):
        s=''
        for i in range(self.__len_y):
            s= s + '['
            for j in range(self.__len_x):
                s = s + '(' + self.__map[i][j].__str__ + ')'
            s = s + '\n' + ']'
        return s

    # These functions gives the parameters needed, without change it
    def map(self): return self.__map
    def all_ants(self): return self.__all_ants
    def init_food_amount(self): return self.__init_food_amount
    def foodList(self): return self.__foodList
    def nestList(self): return self.__nestList
    def len_x(self): return self.__len_x
    def len_y(self): return self.__len_y 

    def __create_empty_map(self,size):
        '''
        Creates a new empty map

        Parameters
        -------
        size
            Tuple (y,x) where first int is number of rows and second int is number of columns
        '''
        self.__len_y=size[0]
        self.__len_x=size[1]
        self.__map = []
        for i in range(self.__len_y):
            map_row = []
            for j in range(self.__len_x):
                map_row.append(Cell(i,j,set(),Cell.OTHER))
            self.__map.append(map_row)

    def __change_type(self,coordinates,type_change_to,size=(1,1)):
        '''
        Adds food to the map

        Parameters
        -------
        coordinate
            Tuple (y,x), the left top coordinates of the node to be changed to food
        type_change_to
            String, the type that we want to change to
        size
            Tuple (y,x), the size of the food to be added, default to be (1,1)
        
        Returns
        --------
        changed
            List, the list of the changed cells
        '''
        # Parameters
        size_y, size_x, y, x = size[0], size[1], coordinates[0], coordinates[1]
        changed=[]

        # Chaneg by iterations
        if y + size_y <= self.__len_y and x + size_x <= self.__len_x:
            for i in range(size_y):
                for j in range(size_x):
                    self.__map[y + i][x + j].type = type_change_to
                    changed.append(self.__map[y + i][x + j])

        else:
            raise ValueError('Indice outside of the map')

        return changed
        
    def __add_nest(self,coordinate,num_ants_nest):
        '''
        Adds nest to the map

        Parameters
        -------
        coordinate
            Tuple (y,x), coordinate of the node to be changed to nest
        '''
        #Update the map
        nests = self.__change_type(coordinate,Cell.NEST)
        #Update the nestList
        for nest in nests:
            nest.num_ants_nest=num_ants_nest
            self.__nestList.append(nest)

    def __add_food(self,coordinates,size=(1,1),food_amount=None):
        '''
        Adds food to the map

        Parameters
        -------
        coordinate
            Tuple (y,x), the left top coordinates of the node to be changed to food
        size
            Tuple (y,x), the size of the food to be added, default to be (1,1)
        food_amount
            Interger, the amount of food, defalut to be init_food_amount
        '''
        #Get the food amount
        if food_amount == None:
            food_amount = self.__init_food_amount
        
        #Update map
        foods = self.__change_type(coordinates,Cell.FOOD,size=size)

        #Update foodList
        for food in foods:
            food.food_amount = food_amount
            self.__foodList.append(food)


    def __add_obstacle(self,coordinates,size=(1,1)):
        '''
        Adds obstacle to the map

        Parameters
        -------
        coordinate
            Tuple (y,x), the left top coordinate of the node to be changed to obstacle
        size
            Tuple (y,x), the size of the obstacle to be added, default to be (1,1)

        '''
        #Update map
        self.__change_type(coordinates,Cell.OBSTACLE,size=size)

    def __random_add_nest(self):
        '''
        Generate nests randomly in the map
        '''
        #Generate num_ants_nest randomly
        num_ants_nest = [r.randint(0, self.__numAnts) for i in range(self.__numNest)]
        num_ants_nest = [0] + sorted(num_ants_nest) + [self.__numAnts]
        num_ants_nest = [num_ants_nest[i + 1] - num_ants_nest[i]
                     for i in range(self.__numNest - 1)]
        num_ants_nest.append(self.__numAnts - sum(num_ants_nest))
        
        #Generate its coordinate randomly
        for i in range(self.__numNest):
            self.__add_nest((r.randint(self.__freeSpace, self.__len_y-self.__freeSpace-1), r.randint(self.__freeSpace, self.__len_x-self.__freeSpace-1)),num_ants_nest[i])


    def __random_add_food(self):
        '''
        Generate food randomly in the map
        '''
        for i in range(self.__numFood):
            stopGenerateFood = False
            while not stopGenerateFood:
                foodX = r.randint(5, self.__len_x - 6) 
                foodY = r.randint(5, self.__len_y - 6) 
                foodSize = (r.randint(1, 4), r.randint(1, 4)) 
                foodSuccess = True
                for nest in self.__nestList:
                    foodSuccess = foodSuccess and (self.__map[foodY][foodX].distance_to(nest) in range(self.__min_food_dis,self.__max_food_dis))
                if foodSuccess:
                    if self.__map[foodY][foodX] not in self.__foodList:
                        self.__add_food((foodY, foodX), size=foodSize)
                        stopGenerateFood = True

    def __random_add_obstacle(self):
        '''
        Generate obstacles randomly in the map
        '''
        for _ in range(self.__numObstacles):
            stopGenerateObs = 0
            while stopGenerateObs < self.__numFood/2:   
                obstacleX = r.randint(3, self.__len_x - 3) 
                obstacleY = r.randint(3, self.__len_x - 3) 
                obstacleSize = (r.randint(1, 2), r.randint(1, 2)) 
                for y in range(obstacleSize[0]):
                    for x in range(obstacleSize[1]):
                        current_cell=self.__map[obstacleY+y][obstacleX+x]

                        if current_cell.type in [Cell.OBSTACLE, Cell.FOOD, Cell.NEST]:
                            continue
                        
                        else:
                            nestSuccess = True
                            for nest in self.__nestList:
                                nestSuccess = nestSuccess and (current_cell.distance_to(nest) >= self.__freeSpace)
                            if nestSuccess:
                                stopGenerateObs += obstacleSize[0] * obstacleSize[1]
                            else:
                                stopGenerateObs = 0
                                continue
                            for food in self.__foodList:
                                foodSuccess = current_cell.distance_to(food) >= self.__freeSpace
                                if foodSuccess:
                                    stopGenerateObs += 1
                                else:
                                    stopGenerateObs = 0
                                    continue
            self.__add_obstacle([obstacleY, obstacleX], size=obstacleSize)
    
    def initAnts(self):
        '''
        Initialization of ants, every ant being in a cell is a Object; 
        For a cell, the ants on it is set(); 
        All ants is a array composed by set()  
        '''
        for nest in self.__nestList:
            self.create_ant_at_nest(nest,self.__numAnts_spawn_per_round)
    
    def update(self):
        '''
        Used only after the ants are moved
        Updates the map with the set of ants on it
        '''
    
        # Delete all old ants
        for y in range(self.__len_y):
            for x in range(self.__len_x):
                self.__map[y][x].delete_all_ant()
    
        # Add ants to their respective cells
        for ant in self.__all_ants:
            ant.cell.add_ant(ant)
    
        # Calculate the new number of pheromone,new number of food etc.
        self.__foodList = []
        for y in range(self.__len_y):
            for x in range(self.__len_x):
                self.__map[y][x].update()
                
                if  self.__map[y][x].type == Cell.FOOD:
                    self.__foodList.append(self.__map[y][x])


    def create_ant_at_nest(self,nest,numAnts_spawn_per_round):
        '''
        Create the ant at the given coordinate

        Parameter
        -------
        nest
            Cell, nest on which the ant should be created
        number_of_ant
            Integer, the number of ants to be created, default to be NBR_OF_ANT_CREATED in the nest
        '''
        #Works IFF it's a nest!
        if nest.type == Cell.NEST:
            #Get defined nest type
            # if number_of_ant is None:
            #     number_of_ant=nest.num_ants_nest
            for _ in range(numAnts_spawn_per_round):
                #Create an ant
                ant = Ant(nest)
                #Add it to the nest list
                nest.add_ant(ant)
                #Add it to the map list
                self.__all_ants.append(ant)

    def have_food(self):
        '''
        Judge whether we still have some food in the map
        '''
        if len(self.__foodList) == 0:
            return False
        else:
            result = False
            for food in self.__foodList:
                if food.food_amount != 0:
                    result = True
                    break
        return result