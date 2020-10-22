# Jeu de la vie - Sprint 0 : Reflexion autour de la conception

Après cette phase d'analyse, nous pouvons avoir une première démarche de conception et essayer d'identifier les principaux objets de notre MVP. 

En lisant la [description du jeu de la vie sur Wikipedia](https://fr.wikipedia.org/wiki/Jeu_de_la_vie), on identifie notamment un certain nombre de concept comme ceux de **grille**, **univers**, **cellule**, **état**, **amorce** ainsi que tous les concepts faisant référence aux différentes structures. 


## Vers un langage commun

Dans cette phase de reflexion sur la conception, pour favoriser le travail collaboratif et une compréhension commune entre tous les membres du projet, il est important de définir, dès le début du projet, un **vocabulaire commun** autour des termes métier. Dans le jargon du developpement de logiciel, on parle de [**ubiquitous language**](http://referentiel.institut-agile.fr/ubiquitous.html) ou **langage omniprésent**. C'est un principe issu de l'approche *Domain Driven Design* décrite dans l'[ouvrage](https://github.com/p0w34007/ebooks/blob/master/Eric%20Evans%202003%20-%20Domain-Driven%20Design%20-%20Tackling%20Complexity%20in%20the%20Heart%20of%20Software.pdf) du même nom et qui consiste à identifier et à définir un langage commun autour des termes métiers.


Dans le cas du jeu de la vie, c'est un travail qui peut vous sembler fastidieux et très certainement inutile mais qui vous sera très utile pour de nombreux autres projets, impliquant différents acteurs.

Le déroulé de cette approche consiste à produire ce que l'on appelle des [**User Stories**](https://en.wikipedia.org/wiki/User_story) (avec l'ensemble des parties prenantes du projet) qui représentent les besoins des utilisateurs à implémenter. Ce travail permet aussi de définir le langage partagé.

Une **user story** ce n'est rien d'autre qu'une phrase simple, en language naturel, qui permet de décrire le contenu d'une fonctionnalité à développer en précisant le *Qui?*, le *Quoi?* et le *Pourquoi?*

 `En tant que <qui>, je veux <quoi> afin de <pourquoi>`

Ici, typiquement : 

+ En tant qu'utilisateur de l'application , je veux pouvoir **paramétrer la simulation** du jeu de la vie
+ En tant qu'utilisateur de l'application, je veux pouvoir **être alerté** lors de la reconnaissance d'une structure.
+ En tant qu'enseignant, je veux pouvoir **générer, paramétrer et sauvegarder des animations** d'instances du jeu de la vie.
+ ...


Concernant le langage partagé, dans le cas du jeu de la vie, plusieurs termes sont utilisés pour parler de la grille du jeu par exemple :, *grille*, *univers*, *tableau*...

Il est donc nécessaire de choisir un terme précis pour chaque objet de l'application

Pour la suite du projet, on choisit par exemple le nom de **univers** pour désigner la grille du jeu de la vie et que nous définirons comme un conteneur de **cellule** .

Une **cellule** est un élement de l'univers qui peut prendre une valeur comprise entre 0 et 1 selon son **état**, morte ou vivante.

## Les principaux objets, modules de votre application

Cette phase d'analyse doit aussi vous faire reflechir à la conception de votre application et notamment aux différents objets et modules de cette dernière en essayant de séparer les responsabilités. 

Pour cela, essayez de réflechir à l'architecture fonctionnelle de votre application et à comment les différents acteurs, modules, objets intéragissent entre eux. Faites le avec un papier et un crayon, de manière schématique. Un travail et une reflexion de groupe peut être intéressante ici !

Prenez un peu de temps pour faire ce travail. Une fois terminé, prenez une photo de ce que vous avez mis sur papier et stockez cela dans un répertoire intitulé `WorkingDocs`de votre dépôt git. N'oubliez pas de faire un `commit` et de mettre à jour votre dépôt distant.

 
L'objectif de ce travail est de vous permettre de modéliser, du point de vue informatique, votre problème mais il est essentiel aussi pour l'organisation de votre travail, c'est-à-dire, son découpage en différents sprints et fonctionnalités par exemple. 

Ici, ce travail a été fait pour vous mais, il faudra le faire pour votre projet de la semaine 2.


Vous pouvez maintenant passer à la [**Fonctionnalité 1** : Représentation de l'univers.](./jeudelavie_S1_Univers.md)