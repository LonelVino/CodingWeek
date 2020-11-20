from cell_mvp import Cell
from map_mvp import *
from ant_mvp import Ant


def create_test_map():
    '''
    test_map=[
        [N,A,A,A,A,A,A],
        [A,A,A,A,A,A,A],
        [A,A,O,O,A,A,A],
        [A,A,O,O,A,A,A],
        [A,A,A,A,A,F,A],
        [A,A,A,A,A,A,A]
    ]
    '''
    test_map = create_empty_map((6,7))
    test_map = add_nest((0,0),test_map)
    test_map = add_food((4,5),test_map)
    test_map = add_obstacle((2,2),test_map,(2,2))
    return test_map


def test_create_map():
    '''
    Tests if map is created with each cell of the correct type
    '''
    test_map = create_test_map()
    for y in range(len(test_map)):
        for x in range(len(test_map[0])):
            assert test_map[y][x].position_x == x
            assert test_map[y][x].position_y == y
            if (y,x) not in [(0,0),(2,2),(2,3),(3,3),(3,2),(4,5)]:
                assert test_map[y][x].type == Cell.OTHER
            elif (y,x) in [(0,0)]:
                assert test_map[y][x].type == Cell.NEST
            elif (y,x) in [(4,5)]:
                assert test_map[y][x].type == Cell.FOOD
            else:
                assert test_map[y][x].type == Cell.OBSTACLE


def test_create_map_limits():
    '''
    Tests if obstacles or food are not allowed to be added if they exceed map limits
    '''
    test_map = create_empty_map((2,2))
    add_food((1,1),test_map)
    add_obstacle((1,1),test_map)
    try:
        add_food((1,1),test_map,(2,2))
    except ValueError:
        assert True
    else:
        assert not True
    try:
        add_obstacle((1,1),test_map,(2,2))
    except ValueError:
        assert True
    else:
        assert not True
    

def test_create_ant():
    '''
    Tests if ants are created only when given coordinates are within map limits
    '''
    test_map = create_empty_map((2,2))
    add_nest((1,1),test_map)
    all_ants = set()
    all_ants = create_ant(test_map,(1,1),all_ants)
    for ant in all_ants:
        assert ant.cell.position_x == 1
        assert ant.cell.position_y == 1
    assert len(all_ants) == NBR_OF_ANT_CREATED
    try:
        create_ant(test_map,(2,2),all_ants)
    except ValueError:
        assert True
    else:
        assert not True


def test_update():
    test_map = create_empty_map((2,2))
    add_nest((0,1),test_map)
    all_ants = set()
    all_ants = create_ant(test_map,(0,1),all_ants)
    for ant in all_ants:
        ant.move_ant(test_map)
    test_map = update_map(test_map,all_ants)
    assert test_map[0][1].ants == set()
    assert test_map[0][0].ants.union(test_map[1][0].ants.union(test_map[1][1].ants)) == all_ants
    assert test_map[0][1].pheromone == 1


if __name__ == '__main__':

    test_create_map()

    test_create_map_limits()
    
    test_create_ant()

    test_update()