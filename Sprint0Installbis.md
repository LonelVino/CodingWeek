# Jeu de la vie - Sprint 0 : Installation du socle technique


Le premier travail consiste à préparer le socle technique nécessaire au bon developpement du projet. Le projet **gameoflife** sera :

+ Un projet Visual Studio Code 
+ Utilisant [git](https://git-scm.com/) comme gestionnaire de version
+ Qui sera déposé sur le [GitLab pédagogique de CentraleSupélec](https://gitlab-cw1.centralesupelec.fr/).



## Versionner avec git

Comme vous l'avez vu lors du cours SIP et lors du tutorial de début de coding weeks, git est un logiciel de gestion de versions décentralisé. Pour rappel, le tutorial est disponible [ici](https://centralesupelec.edunao.com/pluginfile.php/65396/course/section/4378/cours-1.pdf).

D'autres ressources intéressantes sur git :

+ rapide tutorial [ici](http://rogerdudler.github.io/git-guide/index.fr.html).
+ [http://marklodato.github.io/visual-git-guide/index-en.html](http://marklodato.github.io/visual-git-guide/index-en.html)
+ [https://openclassrooms.com/fr/courses/1233741-gerez-vos-codes-source-avec-git](https://openclassrooms.com/fr/courses/1233741-gerez-vos-codes-source-avec-git)
+ ...




### Mise en place de Git sur le projet **`gameoflife`**

Comme vous devrez apprendre à le faire de manière systématique pour tout travail de développement informatique, vous devez passer le projet **`gameoflife`** sous Git pour pouvoir partager votre code et travailler en collaboration.

### Création de votre dépôt (repository) Gitlab

Pour commencer, vous aller configurer git et gitlab pour pouvoir travailler en binôme sur ce projet. Votre binôme est composée de 2 personnes : **A** et **B**.


#### Consignes pour la personne **A**

Allez sur Gitlab et créez un dépôt (un projet) que vous nommerez game2048.


<img src="./Images/gitlab1.png" alt="drawing" width="500"/>




<img src="./Images/gitlab2.png" alt="drawing" width="500"/>

Ce que nous vous faisons faire ici correspond au workflow de travail proposé dans le tutorial git [ici](https://centralesupelec.edunao.com/pluginfile.php/65396/course/section/4378/cours-1.pdf) (slide 62).


##### Ajout de collaborateurs

Vous allez maintenant ajouter votre binôme, votre enseignant et la responsable (identifiant : @2006hudelotc) comme collaborateur de votre dépôt.

Pour cela, allez sur votre depôt GitLab et choisissez le menu `Settings | Members` dans la fenêtre de gauche. Ajouter votre binôme et votre enseignant comme collaborateur. Votre binôme sera *Maintainer* et vos enseignants seront *Reporter*.


#### Consignes pour les personnes **A** et **B**

Chacun personne va maintenant devoir copier (cloner) ce dépôt sur son ordinateur. 

+ Ouvrez pour cela un terminal (vous pouvez utiliser le [terminal intégré à Visual Studio Code](https://code.visualstudio.com/docs/editor/integrated-terminal) si vous le souhaitez).
+ Vérifiez que git est bien installé en tapant :

 `git --version`

+ Le numéro de version de git devrait apparaître.
+ Placez-vous maintenant dans le dossier (aussi appelé répertoire) où vous voulez créer votre projet (il peut s'agir du bureau, de mes documents, etc) à l'aide de la commande `cd`.
+ Allez sur Gitlab récupérer l'adresse web de votre dépôt.

<img src="./Images/gitlab3.png" alt="drawing" width="500"/>



 + Clonez le dépôt dans votre machine (ne le faites pas dans un dossier où il y a déjà des fichiers...) en tapant dans le répertoire choisi : 

 `git clone l_adresse_de_votre_depot`

Un nouveau dossier devrait apparaître avec votre code inclus dedans.

+ Si vous obtenez l'erreur `Couldn't find ref remote master`, allez sur le Gitlab (dans le navigateur web) et créez un fichier random.

    + Si vous obtenez une erreur de certificat (qui sert à crypter vos échanges entre votre ordinateur et Gitlab), vous avez deux solutions possibles :

	    +  Solution 1: désactiver SSL
    	+  Solution 2: créer une paire de clés SSH (une privée et une publique)

### Solution 1: désactiver SSL


A la place d'utiliser la commande `git clone`, utilisez ces commandes :

```
mkdir gameoflife # attention, aucun dossier "gameoflife" ne doit déjà exister
cd gameoflife
git init
git remote add origin ladresse_du_depot_qui_commence_par_https
git config http.sslVerify false
git pull origin master # cela peut prendre un peu de temps
```

### Solution 2 : créer une paire de clés SSH (une privée et une publique)

<img src="./Images/gitlab4.png" alt="drawing" width="500"/>

Lorsque vous générez la clé, laissez tous les champs vides. Pressez juste "Entrée" à chaque fois.

Vous pouvez ensuite afficher votre clé publique via (attention sur Windows, utilisez le Git bash ou le PowerShell):

 `cat ~/.ssh/id_rsa.pub `
 
 
Copiez-la ensuite dans le grand rectangle.

Vous pouvez maintenant faire vos commits et "pusher" vos versions sur Gitlab.


### Rappel des quelques commandes git utiles

Un mémo des commandes git est disponible [ici](https://centralesupelec.edunao.com/pluginfile.php/65396/course/section/4378/cheatsheet.pdf)

Quelques commandes très utiles :

+ afficher les fichiers qui sont sélectionnés pour être commités et ceux qui ne le sont pas.

```
git status
```

+ afficher les modifications depuis le dernier commit

```
git diff
```
+ ajouter un fichier dans la zone de transit

```
git add my_file_name
```

+ créer un commit à partir des fichiers dans la zone de transit.
 
```
git commit -m "A message that describes the commit" # Il s'agit d'une sauvegarde (d'une version) de votre code. Partager votre code revient à transmettre des commits.
```

+ envoyer vos commits sur le serveur

```
git push origin master 
```

+ récupérer les commits du serveur

```
git pull origin master 
```



## Créer un projet python avec Visual Studio Code : **`gameoflife`**


Nous vous recommandons d'utiliser l'éditeur de code [Visual Studio Code](./VisualStudioCode.md) qui vous a déjà été recommandé lors du cours SIP. Il vous suffit juste d'ouvrir le répertoire local du projet `gameoflife` que vous venez de créer via Gitlab.

A ce stade du projet, vous devriez donc avoir :

+ Un projet gameoflife sur le depôt gitlab distant qui possède une seule branche `master`. Ce projet est vide ou est eventuellement constitué d'un fichier `README.md`.
+ Chaque binôme devrait avoit une copie locale de ce projet sur son ordinateur, ouvert via un éditeur de code.

Dans la suite du projet, vous allez travailler en binôme en mettant en place une approche de type [pair programming](https://fr.wikipedia.org/wiki/Programmation_en_bin%C3%B4me) que l'on pourra implémenter de deux manières :

 + A code, B observe et fait une révue du code puis il y a alternance des rôles.
 + A et B code la même fonctionnalité, chacun sur son poste et pour chaque fonctionnalité une discussion et revue commune de chaque solution est faite pour ariver à une version unifiée.

## Ajouter ou modifier un README au projet.

Pour ce premier travail, on appliquera la méthode 1 : construction d'une solution en commun. Supposons que ce soit A qui code.

Il s'agit ici d'ajouter (ou de modifier), via la projet VS Code un fichier `README.md`qui décrit le projet et son contenu. Vous pouvez vous inspirer de ce [template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) pour avoir une idée de ce que votre README devrait contenir. Pour commencer, vous vous contenterez de donner un titre à votre projet et d'y ajouter une petite description.

Une fois ce fichier créé, il convient alors d'ajouter ce changement au dépôt git local de la personne qui a effectué le travail.
Il faut donc excuter les commandes suivantes (en ligne de commande ou via VS Code qui propose une intégration de git).

```
git add README.md
git commit -m "Add README.md"
```

Il faut maintenant mettre à jour le depôt distant, notamment pour B par la commande

```
git push origin master
```

Vous pouvez observer les changements en inspectant votre dépôt Gitlab distant.

Un dernier travail est de mettre à jour les dépôts locaux, notamment pour B en utilisant la commande

```
git pull
```


## Travailler avec des branches

Il vous sera demandé plusieurs fois le long du projet et des séances de pousser votre code sur le dépôt distant qui constitue donc la version stable et partagée de votre projet et qu'il vous faudra donc très souvent synchroniser avec le dépôt local de chaque binôme.

Une démarche classique en developpement consiste à créer une branche par fonctionnalité et/ou par contributeur et à fusionner ensuite les developpements stables dans la branche `master`.

Nous allons donc procéder comme suit dans la suite du projet.

+ Vous aurez un dépôt distant commun pour le binôme.
+ Chaque membre du binôme construira une branche qui lui sera propre

```
 git checkout -b binome_x # creation et placement sur la branche du binome_x
 git push origin binome_x # copie de la branche binome_x sur le dépôt distant
```

Chaque binôme va maintenant ajouter à son projet local un package `game2048`. Il s'agit juste de créer un dossier dans le projet VS Code `game2048` et de créer dans ce dossier un fichier `__init__.py` vide. Chaque binôme va alors ajouter ce changement sur sa branche sur son dépôt local et mettre a jour le dépôt distant.

Après cette opération, votre dépôt distant devrait donc contenir 3 branches avec une branche `master` qui ne contient qu'un fichier `README.md` et les deux branches `binome`, un répertoire contenant un fichier `__init__.py` vide.

 


 <img src="./Images/gitlab5.png" alt="drawing" width="500"/>


 
 
 Il faut maintenant intégrer les modifications faites sur les branches annexes sur la branche principale ce qui consiste en un `merge request`. Il faut pour cela d'abord vous placer sur la branche principale 
 
  `git checkout master `
  
  Puis, faire l'opération de fusion : 

 `git merge <branch>`
 
Pour ne pas avoir trop de problèmes sur cette opération, il faudra vous mettre d'accord sur votre code. 
 

Vous pouvez maintenant continuez par le [Sprint 0 : Analyse du problème](./Sprint0Analyse.md). 

