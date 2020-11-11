# Fonctionnalité 3: Configurer un ensemble d'amorces


Nous allons ici permettre au jeu de la vie de s'initialiser avec un large choix d'amorces qui sont les amorces classiques de ce jeu de la vie.

Pour vous donner une idée, vous pouvez par exemple regarder [ici](http://conwaylife.appspot.com/library) ou [ici](http://conwaylife.com/wiki/Category:Patterns).

Dans les fonctionnalités avancées de ce projet, nous pourrions par exemple alimenter un catalogue d'amorces en *scrapant* le deuxième site et en inférant et en générant la forme de l'amorce à partir des informations présentes sur la page ou en analysant une image de l'amorce (ou pattern).
 
Nous n'en sommes pas là mais gardez en tête cette fonctionnalité (que vous pouvez ajouter dans un fichier `to_do.md` de votre dépôt git pour la suite.)

Nous vous laissons libre de choisir comment réaliser cette fonctionnalité. Il est attendu le code **commenté** permettant de réaliser cette fonctionnalité et les **tests associés**. Vous pouvez librement appliquer la méthodologie TDD ou non. 


Nous vous proposons, à titre indicatif, les étapes suivantes.

## Etape 1 : Définir un catalogue d'amorces

Il s'agit ici de définir et d'ajouter à votre projet un catalogue composé d'une dizaine d'amorces. On pourra par exemple mettre dans notre catalogue les amorces présentées dans la page [wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)

+ [`acorn`](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#/media/File:Game_of_life_acorn.svg)
+ [`boat`](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#/media/File:Game_of_life_boat.svg)
+ ...

**<span style='color:blue'>Pour avoir un catalogue le plus riche possible, vous pouvez aussi vous répartir le travail entre vous et vous répartir les différents patterns à créer entre vous. C'est un bel exercice de travail de programmation en groupe et de partage de code avec git. Attention il est cependant nécessaire d'avoir ici une étape de conception commune concernant la manière dont vous allez représenter votre catalogue. </span>**

Pour vous permettre d'avancer sur la suite du projet nous vous fournissons cependant le catalogue minimal ci-dessous que nous avons choisi de modéliser sous la forme d'un dictionnaire python (`dict`).

```PYTHON
seeds = {
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
    "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
}

```

## Etape 2 : Initialiser l'univers du jeu de la vie en permettant de choisir une amorce

Il s'agit ici de mettre en place l'initialisation de l'univers de votre jeu de la vie en prenant en compte la diversité des types d'amorces de votre univers.
Il faudra traiter cette étape avec soin. En effet, selon l'amorce, la taille de votre univers doit respecter certaines contraintes. Il vous est conseillé d'utiliser au maximum le mécanisme de [**gestion d'exceptions**](https://realpython.com/python-exceptions/) pour la mise en oeuvre de cette étape.


## Etape 3 : Mettre à jour son dépôt


Vous venez de terminer une fonctionnalité donc n'oubliez pas d'appliquer les bons mécanismes présentés dans le tutorial `git`.



Ici cette fonctionnalité met fin à un Sprint donc vous devez aussi **<span style='color:blue'>Tagger votre commit </span>** et penser à lancer une couverture de votre code avec `coverage`.


#### <span style="color: #26B260">A ce stade du projet, vous avez atteint le JALON 6 : un premier sprint complet de développement logiciel en groupe </span> 


Maintenant que nous avons notre univers et son initialisation nous pouvons maintenant nous intéresser à la simulation du jeu en elle-même. Il s'agit de la [**Fonctionnalité 4** : Appliquer les régles du jeu de la vie à une cellule - la fonction `survival`](./S2_survival.md) 