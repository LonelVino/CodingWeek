import pygame as pg
from random import randint
import time

from ant_mvp import *
from map_mvp import *
from cell_mvp import *
from ant_mvp import *
from simulation_mvp import *

######################## GLOABL VARIABLES #######################
MAP_WIDTH = 20
MAP_HEIGHT = 20

# color constant
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (100, 100, 0)
TEAL = (0, 80, 80)

# graphics window scale
scale = 30

######### Parameters of the universe
numFood = 5
numObstacle = 10
foodList = []
food_amount = []
init_food_amount = 50  # Initial amount of food

#### algorithm parameters
re = Cell.RATIO_EVAPORATION   # The ratio of evaporation
freeSpace = 3

#### Ants in map
ant_limit = 25
init_pheromone = Cell.INITIAL_PHEROMONE  # initial pheromone value

#### Initialization
allAnts = []
ini_map = []

enableDrawAnts = True  # enable / disable drawing of ants
enableMessages = True  # on / off messages in the console

'''
ini_map() 
@params: map_size, nest_coordinates, food_coordinates
'''

def setFoodsAndObts(ini_map):
    # randomly set the obtsacles and foods
    for i in range(numFood):
        stopGenerateFood = False
        while not stopGenerateFood:
            foodX, foodY = randint(4, 15), randint(4, 15)
            foodSize = (randint(1, 2), randint(1, 2))
            if [foodX, foodY] not in foodList:
                for i in range(foodSize[0]):
                    for j in range(foodSize[1]):
                        foodList.append([foodY + i, foodX + j])
                        food_amount.append(init_food_amount)
                ini_map[0] = add_food((foodY, foodX), ini_map[0], size=foodSize)
                stopGenerateFood = True
    # Generate obstacles in map
    for i in range(numObstacle):
        stopGenerateObs = 0
        while stopGenerateObs < numFood/2:   # food amount + nest point
            obstacleX, obstacleY = randint(4, 15), randint(4, 15)
            obstacleSize = (randint(1, 3), randint(1, 3))
            if not ((ini_map[0][obstacleY][obstacleX].type == "O") and (ini_map[0][obstacleY][obstacleX].type == "F") and (ini_map[0][obstacleX][obstacleY].type == "N")):
                for j in range(numFood):
                    foodX, foodY = foodList[j][1], foodList[j][0]
                    foodXSuccess = (
                        obstacleX <= foodX - freeSpace) or (obstacleX >= foodX + freeSpace)
                    foodYSuccess = (
                        obstacleY <= foodY - freeSpace) or (obstacleY >= foodY + freeSpace)
                    if foodXSuccess or foodYSuccess:
                        stopGenerateObs += 1
                    else:
                        stopGenerateObs = 0
                        continue
            ini_map[0] = add_obstacle(
                [obstacleY, obstacleX], ini_map[0], size=obstacleSize)
            

def drawPoint(screen, color, alpha, x, y, size=scale):
    '''
    Draws a point as a square at the specified coordinates in the map, such as a Obstacle, Food etc
    
    Parameters
    ------
    color
        String of initial color of the window
    alpha
        Integral of level of the color
    x, y 
        Integral of graph scale
    '''
    s = pg.Surface((size, size))  # the size of your rect
    s.set_alpha(alpha)      # alpha level: a variable used to to draw a picture
    s.fill(color)       # this fills the entire surface
    # (0,0) are the top-left coordinates
    screen.blit(s, (x * scale + (scale-size)/2, y * scale + (scale-size)/2))
    return (x*scale, y*scale)
  
def drawMap(screen, map):
    '''
    Drawing a map, Ant in Black(degree by its amounts, light to dark), Nest in blue, Food in Red, Obstacle in Grey, Background in White
    Parameters
    ------
    screen


    map
        lists of data

    '''
    screen.fill(WHITE)
    for i in range(len(map[0])):
        for j in range(len(map[0][i])):
            if map[0][i][j].type == "N":
                drawPoint(screen, BLUE, 255, i, j)
            elif map[0][i][j].type == "F":
                if (init_food_amount > 0):
                    foodAlpha = food_amount[foodList.index(
                        [i, j])] / init_food_amount * 200 + 55
                else:
                    foodAlpha = 255
                drawPoint(screen, RED, foodAlpha, i, j)
            elif map[0][i][j].type == "O":
                drawPoint(screen, BROWN, 255, i, j)
            else:
                pheromoneGray = 255 - \
                    (map[0][i][j].pheromone - Cell.INITIAL_PHEROMONE) * 32
                pheromoneGreen = 8 * pheromoneGray
                if (pheromoneGray < 0):
                  pheromoneGray = 0
                if (pheromoneGreen < 50):
                    pheromoneGreen = 50
                if (pheromoneGray > 255):
                  pheromoneGray = 255
                if (pheromoneGreen > 255):
                  pheromoneGreen = 255
                drawPoint(screen, (pheromoneGray, pheromoneGreen,
                                   pheromoneGray), 255, i, j)
            
def drawAndMoveAnts(screen, data):
    data[3] = 3
    data = generate(data) 
    '''    
    data
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
    if enableDrawAnts:
        for ant in data[2]:
            if ant.cell.type == 'F':
                if food_amount[foodList.index([ant.cell.position_y, ant.cell.position_x])] > 0:
                    food_amount[foodList.index([ant.cell.position_y,
                                                ant.cell.position_x])] -= 1
                else:
                    ant.cell.type == 'A'
            if ant.carry_food == True:
                drawPoint(screen, BLACK, 100, ant.cell.position_y,
                          ant.cell.position_x, size=scale/2)
            else:
                drawPoint(screen, BLACK, 50, ant.cell.position_y,
                          ant.cell.position_x, size=scale/2)
    return data
        
def main():
    pg.init()
    pg.display.set_caption("Ant Colony Simulation MVP")
    screen = pg.display.set_mode(
        [int(MAP_WIDTH * scale), int(MAP_HEIGHT * scale)])

    ini_map = create_initial_data([20, 20], [0, 0], [7, 7], ant_limit = ant_limit)
    ini_map[2] = create_ant(ini_map[0], ini_map[1], ini_map[2], 1)
    ini_map[3] = 0
    foodList.append([7, 7])
    food_amount.append(init_food_amount)
    setFoodsAndObts(ini_map)
    
    running = True
    while running: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    
        drawMap(screen, ini_map)
        ini_map = drawAndMoveAnts(screen, ini_map)
        pg.display.flip()
        time.sleep(0.1)
        
    pg.quit()
    
if __name__ == "__main__":
    main()
