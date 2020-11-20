from ant import *
from map import *


def try_probabilistic_selection(ant,map):
    return ant.probabilistic_selection(map)


def try_move_ant(ant,map):
    ant.move_ant(map)

def test_all():
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
    testmap = Map((5,5),random_create=False,nest_coordinates=[(0,0)],food_coordinates=[(4,4)])

    # Test probabilistic_selection which determines next cell if not carrying food
    ant1 = Ant(testmap.map()[0][0])
    ant1_next_cell = try_probabilistic_selection(ant1,testmap)
    assert [ant1_next_cell.position_y,ant1_next_cell.position_x] in [[0,1],[1,1],[1,0]]

    # Test movement of ant entering food cell to carry food
    ant2 = Ant(testmap.map()[3][3])
    try_move_ant(ant2,testmap)
    assert [ant2.cell.position_y,ant2.cell.position_x] == [4,4]
    assert ant2.history == [testmap.map()[3][3],testmap.map()[4][4]]
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
    ant3 = Ant(testmap.map()[1][1])
    ant3.carry_food = True
    ant3.history = [testmap.map()[0][0]]
    try_move_ant(ant3,testmap)
    assert [ant3.cell.position_y,ant3.cell.position_x] == [0,0]
    assert ant3.history == [testmap.map()[0][0]]
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

if __name__ == '__main__':
    test_all()