NAO joue au poker
================

Lors de l'éxécution du programme `card-recognition.py` le robot NAO :

* Se présente et affirme qu'il sait reconnaître les cartes.
* Lorsqu'on lui touche la tête il tend la main droite et demande une carte.
* On place alors une carte entre ses doigts.
* Lorsqu'on lui touche la main droite il ferme sa main et déplace
son bras et sa tête de façon à voir la carte.
* Lorsque la carte est dans son champ de vision il tente de reconnaître cette carte et prononce alors le nom de la carte.
* Il déplace alors son bras pour redonner la carte et en redemander une autre.
* Le programme s'arrête lorsqu'on lui touche la main gauche.

En fait, ce programme est actuellement incomplet.
Il manque la partie reconnaissance de la carte.
**Votre mission consiste à concevoir et mettre au point cette partie 
manquante.**

Vous pouvez jeter un oeil sur le programme `card-recognition.py` mais
sa compréhension n'est pas nécessaire pour ce que vous avez à faire.

Le dossier `photos` contient des images prises par NAO lorsque la carte
est en face de lui. Il s'agit de traduire ces images en un tableau
de pixels (numpy) puis d'analyser ce tableau pour reconnaître la carte.
C'est une tâche complexe et j'attends de vous que vous me proposiez des
idées, des méthodes, des démarches que vous pourriez mettre en oeuvre.

Le dossier `cards` contient également des images de cartes mais la situation
est ici plus simple. En effet, elles ont toutes pour dimensions 200x280 pixels
et la carte occupe toute l'image.
Proposez moi là aussi des idées pour reconnaître les cartes.
Vous pouvez procéder par étapes :

* Distinguer une carte noire d'une carte rouge.
* Distinguer une figure d'une carte mineure.
* Distinguer un trèfle d'un pique.
* etc.

Écrivez du code pour mettre vos idées à l'épreuve.


