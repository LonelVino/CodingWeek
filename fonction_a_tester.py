import numpy as np
from pytest import *

def generate_universe(size):
    lignes, colonnes = size[0], size[1]
    universe = np.zeros((lignes,colonnes))
    return universe

def etape_jeu_de_la_vie(universe):
    lignes_universe, colonnes_universe = np.shape(universe)
    nouveau_univers = np.zeros((lignes_universe, colonnes_universe))
    for ligne in range(lignes_universe):
        for colonne in range(colonnes_universe):
            if traitement_cellule(ligne, colonne, universe) == True:
                nouveau_univers[ligne][colonne] = 1
            else:
                nouveau_univers[ligne][colonne] = 0
    return nouveau_univers

def traitement_cellule(ligne_cellule, colonne_cellule, universe):
    lignes_universe, colonnes_universe = np.shape(universe)
    Liste_voisins = [(ligne_cellule - 1, colonne_cellule), (ligne_cellule - 1, colonne_cellule + 1), (ligne_cellule - 1, colonne_cellule - 1), (ligne_cellule, colonne_cellule + 1), (ligne_cellule, colonne_cellule - 1), (ligne_cellule + 1, colonne_cellule + 1), (ligne_cellule + 1, colonne_cellule), (ligne_cellule + 1, colonne_cellule - 1)]
    # On suppose ici que l'univers à une taille supérieure à 3*3 #
    Nb_cellules_vivantes = 0
    # Compte le nombre de cellules vivantes autour de notre cellule #
    for voisin in Liste_voisins:
        if universe[voisin[0]%lignes_universe][voisin[1]%colonnes_universe] != 0:
            # Les modulos permettent de respecter le fait que le tableau se recourbe sur lui-même #
            Nb_cellules_vivantes += 1
    if Nb_cellules_vivantes == 3:
        return True
    elif Nb_cellules_vivantes != 2 and Nb_cellules_vivantes != 3:
        return False
    else:
        return universe[ligne_cellule][colonne_cellule] == 1

def game_life_simulate(universe, Nb_étapes):
    for i in range(Nb_étapes):
        etape_jeu_de_la_vie(universe)
    return universe

def test_create_seed():
    seed = create_seed(type_seed = "r_pentomino")
    assert seed == [[0, 1, 1], [1, 1, 0], [0, 1, 0]]

def test_add_seed_to_universe():
    seed = create_seed(type_seed = "r_pentomino")
    universe = generate_universe(size=(6,6))
    universe = add_seed_to_universe(seed, universe,x_start=1, y_start=1)
    test_equality = np.array(universe == np.array([[0,0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0],
 [0, 1, 1, 0, 0, 0],
 [0 ,0, 1, 0, 0, 0],
 [0 ,0, 0, 0, 0, 0],
 [0 ,0, 0, 0, 0, 0]],dtype = np.uint8))
    assert test_equality.all()

def test_traitement_cellule():
    assert traitement_cellule(1,1,[[0,0,0,0],[0,1,0,0],[0,0,1,1],[0,1,1,1]]) == [[0,0,0,0],[0,0,1,0],[0,0,0,1],[1,1,0,1]]

def test_etape_jeu_de_la_vie():
    assert etape_jeu_de_la_vie([[0,0,1],[1,1,0],[0,0,1]]) == [[0,0,1],[1,1,0],[0,0,1]]

def test_generate_universe():
    assert generate_universe((4,4)) == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def test_simulation():
    assert ([[0,0,1],[1,1,0],[0,0,0]],3) == [[0,0,0],[0,0,0],[0,0,0]]
