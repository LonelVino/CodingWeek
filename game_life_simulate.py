from generation import *

def game_life_simulate(universe, Nb_étapes):
    for i in range(Nb_étapes):
        etape_jeu_de_la_vie(universe)
    return universe

