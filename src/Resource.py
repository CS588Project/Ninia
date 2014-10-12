'''
Created on Sep 28, 2014

@author: jaychen
'''
from libavg import avg
from Controller import LeapController

class ImgRes(avg.ImageNode):

    def __init__(self, parent=None, **kargs):
        super(ImgRes, self).__init__(**kargs)
        self.registerInstance(self, parent)
        self.setControl()
        
    def setControl(self):
        self.subscribe(self.CURSOR_DOWN, LeapController.onMouseDown)
        self.subscribe(self.CURSOR_MOTION, LeapController.onMouseMove)
        self.subscribe(self.CURSOR_UP, LeapController.onMouseUp)
        