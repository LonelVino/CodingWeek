from generate_universe import *
import numpy as np
from seeds import *

def implantation_graine(size_universe, graine, seed_position):
    # implante la graine dans l'univers avec graine qui est un tableau numpy en deux dimensions et size_universe une liste #
    universe = generate_universe(size_universe)
    lignes_universe,colonnes_universe = size_universe
    lignes_graine, colonnes_graine = np.shape(graine)
    if colonnes_graine > colonnes_universe or lignes_graine > lignes_universe:
        return "Dimensions incompatibles"
    else:
        for ligne in range(lignes_graine):
            for colonne in range(colonnes_graine):
                universe[(seed_position[0] + ligne) % lignes_universe][(seed_position[1] + colonne) % colonnes_universe] = graine[ligne][colonne]
                # pour connaître les cases de universe qui sont modifiées, on module par le nombre de colonne
                # et le nombre de ligne car on a supposé que le tableau se recourber sur lui-même
    return universe

# On a réutilisé la fonction graine avec un changement qui est la position de l'emplacement du bord haut gauche de la graine dans l'univers #


