# Programmation du jeu de la vie de Conway

L'**objectif** de ce mini-projet est de developper, de manière très incrémentale, le jeu de la vie de Conway, **un automate cellulaire**, afin de vous former aux bonnes pratiques de la programmation et à la culture de la qualité logicielle. En particulier, au travers de ce projet, vous allez découvrir plusieurs principes du mouvement dit du [*Software Craftmanship*](https://www.octo.com/fr/publications/20-culture-code). 




## A propos du jeu de la vie de Conway

Le [jeu de la vie](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) est un [automate cellulaire](https://en.wikipedia.org/wiki/Cellular_automaton) imaginé par [John Horton Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) au début du 19ème siècle. C'est probablement le plus connu de tous les automates cellulaires qui sont des modèles où chaque état conduit mécaniquement à l'état suivant à partir de règles pré-établies. 


Si vous n'avez jamais entendu parler du jeu de la vie, prenez le temps de lire la [page Wikipédia](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) le décrivant


![jeu de la vie](./Images/Gospers_glider_gun.gif)


### Règles du jeu

Le jeu se déroule sur une **grille** à deux dimensions, théoriquement infinie (mais de longueur et de largeur finies et plus ou moins grandes dans la pratique), dont les cases — qu'on appelle des **cellules**, par analogie avec les cellules vivantes — peuvent prendre deux états distincts : **vivantes** ou  **mortes**. 


À chaque étape, l’évolution d’une cellule est entièrement déterminée par l’état de ses huit voisines de la façon suivante :

+ Une cellule morte possédant exactement trois voisines vivantes devient vivante (elle naît) (**reproduction**).
+ Une cellule vivante possédant deux ou trois voisines vivantes le reste, sinon elle meurt (**stabilité, sur-population et sous-population**)


### Les structures

Des structures, constituées de plusieurs cellules, peuvent apparaître dans l’univers parmi lesquelles :

 + [Les structures stables](https://fr.wikipedia.org/wiki/Structure_stable_(automate_cellulaire)), des ensembles de cellules ayant stoppé toute évolution.
 + [Les structures périodiques, ou oscillateurs](https://fr.wikipedia.org/wiki/Oscillateur_(automate_cellulaire)) qui se transforment de manière cyclique, en revêtant plusieurs formes différentes avant de retrouver leur état initial.
 + [Les vaisseaux](https://fr.wikipedia.org/wiki/Vaisseau_(automate_cellulaire)), des structures capables, après un certain nombre de générations, de produire une copie d’elles-mêmes, mais décalée dans l’univers du jeu.
 + [Les mathusalems](https://fr.wikipedia.org/wiki/Mathusalem_(automate_cellulaire)), des structures actives qui mettent un certain temps avant de se stabiliser
 + Et  bien d'autres, les puffeurs, les canons, les jardins d’Éden...

 
L'objectif de ce projet est de programmer le jeu de la vie en python d'abord très simplement avec les bibliothèques scientifiques de python (`numpy`, `scipy` et `matplolib`), puis en ajoutant ensuite une interface graphique et des modules d'animation.
 
Nous travaillerons sur un tore : il n'y aura pas de bords. Sur notre grille, la première colonne sera voisine de la dernière et la première ligne sera voisine de la dernière.
 
 

## Organisation du mini-projet

Ce mini-projet est découpé en plusieurs objectifs, eux-même découpés en  **sprints** et **fonctionnalités**. La notion de sprint fait référence à la [méthode agile](https://fr.wikipedia.org/wiki/M%C3%A9thode_agile). Un sprint correspond à un intervalle de temps pendant lequel l’équipe projet va compléter un certain nombre de tâches.

Ce travail de découpage a été fait pour vous mais c'est une des premières étapes à faire pour tout projet de developpement logiciel, au moins de manière macroscopique. **Pensez-y la semaine prochaine!**

### **Objectif 1 (MVP): Un jeu de la vie simple, sans interface graphique** 

Le premier objectif est de constuire et d'implémenter une version simple du jeu de la vie que l'on peut qualifier de  **[MVP (Minimum Viable product)](https://medium.com/creative-wallonia-engine/un-mvp-nest-pas-une-version-simplifi%C3%A9e-de-votre-produit-89017ac748b0)**. 

Ce concept de MVP a été popularisé par Eric Ries, l'auteur de [The Lean Startup](http://theleanstartup.com/), une approche spécifique de démarrage d'une activité économique et de lancement d'un produit. La figure ci-dessous permet de bien expliquer ce concept.


![MVP](./Images/mvp.png)

 + **Sprint 0** :
	 + [Installation du socle technique.](./Sprint0Installbis.md)
	 + [Analyse des besoins.](./Sprint0Analyse.md) 
	 + [Refexion autour de la conception.](./Sprint0Conception.md)

 + **Sprint 1 : Mise en place des données du jeu de la vie**
 	+ [**Fonctionnalité 1** : Représentation de l'univers avec une graine positionnée aléatoirement.](./jeudelavie_S1_Univers.md)
 	+ [**Fonctionnalité 2** : Afficher l'univers.](./jeudelavie_S1_Display.md)
 	+ [**Fonctionnalité 3** : Configurer un ensemble d'amorces.](./jeudelavie_S1_Amorces.md)
 		
 + **Sprint 2** : **Simulation du jeu de la vie**
 	+ [**Fonctionnalité 4** : Appliquer les régles du jeu de la vie à une cellule - la fonction `survival`](./S2_survival.md) 
 	+ [**Fonctionnalité 5** : Appliquer les régles du jeu de la vie à toutes les cellules de l'univers sur une génération - la fonction `generation`](./S2_generation.md)
 	+ [**Fonctionnalité 6** : Simuler le jeu de la vie pour un univers donné sur un ensemble d'itérations fixé - la fonction `game_life_simulate`](./S2_simulate.md)
 		
 + **Sprint 3** : **Affichage et génération d'animations avec `matplotlib`**
 	+ [**Fonctionnalité 7** : Une première animation avec `matplotlib`](./S3_simpleanimation.md)
 	+ [**Fonctionnalité 8** : Visualisation et animation du jeu de la vie](./S3_animategame.md)

 + **Sprint 4** : **On joue le jeu de la vie!**

 	+ [**Fonctionnalité 9** : Gestion des paramètres avec argparse](./S4_arguments.md)
 	+ [**Fonctionnalité 10** : On met tout cela dans un programme principal](./S4_gamemain.md)
 	

### Objectif 2 : Un jeu de la vie avec une interface graphique (Amélioration du MVP) 
 	
 + **Sprint 5** : **Montée en compétences : les interfaces graphiques en python**

 	+ [**Fonctionnalité 11** : Premiers pas en Tkinter](S5_GUI_Tutorial.md)

+ **Sprint 6** : **Creation de l'interface pour l'univers**

	+ [**Fonctionnalité 12**: Affichage de l'univers dans une fenêtre Tkinter](./univers.md)
	+ [**Fonctionnalité 13** : Permettre la configuration du jeu via l'interface graphique](./config.md)
 	
 	
### Objectif 3 : Un jeu de la vie avec pygame 

Il s'agit ici d'utiliser l'utilitaire `pygame` pour simuler le jeu de la vie. Pour cet objectif, nous allons procéder un peu différemment. Nous allons chercher une implémentation existante du jeu de la vie en `pygame`. Vous pouvez par exemple prendre et regarder [cette implémentation du jeu de la vie](https://gist.github.com/bennuttall/6952575).

Vous pouvez en profitez pour regarder les commentaires qui sont faits sur ce code.

Vous pouvez le récupérer et le tester. Il est possible qu'il ne marche pas du premier coup. C'est un bon travail d'essayer de faire fonctionner un code existant. Prenez le temps de comprendre ce qui pose problème et modifiez le code de telle sorte à le rendre fonctionnel. 

Essayer maintenant de le comprendre. Vous pourrez pour cela regader ce [tutoriel sur Pygame](https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/).

Vous êtes prêts maintenant à écrire votre propre version du jeu de la vie en pygame. A vous de jouer ! Il faudra bien sûr pour cela appliquer les mêmes méthodologies que pour l'objectif 1 et l'objectif 2. Avant de vous lancer, il faudra donc découper votre travail en sprints. Un document décrivant votre découpage devra d'ailleurs être déposé sur l'espace Gitlab de votre projet.


### Objectif 4 : Nouvelles améliorations

A ce stage du projet, les objectifs sont complétement atteints et il convient alors de refaire un cycle de conception après avoir eu des retours utilisateurs.
Plusieurs fonctionnalités pourraient être ajoutées comme : 

+ L'enrichissement automatique du catalogue de manière automatique par analyse d'images. Si cet objectif vous intéresse, vous pouvez par exemple suivre le tutorial du groupe **Reconnaissance visuelle** qui se trouve [ici](https://gitlab-cw7.centralesupelec.fr/celine.hudelot/cs_codingweek_facerecognition_2020/-/blob/master/Facerecognition_S1_displayimage.md)
+ L'ajout de nouvelles règles de simulation
+ ...

Ici aussi votre travail se fera en appliquant les mêmes méthodologies que pour l'objectif 1 et l'objectif 2. Avant de vous lancer, il faudra donc découper votre travail en sprints. Un document décrivant votre découpage devra d'ailleurs être déposé sur l'espace Gitlab de votre projet.














