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


import os
import sys
from time import sleep

from AoR import level_dat


def startup() -> str:
    '''
    Prints title art, loads map data and stores the username
    '''
    
    title_art = [
        '                               _ _            __   _____           _   _ _         _   _             ',
        '     /\\                       | | |          / _| |  __ \\         | | (_) |       | | (_)            ',
        '    /  \\   ___ ___  __ _ _   _| | |_    ___ | |_  | |__) |___  ___| |_ _| |_ _   _| |_ _  ___  _ __  ',
        '   / /\\ \\ / __/ __|/ _` | | | | | __|  / _ \\|  _| |  _  // _ \\/ __| __| | __| | | | __| |/ _ \\| \'_ \\ ',
        '  / ____ \\\\__ \\__ \\ (_| | |_| | | |_  | (_) | |   | | \\ \\  __/\\__ \\ |_| | |_| |_| | |_| | (_) | | | |',
        ' /_/    \_\\___/___/\\__,_|\\__,_|_|\\__|  \\___/|_|   |_|  \\_\\___||___/\\__|_|\\__|\\__,_|\\__|_|\\___/|_| |_|'
    ]
    # note: ascii art^^
    for line in title_art: 
        print(line)
        sleep(0.5)
    print('\n')

    username = input('What shall we call you, explorer?\n >\t')
    print(f'Welcome to Assault of Restitution, {username}')

    return username

def load_map_module(module_name: str) -> object:
    return getattr(level_dat, f'{module_name}').LevelController()

def calculate_direction_offset(direction: str) -> tuple[int, int]:
    direction = direction.upper()
    # todo: handle names in addition of symbols

    # future: this could be match/case statements
    # but that's only in Python 3.10 so depends on compatibility
    if direction == 'N':
        return 0, 1
    elif direction == 'S':
        return 0, -1
    elif direction == 'E':
        return 1, 0
    elif direction == 'W':
        return -1, 0
    elif direction == 'NE':
        return 1, 1
    elif direction == 'NW':
        return -1, 1
    elif direction == 'SE':
        return 1, -1
    elif direction == 'SW':
        return -1, -1
    else:
        return 0, 0  # todo: actually handle this

def check_borders(current_location: tuple[int, int], x_offset: int, y_offset: int, map_layout: list[list[str]]) -> bool:
    if x_offset != 0:  # note: if we are moving along the x
        if current_location[0] == 0 and x_offset == 1:
            return False
        elif current_location[0] == len(map_layout[0]) - 1 and x_offset == -1:
            return False
    # note: if x movement is okay

    if y_offset != 0:  # note: if we are moving along the y
        if current_location[1] == 0 and y_offset == 1:
            return False
        elif current_location[1] == len(map_layout) - 1 and y_offset == -1:
            return False
    # note: if y movement is okay

    return True

def change_location(current_location: tuple[int, int], x_offset: int, y_offset: int, map_layout: list[list[str]]) -> tuple[tuple[int, int], str]:
    if check_borders(current_location, x_offset, y_offset, map_layout):
        new_location = (
            current_location[0] + x_offset,
            current_location[1] + y_offset*-1  # note: python indices are australian, https://github.com/Cornelius-Figgle/game-test/blob/main/docs/media/a_brief_dictation_on_why_australia_is_australia_and_why_this_affects_the_polarity_of_pythons.png
        )
        return new_location
    else:
        print()
        return current_location  # todo: actually handle this

def main() -> None:
    '''
    The main function that handles passing or args and return values.
    Also handles the application loop and errors from functions - has
    to be called with `current_location` to be able to pass it through
    to `ask_location()`

    In future will run the order of storyline etc
    '''


    username = startup()
    level_obj = load_map_module('level_01')  # note: load the first map

    current_location = level_obj.starting_location

    try:
        while True: # note: infinite loop
            name_of_current_location = level_obj.map_layout[current_location[1]][current_location[0]]
            print(f'\nYou are currently in {name_of_current_location}')
            level_obj.run_room_entry(current_location)

            user_requested_direction = input('Where would you like to go now? ').upper()
            current_location = change_location(
                current_location,
                *calculate_direction_offset(user_requested_direction),
                level_obj.map_layout
            )

            # future: smth happens in that place
    except KeyboardInterrupt: 
        return  # note: `Ctrl+C` to exit app
