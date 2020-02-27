# Import modules
import pygame

# initialize pygame
pygame.init()

# Import packages modules 
from constants import *
from classes.Character import * 


class Maze:
    """class to create the maze"""

    def __init__(self, file, windowSurface):

        self.file = file                    # Name of the txt file in which the maze is designed
        self.map = []                       # Empty 2D list
        self.windowSurface = windowSurface  # Window surface defined in module constants
        
    def gen(self):
        """ method to build the maze"""
        with open(self.file, "r") as file1:  # Open file read mode and renamed it
            structure_level = []  # Creating empty list

            # Reading the lines in file
            for line in file1:  # Browse lines that are in the file, in txt file each line = character string
                line_of_level = []  # for each line

                # Reading every letters in file
                for sprite in line:  # For each character in the line
                    # Ignoring the last sprite to continue with the next line

                    if sprite != '\n':  # If character is different of line break
                        # Adding every character to the array
                        # Add all the character of the line except the line break
                        line_of_level.append(sprite)
                        # Find and replace '0' by ' ' -  list comprehension 
                        line_of_level = [' ' if x ==
                                         '0' else x for x in line_of_level]
                        # Find and replace 'm' by 'X' - list comprehension 
                        line_of_level = ['X' if x ==
                                         'm' else x for x in line_of_level]

                # Adding every lines to the array
                structure_level.append(line_of_level)

            # Then the method save the entire structure of the level
            self.map = structure_level  # Structure level is passed in the instance property


    def display(self, map):
        """method to display the maze in the window"""
        for i, line in enumerate(self.map):  # Want to find the index of all occurrences in 2d list
            for j, cell in enumerate(line): 
                if cell in liste_image:
                    self.windowSurface.blit(liste_imageb[liste_image.index(cell)], 
                    (j * W_SPRITE, i * W_SPRITE)) # calculate sprites position in pixel
        pygame.display.flip()