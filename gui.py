import pygame as pg
import time

import math as m
import random as r
from random import randint

from ant import Ant
from map import Map
from cell import Cell
from gui_utils import *


### GLOABL VARIABLES ###

bg_location = 'assets\\bg.jpeg'

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_TRANS = (255, 255, 255, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (100, 100, 0)
TEAL = (0, 80, 80)
ORANGE = (255, 128, 0)

scale = 30

# Button choice
RANDOM_GENERATE = 1
USER_DEFINED = 2
ABOUT_US = 3
QUIT = 4
RESTART = 5

### Parameters of the universe ###
iterations = 0  # Number of generations of the ants
labels = []
buttons = []
inputboxs = []
enableDrawAnts = True  # Enable / disable drawing of ants
enableMessages = True  # Enable / disable messages in the console


def drawPoint(screen,color,alpha,y,x,size=scale):
    '''
    Draws a point as a square at the specified coordinates
    
    Parameters
    ------
    color
        String of initial color of the window
    alpha
        Integral of level of the color
    x, y 
        Integral of graph scale
    '''
    s = pg.Surface((size, size)) # Size of rectangle
    s.set_alpha(alpha) # Alpha level  surface transparency
    s.fill(color) # Fills the entire surface
    # (0,0) are the top-left-most coordinates
    screen.blit(s, (x * scale+(scale-size)/2, y * scale+(scale-size)/2))
    #pg.draw.rect(screen, color, (x*scale, y*scale, scale, scale), 0)
    return (x*scale, y*scale)


def drawMap(screen,map):
    '''
    Drawing a map, Nest in blue, Food in Red(degree changed by its amount), Obstacal in Grey, Background in White
    '''
    global scale
    scale = int(min(SCREEN_MAX_HEIGHT/map.len_y(),(SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH)/map.len_x()))
    ini_map=map.map()
    screen.fill(WHITE)
    for i in range(map.len_y()):
        for j in range(map.len_x()):
            cell=ini_map[i][j]
            if cell.type == Cell.NEST:
                drawPoint(screen,BLUE, 255, i, j,size=scale)
            elif cell.type == Cell.FOOD:
                if (map.init_food_amount() > 0):
                    foodAlpha = cell.food_amount / map.init_food_amount() * 200 + 55
                else:
                    foodAlpha = 255
                drawPoint(screen,RED, foodAlpha, i, j,size=scale)
            elif cell.type == Cell.OBSTACLE:
                drawPoint(screen,BROWN, 100, i, j,size=scale)
            else:
                pheromoneGray = 255 - \
                    (ini_map[i][j].pheromone - Cell.INITIAL_PHEROMONE) * 4
                pheromoneGreen = 2 * pheromoneGray
                if (pheromoneGray < 0):
                  pheromoneGray = 0
                if (pheromoneGreen < 50):
                    pheromoneGreen = 50
                if (pheromoneGray > 255):
                  pheromoneGray = 255
                if (pheromoneGreen > 255):
                  pheromoneGreen = 255
                drawPoint(screen,(pheromoneGray, pheromoneGreen,
                           pheromoneGray), 255, i, j,size=scale)


def drawAndMoveAnts(screen,map):
        '''
        Drawing and moving of ants, everytime the ant moves, update the graph
        '''
        for ant in map.all_ants():
            ant.move_ant(map)
            if enableDrawAnts:
                if ant.carry_food:
                    drawPoint(screen,BLACK, 100, ant.cell.position_y, ant.cell.position_x,size=scale/2)
                else:
                    drawPoint(screen,TEAL, 50, ant.cell.position_y, ant.cell.position_x,size=scale/2)


def inc():
    '''
    Iterations process
    '''
    global iterations
    iterations += 1


def welcome(screen):
    '''
    The welcome page

    Returns
    -------
    Button_choosen
        Integer, the button choosen, among: RANDOM_GENERATE, USER_DEFINED and ABOUT_US
    '''
    #Labels and buttons
    bg = pg.image.load(bg_location)
    screen.blit(bg, (0, 0))
    welcome_label = Label('Ant Colony Algorithm (ACO) Simulation',
                          RED, screen, centered_x=True, y_percent=1/6)
    random_generate_button = Button(
        'Generate Randomly', TEAL, screen, x_percent=1/2, y_percent=2/6)
    user_defined_button = Button(
        'Define Map and Generate', TEAL, screen, x_percent=1/2, y_percent=2/5)
    about_us_button = Button('About Us', TEAL, screen,
                             x_percent=1/2, y_percent=3/6)
    
    while True:
        # Detection of event
        for event in pg.event.get():
            # Quit
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            #Button 
            if pg.mouse.get_pressed()[0]:
                if random_generate_button.check_click(pg.mouse.get_pos()):
                    return RANDOM_GENERATE
                elif user_defined_button.check_click(pg.mouse.get_pos()):
                    return USER_DEFINED
                elif about_us_button.check_click(pg.mouse.get_pos()):
                    return ABOUT_US

        #Display the buttons and labels    
        welcome_label.display()
        random_generate_button.display()
        user_defined_button.display()
        about_us_button.display()
        pg.display.flip()


def run(screen, ini_map):
    '''
    Run the simulation

    Returns
    -------
    restart
        Boolean, whether the user want to restart
    '''
    # Labels and buttons
    noStop = True
    noPause = True

    green_rect = Rectangle(screen, x_percent=26/32, y_percent=1/48,
                           w_percent=1/32, h_percent=1/32,  color=GREEN)
    introducing_label_green = Label(
        'Pheromone', GREEN, screen, x_percent=59/64, y_percent=1/48)
    blue_rect = Rectangle(screen, x_percent=26/32, y_percent=3/48,
                          w_percent=1/32, h_percent=1/32,  color=BLUE)
    introducing_label_blue = Label(
        'Nest', BLUE, screen, x_percent=28/32, y_percent=3/48)
    brown_rect = Rectangle(screen, x_percent=26/32, y_percent=5/48,
                           w_percent=1/32, h_percent=1/32,  color=BROWN)
    introducing_label_brown = Label(
        'Obstacle', BROWN, screen, x_percent=29/32, y_percent=5/48)
    red_rect = Rectangle(screen, x_percent=26/32, y_percent=7/48,
                         w_percent=1/32, h_percent=1/32,  color=RED)
    introducing_label_red = Label(
        'Food', RED, screen, x_percent=56/64, y_percent=7/48)
    grey_rect = Rectangle(screen, x_percent=26/32, y_percent=9/48,
                           w_percent=1/48, h_percent=1/48,  color=(105, 105, 105))
    introducing_label_grey = Label(
        'Ant', (105, 105, 105), screen, x_percent=56/64, y_percent=9/48)
    nests_label = Label('Nests', BLUE, screen, x_percent=(
        SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent=6/16)
    obstacles_label = Label('Obstacles', BLUE, screen, x_percent=(
        SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent=7/16)
    numAnts_label = Label('Num of Ants', BLUE, screen, x_percent=(
        SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent=8/16)
    generation_label = Label('Generation', BLUE, screen, x_percent=(
        SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent=9/16)
    pause_button = Button('Pause', GREEN, screen, x_percent=(
        SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent=12/16)
    stop_button = Button('Quit', GREEN, screen, x_percent=(
        SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent=14/16)
    Rects_Labels_Buttons = [
        [green_rect, blue_rect, brown_rect, red_rect, grey_rect],
        [introducing_label_green, introducing_label_blue,
            introducing_label_brown, introducing_label_red, introducing_label_grey, generation_label, obstacles_label, nests_label, numAnts_label],
        [pause_button, stop_button]
    ]

    while noStop:
        if noPause:
            # Normal run
            # Detection of event
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    noStop = False
                if pg.mouse.get_pressed()[0]:
                    if pause_button.check_click(pg.mouse.get_pos()):
                        noPause = False
                        pause_button.changetext('Continue', RED)
                    elif stop_button.check_click(pg.mouse.get_pos()):
                        noStop = False

            #Draw the map part
            drawMap(screen, ini_map)
            ini_map.initAnts()
            drawAndMoveAnts(screen, ini_map)

            #Display the buttons and labels
            for i in range(len(Rects_Labels_Buttons)):
                for item in Rects_Labels_Buttons[i]:
                    item.display()

            #Put on the screen
            pg.display.flip()

            #Update
            ini_map.update()
            inc()
            obstacles_label.changetext('Obstacles: '+str(ini_map._Map__numObstacles))
            nests_label.changetext('Nests: '+str(ini_map._Map__numNest))
            numAnts_label.changetext(
                'Ants_Num: '+str(ini_map._Map__numAnts + iterations*(ini_map._Map__numAnts_spawn_per_round)))
            generation_label.changetext('Iteration: '+str(iterations))

            #Detection if have food
            if not ini_map.have_food():
                answer = quit(screen)
                if answer == QUIT:
                    return False
                elif answer == RESTART:
                    return True
            time.sleep(0.1)
        else:
            # Pause button presed and simulation paused
            # Detection of event
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if pg.mouse.get_pressed()[0]:
                    if pause_button.check_click(pg.mouse.get_pos()):
                        noPause = True
                        pause_button.changetext('Pause', GREEN)
                    elif stop_button.check_click(pg.mouse.get_pos()):
                        noStop = False

            #Display and show
            pause_button.display()
            stop_button.display()

            pg.display.flip()


def quit(screen):
    '''
    Quit page,used in the run(screen)

    Returns
    -------
    Button_choosen
        Integer, the button choosen, among: QUIT and RESTART
    '''
    #Buttons, labels and others
    cover = pg.Rect(0, 0, SCREEN_MAX_WIDTH, SCREEN_MAX_HEIGHT)
    finish_label = Label('Oooooops! All the food has been eaten.',BROWN,screen,x_percent= 1/2, y_percent= 1/4)
    iteration_label = Label('It took '+str(iterations)+' iteration(s).',BROWN,screen,x_percent= 1/2, y_percent= 1/2)
    quit_button = Button('Quit',RED,screen,x_percent= 1/4, y_percent= 3/4)
    restart_button = Button('Return to Simulation Menu',GREEN,screen,x_percent= 3/4, y_percent= 3/4)

    noStop = True
    while noStop:
        #Detection of event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return QUIT
            if pg.mouse.get_pressed()[0]:
                if quit_button.check_click(pg.mouse.get_pos()):
                    return QUIT
                elif restart_button.check_click(pg.mouse.get_pos()):
                    return RESTART

        #Display and show
        pg.draw.rect(screen, WHITE_TRANS, cover,0)
        finish_label.display()
        iteration_label.display()
        quit_button.display()
        restart_button.display()
        
        pg.display.flip()


def customize(screen):
    '''
    Display the customized screen
    Provide self-editing options: [size_of_map, numbers of Obstacle, numbers of food, numbers of nest, numbers of initial ants, numbers of newborn ants per generation, freespace]
    
    Return
    -----
    args
        Dict, Map's arguments, including keys in inputboxs 
    '''
    def do_click1(btn):
        btn.text = 'Waiting'

    def do_click2(btn):
        btn.text = 'Waiting'

    def do_click3(btn):
        main()

    args = {'len_y': 20, 'len_x': 20, 'numFood': 3, 'numObstacles': 10, 'numAnts': 25,
            'numAnts_spawn_per_round': 1, 'freeSpace': 4, 'numNest': 1, 'init_food_amount': 10}
    clock = pg.time.Clock()
    input_label1_x = Label('Size_Y of Map',
                           WHITE, screen, x_percent=2/16, y_percent=1/16, FONT=INPUT_LABEL_FONT)
    len_y = InputBox(x_percent=6/16, y_percent=1/16, w_percent=1/4,
                     h_percent=1/16, screen=screen, key='len_y', text='20')
    input_label1_y = Label('Size_X of Map',
                           WHITE, screen, x_percent=10/16, y_percent=1/16, FONT=INPUT_LABEL_FONT)
    len_x = InputBox(x_percent=27/32, y_percent=1/16, w_percent=1/4, h_percent=1/16, screen=screen, key='len_x',
                     text='20')
    input_label2 = Label('Number of Obstacles',
                         WHITE, screen, x_percent=2/16, y_percent=5/32, FONT=INPUT_LABEL_FONT)
    numObstacles = InputBox(x_percent=6/16, y_percent=5/32, w_percent=1/4,
                            h_percent=1/16, screen=screen, key='numObstacles', text='10')
    input_label3 = Label('Number of Food',
                         WHITE, screen, x_percent=10/16, y_percent=5/32, FONT=INPUT_LABEL_FONT)
    numFood = InputBox(x_percent=27/32, y_percent=5/32, w_percent=1/4,
                       h_percent=1/16, screen=screen, key='numFood', text='3')
    input_label4 = Label('Initial Number of Ants',
                         WHITE, screen, x_percent=2/16, y_percent=8/32, FONT=INPUT_LABEL_FONT)
    numAnts = InputBox(x_percent=6/16, y_percent=8/32, w_percent=1/4,
                       h_percent=1/16, screen=screen, key='numAnts', text='25')
    input_label5 = Label('Ants Spawn Rate',
                         WHITE, screen, x_percent=10/16, y_percent=8/32, FONT=INPUT_LABEL_FONT)
    numAnts_spawn_per_round = InputBox(x_percent=27/32, y_percent=8/32, w_percent=1/4,
                                       h_percent=1/16, screen=screen, key='numAnts_spawn_per_round', text='1')
    input_label6 = Label('Free Space',
                         WHITE, screen, x_percent=2/16, y_percent=11/32, FONT=INPUT_LABEL_FONT)
    freeSpace = InputBox(x_percent=6/16, y_percent=11/32, w_percent=1/4,
                         h_percent=1/16, screen=screen, key='freeSpace', text='4')
    input_label7 = Label('Number of Nests',
                         WHITE, screen, x_percent=10/16, y_percent=11/32, FONT=INPUT_LABEL_FONT)
    numNest = InputBox(x_percent=27/32, y_percent=11/32, w_percent=1/4,
                       h_percent=1/16, screen=screen, key='numNest', text='1')
    input_label8 = Label('Souce Food Amount',
                         WHITE, screen, x_percent=2/16, y_percent=14/32, FONT=INPUT_LABEL_FONT)
    init_food_amount = InputBox(x_percent=12/32, y_percent=14/32, w_percent=1/4,
                                h_percent=1/16, screen=screen, key='init_food_amount', text='10')
    input_label9 = Label('(Food Amount at Each Food Cell)',
                         WHITE, screen, x_percent=11/16, y_percent=14/32, FONT=INPUT_LABEL_FONT)
    input_label10 = Label('Please Input the Appropriate Value, Otherwise Errors may Occur!',
                          ORANGE, screen, x_percent=8/16, y_percent=18/32)
    input_boxes = [len_y, len_x, numFood, numObstacles,
                   numAnts, numAnts_spawn_per_round, freeSpace, numNest, init_food_amount]
    confirm_button = Button('Confirm', GREEN, screen,
                            x_percent=1/6, y_percent=3/4, click=do_click1)
    default_button = Button('Default', ORANGE, screen,
                            x_percent=3/6, y_percent=3/4,
                            click=do_click2)
    return_button = Button('Return', RED, screen,
                           x_percent=5/6, y_percent=3/4, click=do_click3)

    buttons = [confirm_button, default_button, return_button]
    labels = [input_label1_y, input_label1_x, input_label2, input_label3, input_label4,
              input_label5, input_label6, input_label7, input_label8, input_label9, input_label10]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if pg.mouse.get_pressed()[0]:
                if confirm_button.check_click(pg.mouse.get_pos()):

                    keys = []
                    values = []
                    for i in range(len(input_boxes)):
                        keys.append(input_boxes[i].get_key())
                        values.append(int(input_boxes[i].get_value()))
                    args = dict(zip(keys, values))
                    time.sleep(0.1)
                    done = True
                if default_button.check_click(pg.mouse.get_pos()):
                    done = True

                if return_button.check_click(pg.mouse.get_pos()):
                    pass
            confirm_button.update(event)
            default_button.update(event)
            return_button.update(event)

            for box in input_boxes:
                box.handle_event(event)

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.update()
        for box in input_boxes:
            box.draw(screen)
        for box in buttons:
            box.display()
        for label in labels:
            label.display()

        pg.display.flip()
        clock.tick(30)
    
    size = (args['len_y'], args['len_x'])
    numAnts = args['numAnts']
    numAnts_spawn_per_round = args['numAnts_spawn_per_round']
    numFood = args['numFood']
    numObstacles = args['numObstacles']
    freeSpace = args['freeSpace']
    numNest = args['numNest']
    init_food_amount = args['init_food_amount']
    return Map(size, random_create=True, numAnts=numAnts, numAnts_spawn_per_round=numAnts_spawn_per_round, numFood=numFood,
                              init_food_amount=init_food_amount, numObstacles=numObstacles, min_food_dis=2, max_food_dis=20, freeSpace=freeSpace, numNest=numNest)

def user_defined(screen):
    '''
    Ask user to define the map to use

    Returns
    -------
    map_choosen
        Map, the map that the user have choosen
    '''
    
    #Buttons, inputboxes
    screen.fill(BLACK)
    predefined_button = Button('Pre-defined simple map',GREEN,screen,x_percent= 1/2, y_percent= 1/5)
    draw_button = Button('Draw a map using a canvas with size input below',GREEN,screen,x_percent= 1/2, y_percent= 3/5) 
    size_x_input_box = InputBox(x_percent=1/4, y_percent=4/5, w_percent=1/5, h_percent=1/16, screen=screen, text='20')
    size_y_input_box = InputBox(x_percent=3/4, y_percent=4/5, w_percent=1/5, h_percent=1/16, screen=screen, text='20')

    while True:
        #Event detection
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return None
            if pg.mouse.get_pressed()[0]:
                if predefined_button.check_click(pg.mouse.get_pos()):
                    return Map((20,20),numAnts=50,numAnts_spawn_per_round=1,init_food_amount=1000,random_create=False,nest_coordinates=[(1,1)],food_coordinates=[(8,5)],food_amounts=[20],obstacle_coordinates=[(3,0)],obstacle_sizes=[(3,4)])
                elif draw_button.check_click(pg.mouse.get_pos()):
                    return userdraw(screen,int(size_x_input_box.text),int(size_y_input_box.text))
            size_x_input_box.handle_event(event)
            size_y_input_box.handle_event(event)
            size_x_input_box.update()
            size_y_input_box.update()

        #Display and show
        predefined_button.display()
        draw_button.display()
        size_x_input_box.draw(screen)
        size_y_input_box.draw(screen)
        
        pg.display.flip()
    

def userdraw(screen,size_x=20,size_y=20):
    '''
    Ask user to draw a map

    Parameters
    -------
    screen
        The screen to draw on
    size_x
        The size of the map,defalute to be 20
    size_y
        The size of the map,defalute to be 20

    Returns
    -------
    map_drawn
        Map, the map that the user have drawn
    '''
    #Parameters
    global scale
    scale = int(min(SCREEN_MAX_HEIGHT/size_y,(SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH)/size_x))
    color = WHITE
    number = 0
    numAnts_spawn_per_round = 1
    nest_coordinates = []
    food_coordinates = []
    food_amounts = []
    obstacle_coordinates = []
    
    #Initialisation of Button Labels etc.
    draw_map = []
    for i in range(size_y):
        row = []
        for j in range(size_x):
            row.append(CellButton(j*scale,i*scale,scale,scale,color))
        draw_map.append(row)

    situation_label = Label('No Brush Selected',BLACK,screen,x_percent= (SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent= 1/11)
    nest_button = Button('Nest Brush',BLUE,screen,x_percent= (SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent= 2/11)
    num_ant_label = Label('Set Spawn Rate',BLACK,screen,x_percent= (SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent= 3/11)
    num_ant_input_box = InputBox(x_percent=(SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent=4/11, w_percent=SCREEN_CONFIG_WIDTH*2/3/SCREEN_MAX_WIDTH, h_percent=1/16, screen=screen, text='1')
    
    food_button = Button('Food Brush',RED,screen,x_percent= (SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent= 5/11)
    food_amount_label = Label('Set Food Amount',BLACK,screen,x_percent= (SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent= 6/11)
    food_amount_input_box = InputBox(x_percent=(SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent=7/11, w_percent=SCREEN_CONFIG_WIDTH*2/3/SCREEN_MAX_WIDTH, h_percent=1/16, screen=screen, text='20')

    obstacle_button = Button('Obstacle Brush',BROWN,screen,x_percent= (SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent= 8/11)
    
    clean_button = Button('Eraser',ORANGE,screen,x_percent= (SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent= 9/11)
    finish_button = Button('FINISH',GREEN,screen,x_percent= (SCREEN_MAX_WIDTH-SCREEN_CONFIG_WIDTH/2)/SCREEN_MAX_WIDTH, y_percent= 10/11)
    
    
    
    while True:
        screen.fill(WHITE)
        # Event detection
        for event in pg.event.get():
            # Quit
            if event.type == pg.QUIT:
                return None
            if pg.mouse.get_pressed()[0]:
                # Event button
                if nest_button.check_click(pg.mouse.get_pos()):
                    color =  BLUE
                    number = int(num_ant_input_box.text)
                    situation_label.changetext('Drawing Nest...')
                elif food_button.check_click(pg.mouse.get_pos()):
                    color = RED
                    number = int(food_amount_input_box.text) 
                    situation_label.changetext('Drawing Food...')
                elif obstacle_button.check_click(pg.mouse.get_pos()):
                    color = BROWN
                    number = 0
                    situation_label.changetext('Drawing Obstacle...')
                elif clean_button.check_click(pg.mouse.get_pos()):
                    color = WHITE
                    number = 0
                    situation_label.changetext('Erasing...')
                elif finish_button.check_click(pg.mouse.get_pos()):
                    return Map((20,20),numAnts=0,numAnts_spawn_per_round=numAnts_spawn_per_round,random_create=False,nest_coordinates=nest_coordinates,food_coordinates=food_coordinates,food_amounts=food_amounts,obstacle_coordinates=obstacle_coordinates)
                
                # Draw button
                for i in range(size_y):
                    for j in range(size_x):
                        if draw_map[i][j].check_click(pg.mouse.get_pos()):
                            if color == BLUE:
                                #Draw nest
                                if draw_map[i][j].color == BLUE:
                                    nest_coordinates.remove((i,j))
                                elif draw_map[i][j].color == RED:
                                    index = food_coordinates.index((i,j))
                                    del(food_coordinates[index])
                                    del(food_amounts[index])
                                elif draw_map[i][j].color == BROWN:
                                    obstacle_coordinates.remove((i,j))
                                nest_coordinates.append((i,j))
                            elif color == RED:
                                #Draw food
                                if draw_map[i][j].color == BLUE:
                                    nest_coordinates.remove((i,j))
                                elif draw_map[i][j].color == RED:
                                    index = food_coordinates.index((i,j))
                                    del(food_coordinates[index])
                                    del(food_amounts[index])
                                elif draw_map[i][j].color == BROWN:
                                    obstacle_coordinates.remove((i,j))
                                food_amounts.append(number)
                                food_coordinates.append((i,j))
                            elif color == BROWN:
                                #Obstacle food
                                if draw_map[i][j].color == BLUE:
                                    nest_coordinates.remove((i,j))
                                elif draw_map[i][j].color == RED:
                                    index = food_coordinates.index((i,j))
                                    del(food_coordinates[index])
                                    del(food_amounts[index])
                                elif draw_map[i][j].color == BROWN:
                                    obstacle_coordinates.remove((i,j))
                                obstacle_coordinates.append((i,j))
                            elif color == WHITE:
                                #Clean
                                if draw_map[i][j].color == BLUE:
                                    nest_coordinates.remove((i,j))
                                elif draw_map[i][j].color == RED:
                                    index = food_coordinates.index((i,j))
                                    del(food_coordinates[index])
                                    del(food_amounts[index])
                                elif draw_map[i][j].color == BROWN:
                                    obstacle_coordinates.remove((i,j))
                            draw_map[i][j].color = color
                            draw_map[i][j].change_text(str(number) if number != 0 else '')
            num_ant_input_box.handle_event(event)
            food_amount_input_box.handle_event(event)
            num_ant_input_box.update()
            food_amount_input_box.update()
        
        #Display and show
        situation_label .display()
        nest_button.display()
        num_ant_label.display()
        num_ant_input_box.draw(screen)
        food_button.display()
        food_amount_label.display()
        food_amount_input_box.draw(screen)
        obstacle_button.display()
        clean_button.display()
        finish_button.display()
        
        for i in range(size_y):
            for j in range(size_x):
                draw_map[i][j].display(screen)
        
        pg.display.flip()
    return None

def about_us(screen):
    '''
    About us page

    Returns
    -------
    restart
        Boolean, if we go to the welcome page
    '''
    #Buttons, labels and others
    screen.fill(BLACK)
    label0 = Label('CentraleSupélec Coding Weeks Semaine 2',BROWN,screen,x_percent= 1/2, y_percent= 1/5)
    label1 = Label('Ant Colony Optimisation (ACO) Simulation',BROWN,screen,x_percent= 1/2, y_percent= 3/10)
    label2 = Label('Members:',BLUE,screen,x_percent= 1/2, y_percent= 4/10)
    label3 = Label('Chensheng Luo, Haonan Lin',BLUE,screen,x_percent= 1/2, y_percent= 9/20)
    label4 = Label('Mingshan Ye, Raven Bast',BLUE,screen,x_percent= 1/2, y_percent= 1/2)
    label5 = Label('Yue Yang Oo',BLUE,screen,x_percent= 1/2, y_percent= 11/20)
    quit_button = Button('Quit',RED,screen,x_percent= 1/4, y_percent= 3/4)
    restart_button = Button('Return to Simulation Menu',GREEN,screen,x_percent= 3/4, y_percent= 3/4)

    noStop = True
    while noStop:
        #Detection of event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            if pg.mouse.get_pressed()[0]:
                if quit_button.check_click(pg.mouse.get_pos()):
                    return False
                elif restart_button.check_click(pg.mouse.get_pos()):
                    return True

        #Display and show
        label0.display()
        label1.display()
        label2.display()
        label3.display()
        label4.display()
        label5.display()
        quit_button.display()
        restart_button.display()
        
        pg.display.flip()

def main():
    #### Initialization of pygame and clock

    pg.init()
    pg.display.set_caption("Ant Colony Simulation")

    screen = pg.display.set_mode([SCREEN_MAX_WIDTH, SCREEN_MAX_HEIGHT])

    ## Initialization of welcome window
    restart = True
    while restart:
        answer = welcome(screen)
        ## Initialization of files
        if answer == USER_DEFINED:
            ini_map = user_defined(screen)
            if ini_map is not None:
                ini_map.initAnts()
                restart = run(screen,ini_map)
            else:
                restart = False
        elif answer == RANDOM_GENERATE:
            ini_map = customize(screen)
            if ini_map is not None:
                ini_map.initAnts()
                restart = run(screen,ini_map)
            else:
                restart = False
        elif answer == ABOUT_US:
            restart = about_us(screen)
            
    
    pg.quit()
    
if __name__ == "__main__":
    main()
