# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:24:32 2020

@author: reaga
"""

class car():
    def __init__(self,name,windows,Wheels):
        self.name=name
        self.windows=windows
        self.Wheels=Wheels
        
    def Wheels(self):
        return self.Wheels+self.windows
class moto(car):
    def __init__(self,seat,handleBar):
        super.__init__(name,windows,Wheels)
        self.seat=seat
        self.handleBar=handleBar
        