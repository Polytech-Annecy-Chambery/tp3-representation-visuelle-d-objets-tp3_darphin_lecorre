# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class House:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the house
        # orientation: orientation of the house

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]  
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0  
                
        # Objects list
        self.objects = []

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self
       
    # Adds an object    
    def add(self, x):
        self.objects.append(x)
        return self
            
    # Draws the house      
    def draw(self):
        gl.glPushMatrix()
        gl.glTranslated(self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2])
        gl.glRotatef(self.parameters['orientation'], 0, 0, 1)
        for x in self.objects: 
            x.draw() 
        gl.glPopMatrix()