from ant_mvp import *
from map_mvp import *


def try_probabilistic_selection(ant,map):
    return ant.probabilistic_selection(map)


def try_move_ant(ant,map):
    ant.move_ant(map)


if __name__ == '__main__':
    '''
    testmap =
    [
        [N,A,A,A,A],
        [A,A,A,A,A],
        [A,A,A,A,A],
        [A,A,A,A,A],
        [A,A,A,A,F],
    ]

    '''
    # Create testmap
    testmap = add_food([4,4],add_nest([0,0],create_empty_map([5,5])))
    
    # Test probabilistic_selection which determines next cell if not carrying food
    ant1 = Ant(testmap[0][0])
    ant1_next_cell = try_probabilistic_selection(ant1,testmap)
    assert [ant1_next_cell.position_y,ant1_next_cell.position_x] in [[0,1],[1,1],[1,0]]

    # Test movement of ant entering food cell to carry food
    ant2 = Ant(testmap[3][3])
    try_move_ant(ant2,testmap)
    assert [ant2.cell.position_y,ant2.cell.position_x] == [4,4]
    assert ant2.history == [testmap[3][3],testmap[4][4]]
    assert ant2.carry_food == True
    #print(ant2)
    #print(ant2.cell)

    # Test movement of ant leaving food cell
    try_move_ant(ant2,testmap)
    assert [ant2.cell.position_y,ant2.cell.position_x] == [3,3]
    assert ant2.history == []
    assert ant2.carry_food == True
    #print(ant2)
    #print(ant2.cell)

    # Test movement of ant returning to nest cell
    ant3 = Ant(testmap[1][1])
    ant3.carry_food = True
    ant3.history = [testmap[0][0]]
    try_move_ant(ant3,testmap)
    assert [ant3.cell.position_y,ant3.cell.position_x] == [0,0]
    assert ant3.history == [testmap[0][0]]
    assert ant3.carry_food == False
    #print(ant3)
    #print(ant3.cell)

    # Test movement of ant leaving nest cell after dropping food
    try_move_ant(ant3,testmap)
    assert [ant3.cell.position_y,ant3.cell.position_x] in [[0,1],[1,1],[1,0]]
    assert len(ant3.history) == 2
    assert ant3.carry_food == False
    #print(ant3)
    #print(ant3.cell)