'''
File: test_wall.py
Created Date: Monday November 8th 2021 - 03:32pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Mon Nov 08 2021
Modified By: Ammar Mian
-----
Fichier regroupant les tests de la question 3.
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
from Wall import Wall
from Section import Section
import pygame
import OpenGL.GL as gl


class TestWall(unittest.TestCase):
    configuration = Q3a()
    
    def test_configuration_exists(self):
        assert self.configuration is not None

    def test_Wall_exists(self):
        assert len(self.configuration.objects) >= 1
        assert isinstance(self.configuration.objects[0], Wall)

    def test_Wall_is_one_section(self):
        """Teste si le mur est constitué d'une seule section parente et rien d'autre."""
        wall = self.configuration.objects[0]
        assert len(wall.objects) == 1
        assert isinstance(wall.objects[0], Section)


if __name__ == '__main__':
    import nose2
    nose2.main()
