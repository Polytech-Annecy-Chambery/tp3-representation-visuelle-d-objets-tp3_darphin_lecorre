# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [ 
                [0, 0, 0 ], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                [0, self.parameters['thickness'], 0],
				[0, self.parameters['thickness'], self.parameters['height']], 
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'], 0]
                ]
        self.faces = [
                [0, 1, 2, 3],
                [0, 1, 5, 4],
                [2, 3, 7, 6],
                [0, 3, 7, 4],
                [1, 2, 6, 5],
                [4, 5, 6, 7],
                ] 
        return self 

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        if x.parameters['position'][0] + x.parameters['width'] < self.parameters['position'][0] + self.parameters['width'] and x.parameters['position'][2] + x.parameters['height'] < self.parameters['position'][2] + self.parameters['height'] and x.parameters['thickness'] == self.parameters['thickness'] :
            return True
        else:
            return False
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        l =[]
        if x.parameters['position'][0] != self.parameters['position'][0] :
            subsection1 = Section({'width': abs(self.parameters['position'][0] - x.parameters['position'][0]),
                                   'height': self.parameters['height'],
                                   'thickness': self.parameters['thickness'],
                                   'color': self.parameters['color'],
                                   'edges': self.parameters['edges'],
                                   'position': self.parameters['position']})
            l.append(subsection1)
        if (self.parameters['position'][2] - x.parameters['position'][2] + x.parameters['height']) != self.parameters['height']:
            subsection2 = Section({'width': x.parameters['width'],
                                   'height': self.parameters['height'] - ((x.parameters['position'][2] - self.parameters['position'][2]) + x.parameters['height']),
                                   'thickness': self.parameters['thickness'],
                                   'color': self.parameters['color'],
                                   'edges': self.parameters['edges'],
                                   'position': [ x.parameters['position'][0],  self.parameters['position'][1], (x.parameters['position'][2] + x.parameters['height'])]})
            l.append(subsection2)
        if x.parameters['position'][2] != self.parameters['position'][2] :
            subsection3 = Section({'width': x.parameters['width'],
                                    'height': abs(self.parameters['position'][2] - x.parameters['position'][2]),
                                    'thickness': self.parameters['thickness'],
                                    'color': self.parameters['color'],
                                    'edges': self.parameters['edges'],
                                    'position': [ x.parameters['position'][0],  self.parameters['position'][1], self.parameters['position'][2]]})
            l.append(subsection3)
        if (x.parameters['position'][0] - self.parameters['position'][0] + x.parameters['width']) != self.parameters['width']:
            subsection4 = Section({'width': self.parameters['width'] - (x.parameters['position'][0] - self.parameters['position'][0] + x.parameters['width']),
                                    'height': self.parameters['height'],
                                    'thickness': self.parameters['thickness'],
                                    'color': self.parameters['color'],
                                    'edges': self.parameters['edges'],
                                    'position': [ (x.parameters['position'][0] + x.parameters['width']),  self.parameters['position'][1], self.parameters['position'][2]]})
            l.append(subsection4)
        return l
    # Draws the edges
    def drawEdges(self):
        f = self.faces
        v = self.vertices
        for i in f :
            a,b,c,d = v[i[0]],v[i[1]],v[i[2]],v[i[3]]
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les edges : GL_LINE
            gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
            gl.glColor3fv([0, 0, 0]) # Couleur noir
            gl.glVertex3fv(a)
            gl.glVertex3fv(b)
            gl.glVertex3fv(c)
            gl.glVertex3fv(d)
            gl.glEnd()
                    
    # Draws the faces
    def draw(self):
        gl.glPushMatrix()
        gl.glTranslated(self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2])
        gl.glRotatef(self.parameters['orientation'], 0, 0, 1)
        if self.parameters['edges'] == True :
            self.drawEdges()
        f = self.faces
        v = self.vertices
        for i in f :
            a,b,c,d = v[i[0]],v[i[1]],v[i[2]],v[i[3]]
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
            gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
            gl.glColor3fv(self.parameters['color']) # Couleur gris moyen
            gl.glVertex3fv(a)
            gl.glVertex3fv(b)
            gl.glVertex3fv(c)
            gl.glVertex3fv(d)
            gl.glEnd()  
        gl.glPopMatrix()