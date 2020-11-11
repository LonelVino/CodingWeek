from graine import *
from generate_universe import *
import matplotlib.pyplot as plt

def Affichage_universe(universe):
    size_universe = np.shape(universe)
    colonnes_universe, lignes_universe = size_universe[1], size_universe[1]
    A = np.zeros((lignes_universe,colonnes_universe,3), dtype = 'uint8')
    for lignes in range(lignes_universe):
        for colonnes in range(colonnes_universe):
            if universe[lignes][colonnes] != 0:
                A[lignes][colonnes] = (0, 0, 0) # noir
            else:
                A[lignes][colonnes] = (255, 255, 255) # blanc
    plt.imshow(A)
    plt.show()

Affichage_universe(implantation_graine([(0,1),(1,1)], (8,8)))
