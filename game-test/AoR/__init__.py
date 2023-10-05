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
from typing import NoReturn

import AoR.main as AoR


def main() -> NoReturn:
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')  # note: clears the screen
    sys.exit(AoR.main())  # note: starts then application loop