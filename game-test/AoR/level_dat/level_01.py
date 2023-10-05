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


from typing import Callable

from AoR.creatures import creatures


class LevelController:
    '''
    Handles the main level layouts etc
    '''

    def __init__(self) -> None:
        self.map_layout = [
            ['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o'],
            ['p', 'q', 'r', 's', 't'],
            ['u', 'v', 'w', 'x', 'y']
        ]
        self.starting_location = (2, 2)
        self.level = 1

    def run_room_entry(self, current_location: tuple[int, int]) -> Callable:
        '''
        Runs a local function with the same name as the current room as
        retrieved from `self.map_layout`. Should be called on entry to
        a room

        We first retrieve the memory address of the function from the
        dictionary returned by `globals()`. This contains the global
        namespaces for all the objects for the current Python module,
        and from it we can retrieve the memory addresses of any object
        we like. Here we lookup the call address of the function with
        the same name as the current room, and save it into
        `location_func`. We can then call this like a normal function

        Code stolen from [@sastanin on StackOverflow](https://stackoverflow.com/a/834451/19860022)

        Previously, we ran the below `exec` line to call the function,
        which is ofc very insecure and probably a security concern

        ```python
        exec(f'{self.map_layout[current_location[1]][current_location[0]]}()')
        ```

        So whilst the global lookup probably isn't much better as a
        technical solution - the ideal one would probably be a class or
        smth to dynamically create the functions but that is a bit out
        of the scope for this so we will continue to just lookup the
        function address from our room name (for now at least)
        '''

        location_func = globals()[f'{self.map_layout[current_location[1]][current_location[0]]}']
        return(location_func(obj=self))
        # old: exec(f'{self.map_layout[current_location[1]][current_location[0]]}()')

def a(obj: LevelController):
    print('a has been called')

def b(obj: LevelController):
    bear = creatures.Bear(obj.level)
    print(f'spawned a bear, bear is called {bear}\nfunction is at level {obj.level}')

def c(obj: LevelController):
    print('c has been called')

def d(obj: LevelController):
    print('d has been called')

def e(obj: LevelController):
    print('e has been called')

def f(obj: LevelController):
    print('f has been called')

def g(obj: LevelController):
    print('g has been called')

def h(obj: LevelController):
    print('h has been called')

def i(obj: LevelController):
    print('i has been called')

def j(obj: LevelController):
    print('j has been called')

def k(obj: LevelController):
    print('k has been called')

def l(obj: LevelController):
    print('l has been called')

def m(obj: LevelController):
    print('m has been called')

def n(obj: LevelController):
    print('n has been called')

def o(obj: LevelController):
    print('o has been called')

def p(obj: LevelController):
    print('p has been called')

def q(obj: LevelController):
    print('q has been called')

def r(obj: LevelController):
    print('r has been called')

def s(obj: LevelController):
    print('s has been called')

def t(obj: LevelController):
    print('t has been called')

def u(obj: LevelController):
    print('u has been called')

def v(obj: LevelController):
    print('v has been called')

def w(obj: LevelController):
    print('w has been called')

def x(obj: LevelController):
    print('x has been called')

def y(obj: LevelController):
    print('y has been called')
