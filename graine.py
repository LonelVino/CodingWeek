from generate_universe import *
import numpy as np
import random as rd

def implantation_graine(graine, size_universe):
    # implante la graine dans l'univers avec graine qui est un tableau numpy en deux dimensions et size_universe une liste #
    universe = generate_universe(size_universe)
    colonnes_universe, lignes_universe = size_universe
    colonnes_graine, lignes_graine = np.shape(graine)
    if colonnes_graine > colonnes_universe or lignes_graine > lignes_universe:
        return "Dimensions incompatibles"
    else:
        # On définit deux nombres qui correspondent à l'abscisse et à l'ordonnée de la case en bas à gauche de notre graine #
        abscisse, ordonnée = rd.randint(0, colonnes_universe - 1), rd.randint(0, lignes_universe - 1)
        for colonne in range(colonnes_graine):
            for ligne in range(lignes_graine):
                universe[(ordonnée + ligne) % lignes_universe][(abscisse + colonne) % colonnes_universe] = graine[ligne][colonne]
                # pour connaître les cases de universe qui sont modifiées, on module par le nombre de colonne
                # et le nombre de ligne car on a supposé que le tableau se recourber sur lui-même
    return universe

print(implantation_graine([(0,1),(2,2)], (8,8)))
