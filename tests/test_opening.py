'''
File: test_opening.py
Created Date: Monday November 8th 2021 - 10:51pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Mon Nov 08 2021
Modified By: Ammar Mian
-----
Fichier regroupant les tests des questions
(5).a), (5).b), (5).c) et (5).d)
-----
Copyright (c) 2021 Université Savoie Mont-Blanc
'''

import sys
sys.path.append('../src')
sys.path.append('./src')
import numpy as np
from numpy.testing import assert_almost_equal
import unittest
import numbers

from Main import *
from Opening import Opening
from Wall import Wall
from Section import Section
import pygame
import OpenGL.GL as gl


class TestOpeningClass(unittest.TestCase):

    def test_Opening_vertices_length(self):
        opening = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
        assert len(opening.vertices) == 8

    def test_Opening_faces_length(self):
        opening = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
        assert len(opening.faces) == 4


class TestSectionCreateOpening(unittest.TestCase):
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    opening3 = Opening({'position': [4, 0, 1.7], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    
    def test_canCreateopening_is_boolean(self):
        assert type(self.section.canCreateOpening(self.opening1)) == bool
        assert type(self.section.canCreateOpening(self.opening2)) == bool
        assert type(self.section.canCreateOpening(self.opening3)) == bool


    def test_canCreateopening_works(self):
        """Teste les sorties de la méthode canCreateOpening avec 3 exemples.
        """
        assert self.section.canCreateOpening(self.opening1)
        assert self.section.canCreateOpening(self.opening2)
        assert not self.section.canCreateOpening(self.opening3)


class TestCreateNewSections(unittest.TestCase):


    def test_length_new_sections_general(self):
        """Teste la longeur des sections pour le cas général.
        """
        section = Section({'width':7, 'height':2.6})
        opening1 = Opening({'position': [2, 0, 0.1], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
        sections = section.createNewSections(opening1)
        assert len(sections) == 4

    def test_length_new_sections_left(self):
        """Teste la longeur des sections pour le cas pas de section à gauche.
        """
        section = Section({'width':7, 'height':2.6})
        opening1 = Opening({'position': [0, 0, 0.1], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
        sections = section.createNewSections(opening1)
        assert len(sections) == 3

    def test_length_new_sections_right(self):
        """Teste la longeur des sections pour le cas pas de section à droite.
        """
        section = Section({'width':7, 'height':2.6})
        opening1 = Opening({'position': [0, 7-0.9, 0.1], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
        sections = section.createNewSections(opening1)
        assert len(sections) == 3

    def test_length_new_sections_top(self):
        """Teste la longeur des sections pour le cas pas de section en haut.
        """
        section = Section({'width':7, 'height':2.6})
        opening1 = Opening({'position': [2, 0, 2.6-2.15], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
        sections = section.createNewSections(opening1)
        assert len(sections) == 3

    def test_length_new_sections_bottom(self):
        """Teste la longeur des sections pour le cas pas de section en bas.
        """
        section = Section({'width':7, 'height':2.6})
        opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
        sections = section.createNewSections(opening1)
        assert len(sections) == 3


if __name__ == '__main__':
    import nose2
    nose2.main()
