#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""card-recognition -- Reconnaissance de cartes -- version du 01/12/12

    NAO reconnait les cartes du jeu de poker
"""

from __future__ import division

__author__ = 'Denis Pinsard'
__email__ = 'denis.pinsard@dichotomies.fr'

from naoqi import ALProxy
import nao
import Image
import numpy as np
import time

#______________________________________________________________________________
# Mouvements accomplis par NAO
# Un mouvement est décrit par dictionnaire dont les clés sont les noms des
# articulations et dont les valeurs donnent le "stiffness" à appliquer ainsi qu'une
# liste de couples (instant, position angulaire)

# Déplacement vers la position de repos
idle = {
    'RWristYaw':      [0.5, [(2, 35)]],
    'RElbowYaw':      [0.5, [(2, 55)]],
    'RShoulderPitch': [0.8, [(2, 69)]],
    'RShoulderRoll':  [0.8, [(2, -12)]],
    'RElbowRoll':     [0.5, [(2, 56)]],
    'HeadYaw':        [0.5,  [(2, 0)]],
    'HeadPitch':      [0.5,  [(2, -16)]]}
# Depuis la position REPOS, NAO déplace le bras droit pour demander une carte.
# NAO dirige la tête vers l'avant.
idle_to_give = {
    'RWristYaw':      [0.5, [(1, 65), (2, 91)]],
    'RElbowYaw':      [0.5, [(1, 75), (2, 95)]],
    'RShoulderPitch': [0.8, [(.5, 55), (2, 40)]],
    'RShoulderRoll':  [0.8, [(1, -6), (2, -1)]],
    'RElbowRoll':     [0.5, [(1, 70), (2, 84)]],
    'HeadYaw':        [0.5,  [(2, 0)]],
    'HeadPitch':      [0.5,  [(2, -16)]]}
# Depuis la position de demande de carte, NAO déplace le bras droit et la tête
# pour pouvoir lire la carte.
give_to_look = {
    'RWristYaw':      [0.5, [(3, 77)]],
    'RElbowYaw':      [0.5, [(3, 84)]],
    'RShoulderPitch': [0.8, [(3, -6)]],
    'RShoulderRoll':  [0.8, [(3, -46)]],
    'RElbowRoll':     [0.5, [(3, 85)]],
    'HeadYaw':        [0.5,  [(3, -72)]],
    'HeadPitch':      [0.5,  [(3, -21)]]}
# Depuis la position d'observation de la carte, NAO dirige sa main et sa tête
# pour rendre la carte
look_to_give = {
    'RWristYaw':      [0.5, [(3, 91)]],
    'RElbowYaw':      [0.5, [(3, 95)]],
    'RShoulderPitch': [0.8, [(3, 40)]],
    'RShoulderRoll':  [0.8, [(3, -1)]],
    'RElbowRoll':     [0.5, [(3, 84)]],
    'HeadYaw':        [0.5,  [(1, 0)]],
    'HeadPitch':      [0.5,  [(1, -16)]]}

#______________________________________________________________________________
def move(joints):
    """Mise en mouvement des articulations selon la description `joints`
    
    `joints` est une structure de données telles que décrites ci-dessus
    """
    chain = []
    stiffnesses = []
    angles = []
    times = []
    for joint in joints:
        chain.append(joint)
        stiffnesses.append(joints[joint][0])
        joint_times, joint_angles  = zip(*joints[joint][1])
        joint_angles = [value / 180 * np.pi for value in joint_angles]
        angles.append(joint_angles)
        times.append(list(joint_times))
    motion.setStiffnesses(chain, stiffnesses)
    motion.angleInterpolation(chain, angles, times, True)
    
#______________________________________________________________________________
def open_hand():
    """Ouverture de la main droite"""
    motion.setStiffnesses('RHand', .5)
    motion.setAngles('RHand', 1, .3)
    time.sleep(1)
    motion.setStiffnesses('RHand', 0)
    
#______________________________________________________________________________
def close_hand():
    """Fermeture de la main droite"""
    motion.setStiffnesses('RHand', .5)
    motion.setAngles('RHand', .2, .3)
    

#============== PROGRAMME PRINCIPAL =======================

nao.init('192.168.1.21')

try:
    # Initialisation des modules NAO
    tts = ALProxy("ALTextToSpeech")
    leds = ALProxy("ALLeds")
    ap = ALProxy("ALAudioPlayer")
    motion = ALProxy("ALMotion")
    videoModule = nao.VideoModule()
    sensorModule = nao.SensorModule()
    
    tts.post.say("Bonjour, je m'appelle David")
    move(idle)
    tts.post.say("Je sais reconnaitre les cartes")
    nao.wait(nao.TACTIL_TOUCHED, nao.HEAD_TOUCHED)
    leds.rasta(1)
    move(idle_to_give)
    tts.post.say("Donne moi une carte")
    while True:
        open_hand()
        nao.event.purge()
        event = nao.event.get()
        if event.type == nao.TACTIL_TOUCHED:
            if event.value in nao.HAND_RIGHT_TOUCHED:
                close_hand()
                move(give_to_look)
                # Capture d'une image sur la webcam
                naoImage = videoModule.getImage()
                # Affichage de l'image vue par NAO
                image = Image.fromarray(naoImage.pixels)
                image.show()
                # Reconnaissance de la carte
                # ******************************************************************
                # ********************** À FAIRE **********************************
                # ******************************************************************
                tts.post.say("Je n'arrive pas à lire cette carte")
                move(look_to_give)
                tts.post.say("Donne moi une autre carte")
            elif event.value in nao.HAND_LEFT_TOUCHED:
                break
    
finally:
    move(idle)
    # Libération propre des ressources avant de quitter        
    nao.shutdown()














    


                