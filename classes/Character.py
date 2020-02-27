# Import modules
import pygame
import os
import sys

# initialize pygame
pygame.init()

# Import packages modules 
from constants import *


class Character:
    """ class to create characters macgyver and guardian"""

    def __init__(self, x, y, imagemc, lab):
        self.imagemc = imagemc  # Image of character in the terminal 'M' or 'G'
        self.x = x              # Position of the character in the 2d list column
        self.y = y              # Position of the character in the 2d list row
        self.lab = lab          # Instance of the maze
        self.lab.map[self.y][self.x] = self.imagemc #  Character sprite in the 2D list
        self.score_value = 0    # Initialize score objects collected
        self.text = ''

    def deplacement(self, c, l):  
        """Indicates if the movement of the character is authorized or not.
        l: position of the character on the lines
        c: position of the character on the columns and calculate new position in the 2D list"""
        # Maze size
        n_cols = NS  
        n_lignes = NS  
        # Test if the movement leads MacGyver outside the area
        # of games
        if l < 0 or c < 0 or l > (n_lignes - 1) or \
                c > (n_cols - 1):
            # The symbol \ indicates that the line is not finished
            print("Déplacement impossible")
            self.lab.map[self.y][self.x] = self.imagemc
        
        # Test if MacGyver collides with wall
        elif self.lab.map[l][c] == "X":
            print("Déplacement impossible")
            self.lab.map[self.y][self.x] = self.imagemc
        
        # Test if MacGyver position is same as object 
        elif self.lab.map[l][c] == image_needle or self.lab.map[l][c] == image_ether or \
                self.lab.map[l][c] == image_tube:
            self.score_value += 1
            self.x = c
            self.y = l
            self.lab.map[self.y][self.x] = self.imagemc
            print("nombre objets collectés est {}".format(self.score_value))
        
        # MacGyver arrives end of Maze and did not collect all objects => game over
        elif self.lab.map[l][c] == image_guardian and self.score_value < 3:
            print("Partie perdue")
            self.text = "Perdu!" 

        # MacGyver arrives end of Maze and did collect all objects => win
        elif self.lab.map[l][c] == image_guardian and self.score_value == 3:
            print("Partie gagnée")
            self.text = "Gagné!"
        
        # Move MacGyver to next sprite
        else:
            self.x = c
            self.y = l
            self.lab.map[self.y][self.x] = self.imagemc

    def remove_old_character_position(self):
        """ method to remove previous character position from the 2D list"""
        self.lab.map[0][0] = image_ground  # Remove initial MacGyver postion 
        self.lab.map[self.y][self.x] = image_ground  # Remove previous MacGyver position

    def player_choice(self, event):  
        """ Ask the player to enter its movement and check if it's possible.
        If not display a message, otherwise change the position of the character
        in maze""" 
        if event.key == pygame.K_UP:
            self.deplacement(self.x, self.y - 1)
        elif event.key == pygame.K_DOWN:
            self.deplacement(self.x, self.y + 1)
        elif event.key == pygame.K_LEFT:
            self.deplacement(self.x - 1, self.y)
        elif event.key == pygame.K_RIGHT:
            self.deplacement(self.x + 1, self.y)
        elif event.key == pygame.K_ESCAPE:
            os._exit(1)