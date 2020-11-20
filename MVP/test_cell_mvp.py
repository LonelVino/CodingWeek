from cell_mvp import Cell
from ant_mvp import Ant

if __name__ == '__main__':

    # Test cell creation
    cell1 = Cell(0, 0)
    assert cell1.position_x == 0
    assert cell1.position_y == 0
    assert cell1.type == Cell.OTHER

    # Test type change
    cell1.def_type(Cell.NEST)
    assert cell1.type == Cell.NEST

    # Create ant for testing
    ant1 = Ant(cell1)
    
    # Test add
    cell1.add_ant(ant1)
    assert cell1.ants == {ant1}
    
    # Test update_pheromone
    cell1.update_pheromone()
    a = cell1.pheromone
    assert a == min(max(cell1.INITIAL_PHEROMONE, (1 - cell1.RATIO_EVAPORATION) * cell1.pheromone + sum([ant.pheromone_deposit_amount for ant in cell1.ants if ant.carry_food])),cell1.MAX_PHEROMONE)

    # Test delete
    cell2 = Cell(0,1)
    ant2 = Ant(cell1)
    ant3 = Ant(cell1)
    cell1.add_ant(ant2)
    cell1.add_ant(ant3)
    ant4 = Ant(cell2)
    assert cell1.delete_ant(ant4) == False # Delete an ant that does not exist in cell1
    assert cell1.delete_ant(ant1) == True # Delete an ant that exists

    # Test update_pheromone
    ant2.carry_food = True
    cell1.update_pheromone()
    assert cell1.ants == {ant2,ant3}
    assert cell1.pheromone == min(max(cell1.INITIAL_PHEROMONE, (1 - cell1.RATIO_EVAPORATION) * cell1.pheromone + sum([ant.pheromone_deposit_amount for ant in cell1.ants if ant.carry_food])),cell1.MAX_PHEROMONE)
    a = cell1.pheromone

    # Test have_ant
    assert cell1.have_ant() == True
    cell3 = Cell(0,2)
    assert cell3.have_ant() == False

    # Test update
    ant3.cell = cell1
    ant4.cell = cell1
    cell1.update({ant3,ant4})
    assert cell1.ants == {ant3,ant4}
    assert cell1.pheromone == min(max(cell1.INITIAL_PHEROMONE, (1 - cell1.RATIO_EVAPORATION) * cell1.pheromone + sum([ant.pheromone_deposit_amount for ant in cell1.ants if ant.carry_food])),cell1.MAX_PHEROMONE)