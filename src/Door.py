# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
import OpenGL.GLU as glu
from Window import Window
from Section import Section
from Opening import Opening
import pygame as pygame

class Door:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters dictionnary
        # position: position of the door
        # width: width of the door
        # height: height of the door
        # thickness: thickness of the door
        # color: color of the door

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]       
        if 'width' not in self.parameters:
            self.parameters['width'] = 0.9
        if 'height' not in self.parameters:
            self.parameters['height'] = 2.15
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.05    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.6, 0.5, 0]  
        self.parameters['openDoor'] = False      
        
        # Initializes the object list
        self.objects = []     

        # Adds a Section for this object
        self.parentSection = Section({'width': self.parameters['width'], \
                                      'height': self.parameters['height'], \
                                      'thickness': self.parameters['thickness'], \
                                      'color': self.parameters['color']})
        self.objects.append(self.parentSection)           
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]   

    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     
              
    # Finds the section where the object can be inserted
    def findSection(self, x):
        for item in enumerate(self.objects):
            if isinstance(item[1], Section) and item[1].canCreateOpening(x):
                return item
        return None
    
    # Adds an object to the object list
    def add(self, x):
        section = self.findSection(x)
        # Removes the section from the list
        if section != None:
            newSections = section[1].createNewSections(x)         
            if isinstance(x, Window):
                opening = Opening({
                    'position':[x.getParameter('position')[0], 0, x.getParameter('position')[2]],
                    'width': x.getParameter('width'),
                    'height': x.getParameter('height'),
                    'thickness': self.parameters['thickness'],
                    'color': self.parameters['color']
                    }) 
                self.objects.append(opening)               
                                              
            # Removes the old door
            self.objects.pop(section[0])  
            
            # Adds the new door with opening
            self.objects.extend(newSections)           

            # Adds the window 
            self.objects.append(x) 
            
        return self            
    
    # Processes the Pygame USER EVENT
    def processPygameUserEvent(self):
        # Gets the model view matrix    
        modelViewMatrix = gl.glGetDoublev(gl.GL_MODELVIEW_MATRIX)
        
        # Checks if the USER event is received
        if pygame.event.peek(pygame.USEREVENT):
            # Gets the events and recovers the window coordinates from the first one
            event = pygame.event.get(pygame.USEREVENT)
            winX = event[0].dict['winX']
            winY = event[0].dict['winY']
            winZ = event[0].dict['winZ']
            
            # Unprojects the window coordinates to get the model coordinate
            position =  glu.gluUnProject(winX, winY, winZ, modelViewMatrix, gl.glGetDoublev(gl.GL_PROJECTION_MATRIX),  gl.glGetIntegerv(gl.GL_VIEWPORT))
            
            # Checks if there is a section corresponding to the event position
            sectionFound = False
            for x in self.objects:
                if x.getParameter('position')[0] < position[0] < x.getParameter('position')[0] + x.getParameter('width') and \
                    x.getParameter('position')[2]  < position[2] < x.getParameter('position')[2] + x.getParameter('height') and \
                    abs(x.getParameter('position')[1] - position[1]) < 0.05:
                    sectionFound = True        

            if sectionFound:
                # Sets the parameter fir opening the door
                self.setParameter('openDoor', not self.getParameter('openDoor'))
            else:
                # Sends again the event for processing by clones if any
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, event[0].dict))        
           
    # Draws the faces
    def draw(self):
        
        # Saves the frame coordinates
        gl.glPushMatrix()  
                
        # Defines the new transformation matrix : translation
        gl.glTranslatef(self.parameters['position'][0], self.parameters['position'][1], 0)
        
        # Rotation for the door if it is opened
        if self.getParameter('openDoor') == True:         
            gl.glRotate(-90, 0, 0, 1)  
            
        # Processes the Pygrame USER event
        self.processPygameUserEvent()
        
        # Draws the edges of the parent section
        self.parentSection.drawEdges()        
        
        # Draws the objects
        for x in self.objects:
            x.draw()
            
        # Restores the frame coordinates   
        gl.glPopMatrix()   
