from tkinter import *
import numpy as np
from seeds import *
import time

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

def jeu_complet():
    def supprimer(Ligne, Colonne):
        tableau1[Numéro_ligne][Numéro_colonne].delete(tableau2[Ligne][Colonne])
        # Suppression du rond qui se trouve dans le tableau 2

    def creer(Ligne, Colonne):
        tableau1[Numéro_ligne][Numéro_colonne].delete(tableau2[Ligne][Colonne])
        tableau1[Numéro_ligne][Numéro_colonne].create_rectangle(Largeur_carreau*(1 - 1/1.1), Hauteur_carreau*(1 - 1/1.1), Largeur_carreau/1.1, Hauteur_carreau/1.1)
        tableau2[Numéro_ligne][Numéro_colonne] = tableau1[Numéro_ligne][Numéro_colonne].create_oval(Largeur_carreau*(1 - 1/1.5), Hauteur_carreau*(1 - 1/1.5), Largeur_carreau/1.5, Hauteur_carreau/1.5, outline='black', fill='red')
        # Création d'un rond dans le tableau 2

    window = Tk()
    nb_lignes_universe = StringVar()
    lignes = Label(window, text="Entrer le nombre de lignes de votre univers ")
    reponse1 = Entry(window, textvariable=nb_lignes_universe, width=10)
    lignes.pack()
    reponse1.pack()
    nb_colonnes_universe = StringVar()
    colonnes = Label(window, text="Entrer le nombre de colonnes de votre univers ")
    reponse2 = Entry(window, textvariable=nb_colonnes_universe, width=10)
    colonnes.pack()
    reponse2.pack()

    graine = StringVar()
    demande_graine = Label(window, text="Donner le nom de la graine que vous souhaitez implanter ")
    reponse3 = Entry(window, textvariable=graine, width=10)
    demande_graine.pack()
    reponse3.pack()

    Ligne_graine = StringVar()
    ligne_graine = Label(window, text="Entrer la ligne de la case en haut à gauche de votre graine ")
    reponse4 = Entry(window, textvariable=Ligne_graine, width=10)
    ligne_graine.pack()
    reponse4.pack()
    Colonne_graine = StringVar()
    colonne_graine = Label(window, text="Entrer la colonne de la case en haut à gauche de votre graine ")
    reponse5 = Entry(window, textvariable=Colonne_graine, width=10)
    colonne_graine.pack()
    reponse5.pack()

    Nb_etape = StringVar()
    nb_etape = Label(window, text="Entrer le nombre d'étapes souhaitées ")
    reponse6 = Entry(window, textvariable=Nb_etape, width=10)
    nb_etape.pack()
    reponse6.pack()

    Temps = StringVar()
    interval = Label(window, text="Entrer l'intervalle de temps entre deux affichages ")
    reponse7 = Entry(window, textvariable=Temps, width=10)
    interval.pack()
    reponse7.pack()

    bouton_quitter = Button(window, text="Valider", command=window.destroy)
    bouton_quitter.pack()

    window.mainloop()

    nouveau_univers = implantation_graine((int(nb_lignes_universe.get()), int(nb_colonnes_universe.get())), seeds[graine.get()], (int(Ligne_graine.get()), int(Colonne_graine.get())))

    root = Tk()

    Nb_lignes_universe, Nb_colonnes_universe = np.shape(nouveau_univers)
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

                if nouveau_univers[Numéro_ligne][Numéro_colonne] != 0:
                    tableau2[Numéro_ligne][Numéro_colonne] = tableau1[Numéro_ligne][Numéro_colonne].create_oval(Largeur_carreau*(1 - 1/1.5), Hauteur_carreau*(1 - 1/1.5), Largeur_carreau/1.5, Hauteur_carreau/1.5, outline='black', fill='red')
                    # Création d'un rond dans le canevas précédent mis dans le tableau  aux indices Numéro_ligne, Numéro_colonne

                    tableau1[Numéro_ligne][Numéro_colonne].create_rectangle(Largeur_carreau*(1 - 1/1.1), Hauteur_carreau*(1 - 1/1.1), Largeur_carreau/1.1, Hauteur_carreau/1.1)
                    # Dessine un rectangle
                else:
                    tableau1[Numéro_ligne][Numéro_colonne].create_rectangle(Largeur_carreau*(1 - 1/1.1), Hauteur_carreau*(1 - 1/1.1), Largeur_carreau/1.1, Hauteur_carreau/1.1)
                    # Dessine un rectangle
    root.update()
    n = int(Nb_etape.get())
    temps = float(Temps.get())
    for i in range(n):
        univers, nouveau_univers = nouveau_univers, etape_jeu_de_la_vie(nouveau_univers)
        for Numéro_ligne in range(Nb_lignes_universe):
            for Numéro_colonne in range(Nb_colonnes_universe):
                if univers[Numéro_ligne][Numéro_colonne] != nouveau_univers[Numéro_ligne][Numéro_colonne]:
                    # On regarde les points qui vont être modifiés entre deux étapes
                    if nouveau_univers[Numéro_ligne][Numéro_colonne] == 1:
                    # Si dans la case on a un 1, alors il faut dessiner un rond
                        creer(Numéro_ligne, Numéro_colonne)
                        # On utilise la fonction time.sleep() dans le but de pouvoir voir les modifications entre chaque étape
                        # On utilise creer afin de dessiner un rond
                    else:
                    # Si on a un 0 dans notre case, on souhaite supprimer le rond qui était présent à l'état précédent
                        supprimer(Numéro_ligne, Numéro_colonne)
                        # De même, la fonction supprimer permet de supprimer un rond dans les cases concernées
        time.sleep(temps)
        root.update()
        # On met à jour pour voir les changements sur notre interface
    root.mainloop()

jeu_complet()

