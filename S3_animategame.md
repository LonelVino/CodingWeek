# Fonctionnalité 8 : Visualisation et animation du jeu de la vie


Il s'agit ici de mettre en oeuvre l'animation pour tout type d'univers du jeu de la vie en permettant le paramétrage de l'animation.

En particulier, les commentaires de votre fonction d'animation devraient être a peu près identiques à ceux ci-dessous

```PYTHON
"""
:param  tuple (int, int) universe_size: dimensions of the universe
:param seed: (list of lists, np.ndarray) initial starting array
:param seed_position: (tuple (int, int)) coordinates where the top-left corner of the seed array should be pinned
:param cmap: (str) the matplotlib cmap that should be used
:param n_generations: (int) number of universe iterations, defaults to 30
:param interval: (int )time interval between updates (milliseconds), defaults to 300ms
:param save: (bool) whether the animation should be saved, defaults to False
"""
```

Ecrire le code permettant de mettre en oeuvre cette fonctionnalité. 



**N'oubliez pas de mettre à jour votre dépôt local et distant et de tagger votre commit pour marquer la fin du sprint.** et vous pouvez passer à la [**Fonctionnalité 9** : Gestion des paramètres avec argparse](./S4_arguments.md)