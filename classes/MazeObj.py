# Import modules
import random


# import packages modules 
from constants import *


class MazeObj:
    """ class to create objects"""

    def __init__(self, name, imageobj, labyrinth): 
        self.labyrinthb = labyrinth     # Local maze1
        self.name = name                # Object name
        self.imageobj = imageobj        # Objects' sprite in the 2D list

    def random_position(self):  # self allow access to the variable labyrinthb
        """ method to put objects at random position in the maze"""
        count_max = 1
        count = 0
        while count < count_max:
            x = random.randint(0, (NS - 1))
            y = random.randint(0, (NS - 1))
            #  I modify maze1 - labyrinthb is a copy of maze 1 (instance variable)
            if self.labyrinthb.map[y][x] == ' ':  
                self.labyrinthb.map[y][x] = self.imageobj
                count += 1
                break