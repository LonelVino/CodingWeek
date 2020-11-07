# Jeu de la vie - Sprint 0 : Installation du socle technique


Le premier travail consiste à préparer le socle technique nécessaire au bon developpement du projet. Le projet **gameoflife** sera :

+ Un projet Visual Studio Code 
+ Utilisant [git](https://git-scm.com/) comme gestionnaire de version
+ Qui sera déposé sur le [GitLab pédagogique de CentraleSupélec](https://gitlab-cw5.centralesupelec.fr/) dédié à votre projet. Dans votre cas `gitlab-cw5.centralesupelec.fr`.



## Versionner avec git

Comme vous l'avez vu lors du cours SIP et lors du tutorial de début de coding weeks, git est un logiciel de gestion de versions décentralisé. Pour rappel, le tutorial est disponible [ici](https://centralesupelec.edunao.com/pluginfile.php/65396/course/section/4378/cours-1.pdf).

D'autres ressources intéressantes sur git :

+ rapide tutorial [ici](http://rogerdudler.github.io/git-guide/index.fr.html).
+ [http://marklodato.github.io/visual-git-guide/index-en.html](http://marklodato.github.io/visual-git-guide/index-en.html)
+ [https://openclassrooms.com/fr/courses/1233741-gerez-vos-codes-source-avec-git](https://openclassrooms.com/fr/courses/1233741-gerez-vos-codes-source-avec-git)
+ ...




### Mise en place de Git sur le projet **`gameoflife`**


Les consignes à suivre pour cette mise en place et pour une bonne prise en main de git sont dans [ce tutorial](https://github.com/hudelotc/CentraleSupelec_CodingWeeks_2020/blob/main/Git_install.md) qu'il vous faut donc suivre jusqu'au bout.

#### <span style="color: #26B260">A la fin de ce tutorial vous aurez atteint le JALON 1 : Mise en place de Git et GitLab pour un travail de développement collaboratif</span> 


## Créer un projet python avec Visual Studio Code : **`gameoflife`**


Nous vous recommandons d'utiliser l'éditeur de code [Visual Studio Code](./VisualStudioCode.md) qui vous a déjà été recommandé lors du cours SIP. Il vous suffit juste d'ouvrir le répertoire local du projet `gameoflife` que vous venez de créer dans l'étape précédente.

A ce stade du projet, vous devriez donc avoir :

+ Un projet gameoflife sur le depôt gitlab distant
+ + Chaque membre du groupe devrait avoir un clone local de ce projet sur son ordinateur, et qui est ouvert via VSCode.

Dans la suite du projet, vous allez travailler de la manière suivantes:


**Pour chaque fonctionnalité** : 

+ **Chaque membre du groupe travaille, de son côté,  sur son dépôt local. Attention, dans ce cas, il est préférable de ne pas travailler sur la branche `master` mais sur des branches de travail, qui vous seront propres, et que vous devrez créer.**

+ **Il faudra convenir entre vous d'un temps suffisant pour que chacun puisse proposer une solution à cette fonctionnalité.**

+ **Au bout de ce temps fixé, il faudra alors prévoir un temps de mise en commun et de revue entre vous de chacune des foncionnalités. C'est un procédé que l'on pourrait assimilé à de la [revue de code](https://en.wikipedia.org/wiki/Code_review)**

+ **Après ce travail de revue, vous pourrez alors décidé de la version de la foncionnalité à mettre sur la branche `master` qui devra contenir à tout moment la version stable de votre projet.** 

+ **Et bien évidemment, il sera nécessaire de pusher sur le depôt distant pour vous permettre de partager cette version stable entre vous.**

+ **Le passage et le travail à une nouvelle fonctionnalité se fera donc sur la base d'une branche master synchronisée entre vous tous** 


Vous pouvez maintenant continuez par le [Sprint 0 : Analyse du problème](./Sprint0Analyse.md). 

