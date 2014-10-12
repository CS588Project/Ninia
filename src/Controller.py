'''
Created on Oct 12, 2014

@author: jaychen
'''
import os, sys, inspect
from platform import system
if system() is 'Windows':
    sys.path.insert(0, "../libs/win")
else:
    sys.path.insert(0, "../libs/mac")
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
    
from libavg import avg

offset = None

class LeapController(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        pass
    
    def onMouseDown(event):
        global offset
        node = event.node
        offset = node.getRelPos((event.x, event.y))
        node.setEventCapture()

    def onMouseMove(event):
        global offset
        node = event.node
        if offset != None:
            node.x = event.x-offset[0]
            node.y = event.y-offset[1]

    def onMouseUp(event):
        global offset
        node = event.node
        if offset != None:
            node.releaseEventCapture()
            offset = None;
        