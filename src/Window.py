# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
from Section import Section

class Window:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the window
        # width: width of the window
        # height: height of the window
        # thickness: thickness of the window
        # color: colr of the window     
        # wings: number of wings

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]       
        if 'width' not in self.parameters:
            self.parameters['width'] = 1.25
        if 'height' not in self.parameters:
            self.parameters['height'] = 1
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.05    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.9, 0.95, 1] 
        if 'wings' not in self.parameters:
            self.parameters['wings'] = 2        
            
        # Initializes the object list
        self.objects = []       

        # Adds Section objects for this object
        for i in range(self.parameters['wings']):
            # Adds Section for this object
            section = Section({'position': [i*self.parameters['width']/self.parameters['wings'], 0, 0],
                                      'width': self.parameters['width']/self.parameters['wings'], \
                                      'height': self.parameters['height'], \
                                      'thickness': self.parameters['thickness'], \
                                      'color': self.parameters['color']})
            self.objects.append(section) 
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]  

    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self    
 
    # Adds an object to the object list
    def add(self, x):
        self.objects.append(x)
        return self
           
    # Draws the faces
    def draw(self):
        gl.glPushMatrix()
        
        # Defines the new transformation matrix : translation
        gl.glTranslatef(self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2])
        
        # Draws the objects    
        for x in self.objects:
            x.drawEdges()
            x.draw()
            
        # Restores the frame coordinates   
        gl.glPopMatrix() 

        