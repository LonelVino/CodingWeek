# Functionality Analysis and Development Log

## Idea
Ant Colony Optimisation (ACO) simulation.
## Objective
To allow user to simulate and understand how ants use group intelligence to find the best path in the search for food.
## Basic rules
The simulation is set in a rectangular map with cells.
1. All ants start from the nest. All cells are assigned with the same initial level of pheromone (very little).
2. Ants choose the next cell to travel to according to a probabilistic approach; Higher level of pheromones on the neighbouring cell indicates higher probability. They also memorise their individual paths taken.
3. Upon reaching the food source and picking up food, they travel back to the nest following the same paths as before.
4. On their way back, they will deposit decreasing amounts of pheromones on every cell of their path with respect to the distance travelled.
5. The pheromone trail will start to evaporate as soon as it is deposited. 
6. Once ants deposit food at the nest, they will restart the whole process of finding food again.
7. A few ants are generated from the nest on every generation.
8. Ants can only make one cell move per generation.

## Analysis of Work and Functionalities
### Definition of Minimum Viable Product (MVP)
1. Simulate the ACO with already pre-defined map.
2. Display the animation of the simulation using the pygame module.
### Improvements to be made for Final Product (FP)
3. Add an interactive graphical user interface (GUI).
4. Allow users to choose different parameters (size of map, number of obstacles, number of food cells, number of nest cells, number of ants generated per round etc.) and generate a map randomly.
5. Allow users to draw the map by themselves.
6. Fine-tuning of the rules so that ants can pick up all the food much faster.

## Sprints
### Sprint 1: Build cells as a class
1. Initialisation of attributes: position_x, position_y, ants, type, pheromone  
2. Definition of functions: def_type, add_ant, delete_ant, delete_all_ant, update_pheromone,update, have_ant 
### Sprint 2: Build ants as a class 
3. Initialisation of attributes: cell, history, carry_food
4. Apply rules of ACO simulation to the ants: move_ant
### Sprint 3: Create a map  
5. Creation of a map with nest, food and obstacles 
6. Creation of ants at the nests and update the map for the next move 
### Sprint 4: Simulation of ACO and display of animation
7. Simulation of ACO with one food cell, one nest cell with simulation_MVP.py
8. Display animation in a simple user interface with gui_MVP.py
### Sprint 5: Build a graphical user interface 
9.	Define the different basic widgets in gui_utils.py
10.	Build the graphical interface by using these widgets
### Sprint 6: Improvement to the map
11. Change the map to be a map class so that the information is stored as an entity, with the initialisation of attributes (whether generated randomly or not) and the adaptation of the functions already written
12. Adapt the other files already written which use the previous map, including adding new parameters in ant
13. Generate a map randomly which allows parameter configuration
### Sprint 7: Allow users to draw the map by themselves
14.	Define the basic draw module in gui_utils.py: CellButton
15.	Create a clickable interface which can change the colour with users' clicks
16.	Store the information from clicks and create a map
### Sprint 8: Fine-tuning of the rules so that ants can pick up all the food much faster
1.	Change the different parameters already defined to find the best configuration
2.	Modify rules and test the modifications (e.g. ants cannot move to a cell that has been previously visited during the last 3 generations; short memory of ants))