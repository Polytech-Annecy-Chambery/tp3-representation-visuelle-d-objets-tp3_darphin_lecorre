'''
File: test_base.py
Created Date: Tuesday October 26th 2021 - 01:33pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Mon Nov 15 2021
Modified By: Ammar Mian
-----
Fichier regroupant les tests des questions
(1).a), (1).b), (1).c).
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
import pygame
import OpenGL.GL as gl


class TestQuestion1A(unittest.TestCase):
    def test_configuration_exists(self):
        configuration = Q1a()
        pygame.quit()
        assert configuration is not None


class TestQuestion1B(unittest.TestCase):
    configuration = Q1b_f()
    pygame.quit()
    def test_configuration_exists(self):
        assert self.configuration is not None

    def test_screen_position_is_good(self):
        position = self.configuration.parameters['screenPosition'] 
        assert position == -5

    def test_xaxis_color_is_good(self):
        color = self.configuration.parameters['xAxisColor'] 
        assert color == [1, 1, 0]

    def test_yaxis_color_is_good(self):
        color = self.configuration.parameters['yAxisColor'] 
        assert color == [0, 1, 1]


class TestQuestion1C(unittest.TestCase):
    configuration = Q1b_f()
    model = gl.glGetDoublev(gl.GL_MODELVIEW_MATRIX)
    pygame.quit()
    def test_configuration_exists(self):
        assert self.configuration is not None

    def test_transformation_matrix_is_good(self):
        """Teste si la matrice de transformation prends bien en compte la rotation pour avoir l'axe z dans le bon sens.
        """
        expected = np.array([[1, 0, 0, 0], [0, -4.37113883e-08, -1, 0], [0, 1, -4.37113883e-08, 0], [0, 0, -5, 1]])
        assert_almost_equal(self.model, expected)



if __name__ == '__main__':
    import nose2
    nose2.main()
