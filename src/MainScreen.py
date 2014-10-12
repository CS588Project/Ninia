'''
Created on Oct 12, 2014

@author: jaychen
'''
from libavg import avg, app, widget
from Resource import ImgRes

class MainDiv(app.MainDiv):
    def onInit(self):  
        self.mediadir='../media/'
        
        avg.ImageNode(href = 'gray_block.jpg', size = self.size, parent=self)
        
        #main division
        main_div = avg.DivNode(pos=(0,0),size=self.size, parent = self)
        avg.ImageNode(href = 'bg_black.jpg',size = self.size, parent=main_div) 
        avg.ImageNode(href = 'trashcan.png',pos=(self.width-128, self.height-128), parent = main_div)
        main_div.opacity = 1;
        
        #image division
        img_div = avg.DivNode(pos=(0,0),size=self.size, parent = self)
        #node.parent.removeChild(node)
        #res_div.appendChild(node)
        
        #video division
        #vdi_div = avg.DivNode(pos=(0,0),size=self.size, parent = self)
        
        #slide division
        #sld_div = avg.DivNode(pos=(0,0),size=self.size, parent = self)
        
        
        #items on res division
        #avg.ImageNode(href='bg_green.jpg',size=img_div.size,parent = img_div)
        #node1 = avg.WordsNode(pos=(10,10), text="I'm Hero", parent=img_div)
        
        node = ImgRes(href='123.png', pos=(10,10), parent=img_div)
       
        #node = avg.ImageNode(href='123.png', pos=(10,10), parent=img_div)
        #node.subscribe(node.CURSOR_DOWN, onMouseDown)
        #node.subscribe(node.CURSOR_MOTION, onMouseMove)
        #node.subscribe(node.CURSOR_UP, onMouseUp)