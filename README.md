NAO joue au poker
================

Lors de l'�x�cution du programme `card-recognition.py` le robot NAO :

* Se pr�sente et affirme qu'il sait reconna�tre les cartes.
* Lorsqu'on lui touche la t�te il tend la main droite et demande une carte.
* On place alors une carte entre ses doigts.
* Lorsqu'on lui touche la main droite il ferme sa main et d�place
son bras et sa t�te de fa�on �voir la carte.
* Lorsque la carte est dans son champ de vision il tente de reconna�tre cette carte et prononce alors le nom de la carte.
* Il d�place alors son bras pour redonner la carte et en redemander une autre.
* Le programme s'arr�te lorsqu'on lui touche la main gauche.

En fait, ce programme est actuellement incomplet.
Il manque la partie reconnaissance de la carte.
**Votre mission consiste � concevoir et mettre au point cette partie 
manquante.**

Vous pouvez jeter un oeil sur le programme `card-recognition.py` mais
sa compr�hension n'est pas n�cessaire pour ce que vous avez � faire.

Le dossier `photos` contient des images prises par NAO lorsque la carte
est en face de lui. Il s'agit de traduire ces images en un tableau
de pixels (numpy) puis d'analyser ce tableau pour reconna�tre la carte.
C'est une t�che complexe et j'attends de vous que vous me proposiez des
id�es, des m�thodes, des d�marches que vous pourriez mettre en oeuvre.

Le dossier `cards` contient �galement des images de cartes mais la situation
est ici plus simple. En effet, elles ont toutes pour dimensions 200x280 pixels
et la carte occupe toute l'image.
Proposez moi l� aussi des id�es pour reconna�tre les cartes.
Vous pouvez proc�der par �tapes :

* Distinguer une carte noire d'une carte rouge.
* Distinguer une figure d'une carte mineure.
* Distinguer un tr�fle d'un pique.
* etc.

�crivez du code pour mettre vos id�es � l'�preuve.


