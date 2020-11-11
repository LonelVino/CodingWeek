from animation_paramétrée import *
from seeds import *

def main():
    universe_size = (int(input('Entrez le nombre de lignes de notre univers')), int(input('Entrez le nombre de colonnes de notre univers')))
    nom_graine = input('Entrez le nom de la graine parmi les noms du catalogue seeds')
    seed_position = (int(input('Entrez le numéro de la ligne de la case en haut à gauche de la graine')), int(input('Entrez le numéro de la colonne de la case en haut à gauche de la graine')))
    cmap = input('Entrez la couleur')
    n_generations = input('Entrez le nombre itérations')
    interval = int(input('Entrez le temps entre deux itérations'))
    save = bool(input('Entrez si animation doit être sauvegardée'))
    animation_paramétrée(universe_size, seeds[nom_graine], seed_position, cmap, n_generations, interval, save)

if __name__ == '__main__':
    main()
