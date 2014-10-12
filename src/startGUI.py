'''
Created on Sep 28, 2014

@author: jaychen
'''
from libavg import avg, app, widget
from MainScreen import MainDiv

screen_width=1440
screen_lenght=900
        
app.App().run(MainDiv(), app_resolution = '2880x1800', app_fullscreen='True')
