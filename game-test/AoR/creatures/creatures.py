# !/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Pray To Shiva Gatuma Christ Chan
# https://github.com/TheLordJesusHimself/game-test/

'''
Assault of Restitution
'''

# note: view associated GitHub info as well
__version__ = 'v0.1.0'  
__author__ = 'TheLordJesusHimself'
__email__ = 'callumblumfield08@gmail.com'
__maintainer__ = ['TheLordJesusHimself', 'Cornelius-Figgle']
__copyright__ = 'Copyright (c) 2023 Callum Blumfield'
__license__ = 'MIT'
__status__ = 'Development'
__credits__ = ['Callum Blumfield', 'Max Harrison']


from math import log10


def _level_scaling_factor(x: int) -> int:
    '''
    Uses a fancy algorithm to generate a level scaling factor for the
    creatures. The `-1` at the end is so we can add round numbers to
    the value

    ```text
    1: 0    2: 1    3: 3    4: 5    5: 7
    6: 9    7: 12   8: 14   9: 17   10: 20
    ```
    '''

    return round(log10(x**2) * x + 1) - 1


class Jim:
    '''
    "WE ARE FINALLY GONNA HAVE PARENTS!!"
        - Cornelius-Figgle, on the subject of parents
    '''

    def __init__(self, level: int) -> None:        
        self.health = _level_scaling_factor(level)
        self.attack = _level_scaling_factor(level)

        self.inventory = []


class Player(Jim):
    '''
    "Are we not all creatures?"
        - TheLordJesusHimself, on the subject of file names
    '''

    def __init__(self, level: int) -> None:
        super().__init__(level)

        self.health = 100
        self.attack = 5

class Bear(Jim):
    '''
    Bear fite
    '''

    def __init__(self, level: int) -> None:
        self.health += 10
        self.attack += 5

class MaxHarrison(Jim):
    '''
    Final boss fite
    '''

    def __init__(self, level: int) -> None:
        self.health += 100
        self.attack += 100