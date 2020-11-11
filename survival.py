import numpy as np
from seeds import *

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

