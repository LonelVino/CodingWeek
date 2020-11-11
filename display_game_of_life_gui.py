from tkinter import *
import numpy as np
from survival import *
from seeds import *
import time
from implantation_graine import *

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

def interface_graphique_etape(universe):
    root = Tk()

    Nb_lignes_universe, Nb_colonnes_universe = np.shape(universe)
    Largeur, Hauteur = 600 / Nb_lignes_universe, 600 / Nb_colonnes_universe

    tableau1 = list(range(Nb_lignes_universe))
    tableau2 = list(range(Nb_lignes_universe))

    for Numéro_ligne in range(Nb_lignes_universe):
        tableau1[Numéro_ligne] = list(range(Nb_colonnes_universe))
        tableau2[Numéro_ligne] = list(range(Nb_colonnes_universe))

        for Numéro_colonne in range(Nb_colonnes_universe):
            tableau1[Numéro_ligne][Numéro_colonne] = Canvas(root, height=Hauteur, width=Largeur)
            # Création d'un canevas mis dans un tableau aux indices Numéro_ligne, Numéro_colonne

            tableau1[Numéro_ligne][Numéro_colonne].grid(row=Numéro_ligne, column=Numéro_colonne)
            # Création de la case Numéro_ligne, Numéro_colonne de la grille dans laquelle on y met le canevas précédent

            if universe[Numéro_ligne][Numéro_colonne] != 0:
                tableau2[Numéro_ligne][Numéro_colonne] = tableau1[Numéro_ligne][Numéro_colonne].create_oval(Largeur*(1 - 1/1.5), Hauteur*(1 - 1/1.5), Largeur/1.5, Hauteur/1.5, outline='red', fill='black')
                # Création d'un rond dans le canevas précédent mis dans le tableau  aux indices Numéro_ligne, Numéro_colonne

                tableau1[Numéro_ligne][Numéro_colonne].create_rectangle(Largeur*(1 - 1/1.1), Hauteur*(1 - 1/1.1), Largeur/1.1, Hauteur/1.1)
                # Dessine un rectangle
            else:
                tableau1[Numéro_ligne][Numéro_colonne].create_rectangle(Largeur*(1 - 1/1.1), Hauteur*(1 - 1/1.1), Largeur/1.1, Hauteur/1.1)
                # Dessine un rectangle

    root.mainloop()


def interface_graphique_jeu(universe, n):
    def supprimer(Ligne, Colonne):
        tableau1[Numéro_ligne][Numéro_colonne].delete(tableau2[Ligne][Colonne])
        # Suppression du rond qui se trouve dans le tableau 2

    def creer(Ligne, Colonne):
        tableau1[Numéro_ligne][Numéro_colonne].delete(tableau2[Ligne][Colonne])
        tableau1[Numéro_ligne][Numéro_colonne].create_rectangle(Largeur_carreau*(1 - 1/1.1), Hauteur_carreau*(1 - 1/1.1), Largeur_carreau/1.1, Hauteur_carreau/1.1)
        tableau2[Numéro_ligne][Numéro_colonne] = tableau1[Numéro_ligne][Numéro_colonne].create_oval(Largeur_carreau*(1 - 1/1.5), Hauteur_carreau*(1 - 1/1.5), Largeur_carreau/1.5, Hauteur_carreau/1.5, outline='black', fill='red')
        # Création d'un rond dans le tableau 2

    nouveau_univers = universe

    root = Tk()

    Nb_lignes_universe, Nb_colonnes_universe = np.shape(universe)
    Largeur_carreau, Hauteur_carreau = 600 / Nb_lignes_universe, 600 / Nb_colonnes_universe

    tableau1 = list(range(Nb_lignes_universe))
    tableau2 = list(range(Nb_lignes_universe))

    for Numéro_ligne in range(Nb_lignes_universe):
            tableau1[Numéro_ligne] = list(range(Nb_colonnes_universe))
            tableau2[Numéro_ligne] = list(range(Nb_colonnes_universe))

            for Numéro_colonne in range(Nb_colonnes_universe):
                tableau1[Numéro_ligne][Numéro_colonne] = Canvas(root, height=Hauteur_carreau, width=Largeur_carreau)
                # Création d'un canevas mis dans un tableau aux indices Numéro_ligne, Numéro_colonne

                tableau1[Numéro_ligne][Numéro_colonne].grid(row=Numéro_ligne, column=Numéro_colonne)
                # Création de la case Numéro_ligne, Numéro_colonne de la grille dans laquelle on y met le canevas précédent

                if universe[Numéro_ligne][Numéro_colonne] != 0:
                    tableau2[Numéro_ligne][Numéro_colonne] = tableau1[Numéro_ligne][Numéro_colonne].create_oval(Largeur_carreau*(1 - 1/1.5), Hauteur_carreau*(1 - 1/1.5), Largeur_carreau/1.5, Hauteur_carreau/1.5, outline='black', fill='red')
                    # Création d'un rond dans le canevas précédent mis dans le tableau  aux indices Numéro_ligne, Numéro_colonne

                    tableau1[Numéro_ligne][Numéro_colonne].create_rectangle(Largeur_carreau*(1 - 1/1.1), Hauteur_carreau*(1 - 1/1.1), Largeur_carreau/1.1, Hauteur_carreau/1.1)
                    # Dessine un rectangle
                else:
                    tableau1[Numéro_ligne][Numéro_colonne].create_rectangle(Largeur_carreau*(1 - 1/1.1), Hauteur_carreau*(1 - 1/1.1), Largeur_carreau/1.1, Hauteur_carreau/1.1)
                    # Dessine un rectangle
    root.update()
    for i in range(n):
        univers, nouveau_univers = nouveau_univers, etape_jeu_de_la_vie(nouveau_univers)
        for Numéro_ligne in range(Nb_lignes_universe):
            for Numéro_colonne in range(Nb_colonnes_universe):
                if univers[Numéro_ligne][Numéro_colonne] != nouveau_univers[Numéro_ligne][Numéro_colonne]:
                    # On regarde les points qui vont être modifiés entre deux étapes
                    if nouveau_univers[Numéro_ligne][Numéro_colonne] == 1:
                    # Si dans la case on a un 1, alors il faut dessiner un rond
                        time.sleep(0.005)
                        creer(Numéro_ligne, Numéro_colonne)
                        # On utilise la fonction time.sleep() dans le but de pouvoir voir les modifications entre chaque étape
                        # On utilise creer afin de dessiner un rond
                    else:
                    # Si on a un 0 dans notre case, on souhaite supprimer le rond qui était présent à l'état précédent
                        time.sleep(0.005)
                        supprimer(Numéro_ligne, Numéro_colonne)
                        # De même, la fonction supprimer permet de supprimer un rond dans les cases concernées
        root.update()
        # On met à jour pour voir les changements sur notre interface
    root.mainloop()


univers = implantation_graine((12,12), seeds['block_switch_engine'], (2,2))
interface_graphique_jeu(univers, 70)



