from cell import Cell
from map import Map
from ant import Ant


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
    return Map((6,7),random_create=False,nest_coordinates=[(0,0)],food_coordinates=[(4,5)],obstacle_coordinates=[(2,2)],obstacle_sizes=[(2,2)])

def test_create_map():
    '''
    Tests if map is created with each cell of the correct type
    '''
    test_map = create_test_map()
    for y in range(len(test_map.map())):
        for x in range(len(test_map.map()[0])):
            assert test_map.map()[y][x].position_x == x
            assert test_map.map()[y][x].position_y == y
            if (y,x) not in [(0,0),(2,2),(2,3),(3,3),(3,2),(4,5)]:
                assert test_map.map()[y][x].type == Cell.OTHER
            elif (y,x) in [(0,0)]:
                assert test_map.map()[y][x].type == Cell.NEST
            elif (y,x) in [(4,5)]:
                assert test_map.map()[y][x].type == Cell.FOOD
            else:
                assert test_map.map()[y][x].type == Cell.OBSTACLE

def test_create_ant():
    '''
    Tests if ants are created only when given coordinates are within map limits
    '''
    new_map1 = Map((2,2),random_create=False,nest_coordinates=[(1,1)])
    new_map1.initAnts()
    for ant in new_map1.all_ants():
        assert ant.cell.position_x == 1
        assert ant.cell.position_y == 1
    #assert len(test_map1.all_ants()) == Cell.DEFAULT_NBR_OF_ANT_CREATED


def test_update():
    test_map3 = Map((2,2),random_create=False,nest_coordinates=[(0,1)])
    for ant in test_map3.all_ants():
        ant.move_ant(test_map3)
    test_map3.update()
    assert test_map3.map()[0][1].ants == set()
    assert test_map3.map()[0][0].ants.union(test_map3.map()[1][0].ants.union(test_map3.map()[1][1].ants)) == set(test_map3.all_ants())
    assert test_map3.map()[0][1].pheromone == 1


if __name__ == '__main__':

    
    test_create_ant()

    test_update()

    test_create_map()

    print('test_map_final Finished')