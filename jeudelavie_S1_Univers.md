# Fonctionnalité 1 : Représentation de l'univers avec une graine positionnée aléatoirement

L'objectif de cette première fonctionnalité est de pouvoir **représenter l'univers du jeu de la vie**. Il s'agira donc de :

+ Demander à l'utilisateur de saisir la taille du jeu.
+ De générer l'univers associé contenant que des cellules mortes.


Nous allons ici nous familiariser avec l'approche de développement [**TDD (Test Driven Development)**](https://fr.wikipedia.org/wiki/Test_driven_development) qui consiste à spécifier le comportement attendu via un test avant de l’implémenter effectivement. Le principe est donc d'écrire en premier lieu le test et ensuite le code le plus simple possible qui permette au test de passer et donc de satisfaire le comportement spécifié. Le code peut ensuite être amélioré. L'idée est donc de se focaliser sur les fonctionnalités plutôt que sur le code.

Nous allons d'abord travailler pas à pas puis vous prendrez au fur et à mesure de l'autonomie sur cette approche. 

## Créer un univers

Pour créer l'univers, il faut identifier les données qu'il faudra manipuler, c'est-à-dire les données nécéssaires pour représenter cet univers, qui est un conteneur de cellules qui ne peuvent être que dans deux états. Puis, il s'agira ensuite de choisir les structures de données à utiliser.

 1. **Critères d'acceptance.**

 Un des premières tâches à faire ici est de rechercher et de lister l'ensemble des critères qui permettront de répondre correctement aux besoins que la fonctionnalité *Créer un univers* est sensée couvrir. Ces critères sont des **critères d'acceptance**. Ici, c'est très simple, le critère d'acceptance de *Créer un univers* est d'**avoir un univers du jeu de la vie avec toutes les cellules mortes**.
 
 
 
 
 2. **Developpement en mode TDD**

 Le **TDD (Test Driven Development)** est un développement dirigé par les tests et donc la première ligne de votre programme doit être dans un fichier de tests. Dans notre cas, nous utiliserons le module [`pytest`](https://docs.pytest.org/en/latest/) qu'il faut donc ajouter à votre projet. Le principe du TDD repose sur 3 étapes complémentaires.
 
   + Première étape (**<span style='color:red'>RED</span>**) : Ecrire un premier test qui échoue.
   + Deuxième étape (**<span style='color:green'>GREEN</span>**) : Ecrire le code le plus simple qui permet de passer le code.
   + Troisième étape (**REFACTOR**) : Améliorer le code source.


Nous allons donc appliquer cette méthode à la fonctionnalité de la création de l'univers du jeu de la vie.

#### **<span style='color:red'> ETAPE RED</span>**

Notre premier test va consister à tester que étant donnée une taille voulue, notre jeu de la vie dispose bien d'un univers de jeu constitué de cellules mortes.

```PYTHON
from generate_universe import *
from pytest import *


def test_generate_universe():
    assert generate_universe((4,4)) == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
```

Recopier ce code dans un fichier `test_generate_universe.py`
Ce test doit échouer, puisqu'en l'état actuel du projet, le code pour la fonction et même le module `generate_universe` n'existe pas et on a donc l'erreur suivante lors de l'exécution du code <span style='color:red'>`ImportError: cannot import name 'generate_universe'`<span>

#### **<span style='color:green'> ETAPE GREEN</span>**

On va maintenant écrire le code qui permet de faire passer ce test le plus rapidement possible.

Il suffit pour cela de :

 + Créer le fichier `generate_universe.py` dans le projet.
 + Créer et compléter une fonction `generate_universe` dans le fichier `generate_universe.py` de telle manière que le test précédent passe.

 On pourra par exemple, définir la fonction ci-dessous dans le fichier `generate_universe.py`
 
```PYTHON
def generate_universe(size):
    s = []
    for i in range(0,size[0]):
        p = []
        for j in range(0,size[1]):
            p.append (0)
        s.append(p)
    return s
```
 
 Votre test devrait passer au vert avec cette étape **<span style='color:green'> ETAPE GREEN</span>**
 

#### **<span style='color:black'> ETAPE REFACTOR</span>**
   
La dernière étape consiste en une étape de [refactoring](https://refactoring.com/), à mettre en place si nécessaire.   

Le [refactoring](https://en.wikipedia.org/wiki/Code_refactoring)(ou réusinage de code) est un principe de programmation qui consiste à changer la structure interne d’un logiciel sans en changer son comportement observable. C'est une étape qui doit toujours être exécutée quand les différents tests sont au vert et qui n'est pas obligatoire. Elle doit surtout permettre d'améliorer la **qualité du code** par exemple en améliorant :
 
 + **la conception** : decoupage en fonctions, modules ou classes afin de rendre votre code le plus simple possible.
 + **la lisibilité du code** : il faut ici prendre le temps d'appliquer les principes du [clean code](https://cleancoders.com/cart) introduit par Robert C. Martin dans l'ouvrage du même nom et dont un des principe est celui des boy-scouts (*« The Boy Scout Rule »*): *« Toujours laisser un endroit dans un état meilleur que celui où vous l’avez trouvé »*.
 
Dans notre cas, une des premiers principes est de vérifier du bon nommage (variables, fonctions, packages, classes et cie) et de la présence de commentaires dans notre code. 
 
 Vous trouverez [ici](https://github.com/zedr/clean-code-python#objects-and-data-structures) quelques principes du clean code transposé au langage python. Prenez le temps de lire rapidement ce site et appliquer ces différents principes au code que vous allez écrire.
 
Dans cette étape **<span style='color:black'> ETAPE REFACTOR</span>**, on peut aussi travailler à l'optimisation des performances du programme si cela s'avère vraiment nécessaire.
 
 
Dans notre cas, on peut par exemple procéder à une étape de renommage sur la variable `s`. En effet, il peut par exemple être plus explicite de nommer cette variable `universe`. Pour réaliser cette étape de renommage, il est fortement conseillé d'utiliser les fonctionnalités de Refactoring de votre IDE. En effet, ici cela ne vous semble peut être pas très utile mais avec un code plus complexe, ce sera très utile. Avec PyCharm Edu, il vous suffit de selectionner la variable à renommer et à acceder au menu **Refactor** par un clic droit (ou par MAJ F6) et d'acceder à la fonctionnalité **Rename** pour saisir le nouveau nom `universe`. Toutes les variables `s` de la fonction `generate_universe` seront alors simultanément renommer en `universe`.


On peut aussi ici se poser la question du choix de la structure de données utilisée pour représenter notre univers. Nous allons faire des calculs numériques sur cet univers et il semble peut être intéressant d'utiliser la structure d'array `numpy` pour représenter cet univers. 

Nous allons donc ajouter la bibliothèque  `numpy` à notre projet via PyCharmEdu ou avec la commande `pip3 install numpy` et nous allons donc modifier notre code (et les tests associés) pour représenter l'univers par un array `numpy`.

**Faites ce travail de refactoring**. 





#### **ATTENTION**

1. **Après cette étape, n'oubliez pas de relancer les tests pour vérifier que le comportement de votre code n'a pas changé et que tout est encore bien AU VERT !**

2. On vient ici de terminer la réalisation de l'étape *Créer l'univers*, il convient donc de **committer ce changement dans votre gestionnaire de version avec un message de commit explicite reprenant l'objectif de l'étape**. Pensez aussi à mettre à jour votre dépôt distant.


#### **A VOUS de JOUER!**

Vous allez maintenant procéder par itérations pour terminer l'écriture la  fonctionnalité *Représentation de l'univers avec une graine positionné aléatoirement*  dont on rappelle le critère d'acceptance : **avoir un univers avec une graine (ou amorce) (par exemple celle ci : `"r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]]`) aléatoirement placée dans l'univers**.

Chaque itération commence par un test qui échoue mais qui est écrit uniquement s'il apporte un nouveau comportement au système. A la fin de chaque itération, il faut donc se poser la question du prochain test à écrire. Dans notre cas, nous n'avons pas encore traiter l'ajout de la graine dans notre univers et le prochain test à écrire peut donc concerner la création de cet amorce et son ajout dans l'univers.

##### Créer une amorce de type `r_pentomino` et positionnée la aléatoirement dans l'univers


 1. **Critères d'acceptance.**

 + Une amorce est crée.
 + Cette amorce est placée aléatoirement dans l'univers du jeu de la vie.

 
 2. **Developpement en mode TDD**

En appliquant le principe du TDD décrit précédemment, vous allez donc écrire le code pour terminer l'écriture de cette fonctionnalité.
En particulier, il est conseillé d'itérer sur les tests décrits ci-dessous. Ces différents tests correspondant à chaque itération à l'étape **<span style='color:red'> ETAPE RED</span>**. Il vous est demandé de faire les deux autres étapes du cycle TDD pour passer ces tests en vert et améliorer la qualité de votre code.

+ **Itération 1 - Test : Une amorce de type `r_pentomino` est créée** 

``` PYTHON
def test_create_seed():
    seed=create_seed(type_seed = "r_pentomino")
    assert seed==[[0, 1, 1], [1, 1, 0], [0, 1, 0]]
```



+ **Itération 2 - Test : L'amorce est placée aléatoirement dans la grille de jeu**. 


```PYTHON
def test_add_seed_to_universe():
    seed = create_seed(type_seed = "r_pentomino")
    universe = generate_universe(size=(6,6))
    universe = add_seed_to_universe(seed, universe,x_start=1, y_start=1)
    test_equality=np.array(universe ==np.array([[0,0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0],
 [0, 1, 1, 0, 0, 0],
 [0 ,0, 1, 0, 0, 0],
 [0 ,0, 0, 0, 0, 0],
 [0 ,0, 0, 0, 0, 0]],dtype=np.uint8))
    assert test_equality.all()
```


A la fin de ces 2 itérations, vous avez normalement écrit l'ensemble du code nécéssaire à la réalisation de la fonctionnalité 1 : **Représentation de l'univers avec une graine positionnée aléatoirement.**

**<span style='color:blue'>Commiter maintenant vos changements dans votre gestionnaire de version</span>**


## A propos de la couverture de code par vos tests

Une couverture de code par les tests (code coverage) nous permet de connaître le pourcentage de notre code qui est testé et donc cela permet d'avoir une idée de ce qui reste d'ombre dans notre projet.

En règle générale, on considère qu'une couverture de code supérieure à 80% est signe d'un projet bien testé et auquel il sera alors plus facile de rajouter de nouvelles fonctionnalités.

Pour connaitre le taux de couverture de notre projet, nous pouvons utiliser des bibliothèques python [`coverage`] et [`pytest_cov`] qu'il faut donc installer soit en ligne de commande soit depuis votre IDE.

`pip3 install coverage`

`pip3 install pytest-cov`

Il faut ensuite vous placer dans le répertoire de votre projet et lancer la commande suivante :

`pytest --cov=game_of_life --cov-report html test_*.py`

Cette commande permet de tester les fichiers contenus dans le dossier 'game_of_life', crée un rapport en html et le place dans le répertoire `htmlcov` et utilise les tests qui sont dans ce répertoire et qui sont de la forme `test_[caracteres].py`.

L'ouverture du fichier `index.html`dans le répertoire `htmlcov`vous permet de visualiser un bilan du test de couverture qui devrait être bon dans la mesure où nous avons utilisé l'approche TDD. Un clic sur chacun des fichiers permet aussi d'avoir un bilan propre à chaque fichier.

![testcoverage](./Images/coverage.png)



![testcoverage](./Images/coveragebis.png)


## A propos de la gestion des versions

<span style='color:blue'> Pour toute la suite du projet, il vous est demandé de :</span> 

+ <span style='color:blue'>Faire un commit dès que la réalisation d'une fonctionnalité ou d'une sous-fonctionnalité est finie.</span> 
+ <span style='color:blue'>Tagger à la fin de chaque journée votre dernier commit </span> 
+ <span style='color:blue'>Pousser (Push) votre code vers votre dépôt distant sur GitLab.</span> 
+ <span style='color:blue'>Faire un test de couverture de code à la fin de chaque journée et de pousser le bilan obtenu vers votre dépôt distant sur GitLab.</span>



Vous pouvez maintenant passer à la [**Fonctionnalité 2** : Afficher l'univers.](./jeudelavie_S1_Display.md)
 
 
 
    
 




 
 
 
    

