from survival import *
import numpy as np
from seeds import *

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

print(etape_jeu_de_la_vie(seeds["beacon"]))
