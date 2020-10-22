# Fonctionnalité 8 : Affichage de la grille de jeu dans une fenêtre Tkinter


Il s'agit ici de mettre en place votre interface Tkinter pour l'affichage du jeu de la vie. On travaillera dans un premier temps sur le module `display_game_of_life_gui`


## Etape 1 : Création de la structure Tkinter pour afficher l'univers de jeu.

L'étape 1 consiste en l'affichage de la grille de jeu initiale en Tkinter. Dans cette étape, on s'intéressera uniquement à l'affichage de la grille. 


Pour cette étape, il est nécessaire de :

 + Definir avec quel type d'objets widgets notre grille sera représentée.
 + Definir un certain nombre de constantes qui serviront à l'affichage de la grille comme par exemple les couleurs des différentes cellules en fonction de leur valeur, les couleurs des valeurs elle-mêmes, la taille de la fenêtre principale.


### Choix de représentation de la grille de jeu en Tkinter

Pour l'affichage de notre grille de jeu avec Tkinter, nous allons utiliser le widget `Toplevel` qui permet de créer des fenêtres primaires, c'est-à-dire des fenêtres qui possèdent une existence indépendante pour le gestionnaire de fenêtre du système d’exploitation.

Une bonne explication de ce type de widget est disponible [ici](http://tkinter.fdex.eu/doc/toplww.html).


+ Créer une fenêtre principale avec Tkinter, intitulée gameoflife et créer un widget `Toplevel`, intitulé gameoflife que vous associerez à votre fenêtre principale.
+ Placer ce widget à l'aide de la fonction de placement `grid()` de Tkinter.

###  Representation de l'univers de cellules


Nous allons maintenant créer et afficher l'univers lui-même.

+ Initialiser un univers de jeu.
+ Regarder le widget [`Canvas`](http://tkinter.fdex.eu/doc/caw.html) pour l'affichage de l'univers du jeu.





Nous avons donc à ce stade deux objets  :
+ `grid_game` qui contient les données du jeu, donc les données à afficher (le **MODELE**).
+ `graphical_grid`, notre structure de données Tkinter qui contient la présentation de l'interface graphique (la **VUE**).

Cette manière de procéder est très classique en développement d'interfaces graphiques. Elle correspond à un motif d'architecture logicielle appelé [**Modèle-vue-contrôleur ou MVC**](https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur) dédié aux interfaces graphiques, datant de 1978 et devenu très populaire. Ce motif est composé de trois types de modules ayant trois responsabilités différentes : les modèles, les vues et les contrôleurs :

 + Un **modèle (Model)** qui  contient les données à afficher.
+ Une **vue (View)** qui contient la présentation de l'interface graphique.
+ Un **contrôleur (Controller)** qui contient la logique concernant les actions effectuées par l'utilisateur.

Nous avons donc pour l'instant respecté ce principe avec au moins les deux premiers modules. Il nous faut cependant encore connecter la vue au modèle et c'est ce que nous allons faire tout de suite.

###  Affichage de la simulation.

Il s'agit maintenant d'afficher sur votre interface l'évolution de votre univers.

Pour cela, il faut configurer vos cellules en mettant à jour les paramètres de vos différents objets graphiqus avec les valeurs correspondantes dans la grille elle-même

Avant d'écrire votre code, il est nécéssaire de prendre un peu de temps pour réflechir à la conception. Le type de question qu'il faut vous poser est le nombre de fois que cette opération de mise à jour de la vue peut se produire dans le déroulé du jeu. Une fois ? Plusieurs fois ? A chaque tour de jeu ?

En fonction de votre réponse, il peut donc être utile de mettre le code correspondant à cette tâche dans une fonction, par exemple appelée `display_and_update_graphical_gameoflife()` que vous pourrez appeler dès que nécessaire.



## Etape 3 : Simuler !
A ce stade du projet, vous devriez déjà pouvoir simuer le jeu de la vie via votre interface graphique. Prenez le temps de le faire et n'oubliez pas de lister les fonctionnalités qui vous semblent manquantes.



Nous avons maintenant terminé cette fonctionnalité, il vous faut :

+ <span style='color:blue'>Faire un commit</span> 
+ <span style='color:blue'>Pousser (Push) votre code vers votre dépôt distant sur GitLab.</span> 



Nous pouvons maintenant ajouter des moyens graphiques de configurer le jeu. Il s'agit de la [**Fonctionnalité 13** : Permettre la configuration du jeu via l'interface graphique](./config.md)









