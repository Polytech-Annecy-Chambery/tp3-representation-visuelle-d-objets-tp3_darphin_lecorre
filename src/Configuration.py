# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame
import OpenGL.GL as gl
import OpenGL.GLU as glu
       
class Configuration:
    
    # Constructor
    def __init__(self, parameters = {}) :
        # Parameters
        # axes: if True the axis is displayed
        # xAxisColor: color for the x-axis
        # yAxisColor: color for the y-axis
        # zAxisColor: color for the z-axis
        # screenPosition: position of the screen on the z-axis (negative value) - on               

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters   
        if 'axes' not in self.parameters:
            self.parameters['axes'] = True
        if 'xAxisColor' not in self.parameters:
            self.parameters['xAxisColor'] = [1, 0, 0] 
        if 'yAxisColor' not in self.parameters:
            self.parameters['yAxisColor'] = [0, 1, 0]                 
        if 'zAxisColor' not in self.parameters:
            self.parameters['zAxisColor'] = [0, 0, 1] 
        if 'screenPosition' not in self.parameters:
            self.parameters['screenPosition'] = -10
                    
        # Initializes PyGame
        self.initializePyGame()

        # Initializes OpenGl
        self.initializeOpenGL()

        # Initializes the tranformation matrix
        self.initializeTransformationMatrix()
             
        # Initializes the object list
        self.objects = []    
            
        # Generates coordinates
        self.generateCoordinates()     
        
    # Initializes Pygame
    def initializePyGame(self):
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((800, 600), pygame.DOUBLEBUF|pygame.OPENGL)    
        # Gets pygame screen
        self.screen = pygame.display.get_surface()  
        
    # Initializes OpenGL    
    def initializeOpenGL(self):
        # Sets the screen color (white)
        gl.glClearColor(1, 1, 1, 1)

        # Clears the buffers and sets DEPTH_TEST to remove hidden surfaces
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)                  
        gl.glEnable(gl.GL_DEPTH_TEST)   
        
    # Initializes the tranformation matrix    
    def initializeTransformationMatrix(self):     
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluPerspective(70, (self.screen.get_width()/self.screen.get_height()), 0.1, 100.0)

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.glTranslatef(0.0,0.0, self.parameters['screenPosition'])       
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]    
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        if parameterKey == 'screenPosition':
            self.initializeTransformationMatrix()
        return self    

    # Generates the axis coordinates in the real space        
    def generateCoordinates(self):
        self.vertices = [ 
                [0, 0, 0 ],
                [1, 0, 0 ],
                [0, 1, 0],
                [0, 0, 1]
                ] 
        self.edges = [
                [0, 1],
                [0, 2],
                [0, 3]
                ]
        
    # Adds an object to the object list
    def add(self, x):
        self.objects.append(x)
        return self
               
    # Draws the axes and objects    
    def draw(self):

        # Draws the axes
        if self.parameters['axes']:
            gl.glBegin(gl.GL_LINES)

            # x-axis
            gl.glColor3fv(self.parameters['xAxisColor'])
            gl.glVertex3fv(self.vertices[0])
            gl.glVertex3fv(self.vertices[1])                
    
            # y-axis
            gl.glColor3fv(self.parameters['yAxisColor'])
            gl.glVertex3fv(self.vertices[0])
            gl.glVertex3fv(self.vertices[2]) 
    
            # z-axis
            gl.glColor3fv(self.parameters['zAxisColor'])
            gl.glVertex3fv(self.vertices[0])
            gl.glVertex3fv(self.vertices[3]) 
            
            gl.glEnd()      
            
        # Draws the objects if any
        for x in self.objects:
            x.draw()
            
    # Processes the KEYDOWN event
    def processKeyDownEvent(self):
        # Rotates around the z-axis                       
        if self.event.dict['unicode'] == 'Z' or (self.event.mod & pygame.KMOD_SHIFT and self.event.key == pygame.K_z):
            gl.glRotate(-2.5, 0, 0, 1)                     
        elif self.event.dict['unicode'] == 'z' or self.event.key == pygame.K_z:
            gl.glRotate(2.5, 0, 0, 1) 
        
        # Draws or suppresses the reference frame
        elif self.event.dict['unicode'] == 'a' or self.event.key == pygame.K_a:
            self.parameters['axes'] = not self.parameters['axes']
            pygame.time.wait(300)
    
    # Processes the MOUSEBUTTONDOWN event
    def processMouseButtonDownEvent(self):
        pass
    
    # Processes the MOUSEMOTION event
    def processMouseMotionEvent(self):
        pass
         
    # Displays on screen and processes events    
    def display(self): 
           
        # Displays on screen
        self.draw()
        pygame.display.flip() 
    
        # Allows keybord events to be repeated
        pygame.key.set_repeat(1, 100)

        # Infinite loop    
        while True:

            # Waits for an event
            self.event = pygame.event.wait()
 
            # Processes the event
            
            # Quit pygame (compatibility with pygame1.9.6 and 2.0.0)
            if self.event.type == pygame.QUIT or (self.event.type == pygame.WINDOWEVENT and pygame.event.wait(100).type == pygame.QUIT):
                pygame.quit()
                break  

            elif self.event.type == pygame.KEYDOWN: 
                self.processKeyDownEvent()
                
            elif self.event.type == pygame.MOUSEBUTTONDOWN:
                self.processMouseButtonDownEvent() 
            
            elif self.event.type == pygame.MOUSEMOTION: 
                self.processMouseMotionEvent()
                
            # Clears the buffer and displays on screen the result of the keybord action
            gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
            self.draw()
            pygame.event.clear()
            pygame.display.flip()