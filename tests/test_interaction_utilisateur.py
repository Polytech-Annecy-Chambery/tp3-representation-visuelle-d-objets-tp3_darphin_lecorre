'''
File: test_interaction_utilisateur.py
Created Date: Tuesday October 26th 2021 - 01:33pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Wed Oct 27 2021
Modified By: Ammar Mian
-----
Fichier regroupant les tests des questions
(1).d), (1).e), (1).cf).
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


class TestQuestion1D(unittest.TestCase):
    configuration = Q1b_f()
    configuration.event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_PAGEUP, unicode="page up", mod=0)
    configuration.processKeyDownEvent()
    model_up = gl.glGetDoublev(gl.GL_MODELVIEW_MATRIX)
    pygame.quit()
    
    configuration = Q1b_f()
    configuration.event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_PAGEDOWN, unicode="page down", mod=0)
    configuration.processKeyDownEvent()
    model_down = gl.glGetDoublev(gl.GL_MODELVIEW_MATRIX)
    pygame.quit()
    def test_configuration_exists(self):
        assert self.configuration is not None

    def test_pageup(self):
        """Teste si l'appui de Pageup fait bien un zoom de 1.1
        """
        # ATTENETION : l'axe z correspond ici du coup à la deuxième ligne à case de la roation.
        # C'est pour ça que le facteru 1.1 est en 3e pos à la ligne 2 et 2e pos à la ligne 3.
        expected = np.array([[1.1, 0, 0, 0], [0, -4.37113883e-08, -1.1, 0], [0, 1.1, -4.37113883e-08, 0], [0, 0, -5, 1]])
        assert_almost_equal(self.model_up, expected, decimal=5)

    def test_pagedown(self):
        """Teste si l'appui de Pagedown fait bien un zoom de 1/1.1
        """
        # ATTENTION : pareil que pageup mais avec une division de 1.1
        expected = np.array([[1/1.1, 0, 0, 0], [0, -4.37113883e-08, -1/1.1, 0], [0, 1/1.1, -4.37113883e-08, 0], [0, 0, -5, 1]])
        assert_almost_equal(self.model_down, expected, decimal=5)


class TestQuestion1E(unittest.TestCase):
    configuration = Q1b_f()
    configuration.event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=4)
    configuration.processMouseButtonDownEvent()
    model_up = gl.glGetDoublev(gl.GL_MODELVIEW_MATRIX)
    pygame.quit()
    
    configuration = Q1b_f()
    configuration.event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=5)
    configuration.processMouseButtonDownEvent()
    model_down = gl.glGetDoublev(gl.GL_MODELVIEW_MATRIX)
    pygame.quit()
    def test_configuration_exists(self):
        assert self.configuration is not None

    def test_wheelup(self):
        """Teste si la molette vers le haut fait bien un zoom de 1.1
        """
        # ATTENETION : l'axe z correspond ici du coup à la deuxième ligne à case de la roation.
        # C'est pour ça que le facteru 1.1 est en 3e pos à la ligne 2 et 2e pos à la ligne 3.
        expected = np.array([[1.1, 0, 0, 0], [0, -4.37113883e-08, -1.1, 0], [0, 1.1, -4.37113883e-08, 0], [0, 0, -5, 1]])
        assert_almost_equal(self.model_up, expected, decimal=5)

    def test_wheeldown(self):
        """Teste si la molette vers le bas fait bien un zoom de 1/1.1
        """
        # ATTENTION : pareil que wheelup mais avec une division de 1.1
        expected = np.array([[1/1.1, 0, 0, 0], [0, -4.37113883e-08, -1/1.1, 0], [0, 1/1.1, -4.37113883e-08, 0], [0, 0, -5, 1]])
        assert_almost_equal(self.model_down, expected, decimal=5)


class TestQuestion1F(unittest.TestCase):
    configuration = Q1b_f()
    pygame.quit()
    def test_configuration_exists(self):
        assert self.configuration is not None

    # PAS DE TEST POSSIBLE AVEC LES LIRAIRIES INSTALLES A L'ECOLE
    


if __name__ == '__main__':
    import nose2
    nose2.main()
