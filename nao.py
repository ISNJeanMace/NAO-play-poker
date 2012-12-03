#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""nao --  -- version du 18/08/12
"""

__author__ = 'Denis Pinsard'
__email__ = 'denis.pinsard@dichotomies.fr'


from naoqi import ALProxy, ALBroker, ALModule

import math
import time
import numpy as np

modules = []

def init(ip='127.0.0.1', port=9559):
    global myBroker
    myBroker = ALBroker('myBroker', '0.0.0.0', 0, ip, port)
    motion = ALProxy("ALMotion")
    motion.setStiffnesses('Body', .3)
    motion.setAngles('Body', motion.getAngles('Body', True), 1)
    time.sleep(1)
    motion.setStiffnesses('Body', 0)
    
def shutdown():
    print 'See You later'
    motion = ALProxy("ALMotion")
    motion.setStiffnesses('Body', .4)
    time.sleep(1)
    motion.setStiffnesses('Body', .2)
    time.sleep(1)
    motion.setStiffnesses('Body', 0)
    for module in modules:
        module.close()
    myBroker.shutdown()

(
    SPEECH_DETECTED,
    WORD_DETECTED,
    FACE_DETECTED,
    TACTIL_TOUCHED,
) = range(4)
HEAD_TOUCHED = [
    'FrontTactilTouched',
    'RearTactilTouched']
HAND_LEFT_TOUCHED = [
    'HandLeftLeftTouched',
    'HandLeftRightTouched',
    'HandLeftBackTouched']
HAND_RIGHT_TOUCHED = [
    'HandRightLeftTouched',
    'HandRightRightTouched',
    'HandRightBackTouched']

#______________________________________________________________________________
class event():
    events = []
    
    @staticmethod
    def put(evt):
        evt.time = time.time()
        event.events.append(evt)
        
    @staticmethod
    def get():
        while not event.events:
            time.sleep(.1)
        return event.events.pop(0)
        
    @staticmethod
    def purge():
        event.events = []
#______________________________________________________________________________

#______________________________________________________________________________
class Event():
    def __init__(self, type=None, value=None):
        self.type = type
        self.value = value
#______________________________________________________________________________
    
#______________________________________________________________________________
def wait(type, values=None):
    while True:
        evt = event.get()
        if type == evt.type:
            if values is None or evt.value in values:
                break
        time.sleep(.1)
#______________________________________________________________________________
    
#______________________________________________________________________________
class NaoModule(ALModule):
    
    def __init__(self):
        pass

    def start(self):
        pass
        
    def stop(self):
        pass
        
    def close(self):
        pass
#______________________________________________________________________________

#______________________________________________________________________________
class NaoImage():
    def __str__(self):
        return(
            'width = %s\n' % self.width +
            'height = %s\n' % self.height +
            'layersNumber = %s\n' % self.layersNumber +
            'colorSpace = %s\n' % self.colorSpace +
            'timestamp (sec) = %s\n' % self.timestamp +
            'timestamp (msec) = %s\n' % self.microtimestamp +
            'cameraID = %s\n' % self.cameraID +
            'leftAngle = %s°\n' % (self.leftAngle / math.pi * 180) +
            'rightAngle = %s°\n' % (self.rightAngle / math.pi * 180) +
            'topAngle = %s°\n' % (self.topAngle / math.pi * 180) +
            'bottomAngle = %s°\n' % (self.bottomAngle / math.pi * 180) +
            'pixels = %s' % self.pixels)
#______________________________________________________________________________

#______________________________________________________________________________
class VideoModule():
    
    def __init__(self, resolution=2, colorSpace=11, fps=5):
        self.vd = ALProxy('ALVideoDevice')
        modules.append(self)
        self.vd.subscribe('videoModule', resolution, colorSpace, fps)


    def getImage(self):
        results = self.vd.getImageRemote('videoModule')
        image = NaoImage()
        image.width = results[0]
        image.height = results[1]
        image.layersNumber = results[2]
        image.colorSpace = results[3]
        image.timestamp = results[4]
        image.microtimestamp = results[5]
        image.pixels = np.frombuffer(
            results[6], dtype=np.uint8).reshape((image.height, image.width, 3))
        image.cameraID = results[7]
        image.leftAngle = results[8]
        image.rightAngle = results[9]
        image.topAngle = results[10]
        image.bottomAngle = results[11]
        return image
        
    def startRecord(self, filename):
        self.vd.recordVideo('videoModule', 100, 1)
        
    def stopRecord(self, filename):
        self.vd.stopVideo('videoModule')
        
    def close(self):
        self.vd.unsubscribe('videoModule')
#______________________________________________________________________________

#______________________________________________________________________________
class SensorModule(ALModule):
    def __init__(self):
        ALModule.__init__(self, 'sensorModule')
        modules.append(self)
        self.memory = ALProxy('ALMemory')
        try:
            self.memory.subscribeToEvent("FrontTactilTouched",
                                         "sensorModule",
                                         "onTactilTouched")
            self.memory.subscribeToEvent("RearTactilTouched",
                                         "sensorModule",
                                         "onTactilTouched")
            self.memory.subscribeToEvent("HandLeftLeftTouched",
                                         "sensorModule",
                                         "onTactilTouched")
            self.memory.subscribeToEvent("HandLeftRightTouched",
                                         "sensorModule",
                                         "onTactilTouched")
            self.memory.subscribeToEvent("HandLeftBackTouched",
                                         "sensorModule",
                                         "onTactilTouched")
            self.memory.subscribeToEvent("HandRightLeftTouched",
                                         "sensorModule",
                                         "onTactilTouched")
            self.memory.subscribeToEvent("HandRightRightTouched",
                                         "sensorModule",
                                         "onTactilTouched")
            self.memory.subscribeToEvent("HandRightBackTouched",
                                         "sensorModule",
                                         "onTactilTouched")
        except Exception, e:
            print e

    def close(self):
        pass
        try:
            self.memory.unsubscribeToEvent("FrontTactilTouched",
                                           "sensorModule")
            self.memory.unsubscribeToEvent("RearTactilTouched",
                                           "sensorModule")
            self.memory.unsubscribeToEvent("HandLeftLeftTouched",
                                           "sensorModule")
            self.memory.unsubscribeToEvent("HandLeftRightTouched",
                                           "sensorModule")
            self.memory.unsubscribeToEvent("HandLeftBackTouched",
                                           "sensorModule")
            self.memory.unsubscribeToEvent("HandRightLeftTouched",
                                           "sensorModule")
            self.memory.unsubscribeToEvent("HandRightRightTouched",
                                           "sensorModule")
            self.memory.unsubscribeToEvent("HandRightBackTouched",
                                           "sensorModule")
        except Exception, e:
            print e

    def onTactilTouched(self, evt, val, *args):
        if val == 1:
            event.put(Event(TACTIL_TOUCHED, evt))
#______________________________________________________________________________


