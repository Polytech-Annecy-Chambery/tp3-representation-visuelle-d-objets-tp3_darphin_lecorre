'''
File: test_section.py
Created Date: Tuesday October 26th 2021 - 01:33pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Mon Nov 08 2021
Modified By: Ammar Mian
-----
Fichier regroupant les tests des questions
(2).a), (2).b), (2).c).
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
from Section import Section
import pygame
import OpenGL.GL as gl


class TestSection(unittest.TestCase):
    configuration = Q2c()

    def test_configuration_exists(self):
        assert self.configuration is not None

    def test_Section_exists(self):
        assert len(self.configuration.objects) >= 1
        assert isinstance(self.configuration.objects[0], Section)

    def test_vertices_exists(self):
        section = self.configuration.objects[0]
        assert hasattr(section, 'vertices')

    def test_faces_exists(self):
        section = self.configuration.objects[0]
        assert hasattr(section, 'faces')

    def test_vertices_length(self):
        section = self.configuration.objects[0]
        assert len(section.vertices) == 8

    def test_faces_length(self):
        section = self.configuration.objects[0]
        assert len(section.faces) == 6

    def test_width_is_right(self):
        """Teste si la largeur de la section est bien celle entrée en paramètre.
        """
        section = self.configuration.objects[0]
        width = section.vertices[2][0] - section.vertices[1][0]
        assert width == section.parameters['width']

    def test_height_is_right(self):
        """Teste si la hauteur de la section est bien celle entrée en paramètre.
        """
        section = self.configuration.objects[0]
        height = section.vertices[1][2] - section.vertices[0][2]
        assert height == section.parameters['height']

    def test_thickness_is_right(self):
        """Teste si la profondeur de la section est bien celle entrée en paramètre.
        """
        section = Section({'width':7, 'height':2.6, 'thickness': 1.5})
        thickness = section.vertices[4][1] - section.vertices[3][1]
        assert thickness == section.parameters['thickness']


if __name__ == '__main__':
    import nose2
    nose2.main()
