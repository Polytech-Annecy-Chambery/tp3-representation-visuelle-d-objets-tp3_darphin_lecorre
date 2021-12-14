'''
File: test_house.py
Created Date: Monday November 8th 2021 - 04:26pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Mon Nov 08 2021
Modified By: Ammar Mian
-----
Fichier regroupant les tests de la question 4.
----
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
from House import House
from Wall import Wall
from Section import Section
import pygame
import OpenGL.GL as gl


class TestHouse(unittest.TestCase):
    configuration = Q4a()

    def test_configuration_exists(self):
        assert self.configuration is not None

    def test_House_exists(self):
        assert len(self.configuration.objects) >= 1
        assert isinstance(self.configuration.objects[0], House)

    def test_House_is_four_walls(self):
        """Teste si la maison est constituée de 4 murs."""
        house = self.configuration.objects[0]
        assert len(house.objects) == 4
        for wall in house.objects:
            assert isinstance(wall, Wall)

if __name__ == '__main__':
    import nose2
    nose2.main()
