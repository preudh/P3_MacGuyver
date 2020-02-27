 #! /usr/bin/env python3
# coding: utf-8

"""Maze games in which MacGyver is trapped. The exit is monitored by a 
guard. To distract him, you need to gather the following objects 
(scattered in the labyrinth): a needle, a plastic tube and ether.
They will allow MacGyver to create a syringe and to sleep the guard."""

# Import modules
import pygame
import sys
import os
import random
import time


# Import packages modules 
from constants import *
from classes.Maze import * 
from classes.MazeObj import *  
from classes.Character import * 
from images import *

# Initialisating of pygame
pygame.init()

# Creation of maze instance
maze1 = Maze(FILE, windowSurface)

# Build maze
maze1.gen()

# Appending instances to Class Character
Mc = Character(0, 0, image_macgyver, maze1)
Gu = Character((NS - 1), (NS - 1), image_guardian, maze1)

# Creating empty objects list for class MazeObj
list_maze_objects = []

# Appending instances to list
list_maze_objects.append(MazeObj('eth', image_ether, maze1))
list_maze_objects.append(MazeObj('aig', image_needle, maze1))
list_maze_objects.append(MazeObj('tub', image_tube, maze1))

# Applied randpos method for instances of the list
for obj in list_maze_objects:
    # Calling method
    obj.random_position()

# Initialisation of maze1 
maze1.display(map)

# Remove initial position of Macgyver x = 0 and y = 0 before 2nd input
Mc.remove_old_character_position()  


def show_score (x,y):
    """ show in the window number objects collected and if game is over or not"""
    score = font.render("Objets collectés : " + str(Mc.score_value), True, (WHITE))
    windowSurface.blit(score, (x, y))
    score2 = font2.render("" + str(Mc.text), True, (WHITE))
    windowSurface.blit(score2, (x , y + 30))
    if Mc.score_value == 3:
        windowSurface.blit(image_syringe, (x + 30*6, y))


# Game loop

def game(lab, Mc, map, textX, textY):

    continuer = True
    while continuer:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                Mc.player_choice(event)
                maze1.display(map)
                Mc.remove_old_character_position()
                show_score(textX, textY)
                pygame.display.update()
            if event.type == pygame.QUIT:
                continuer = False
            #Show Game Over and quit game 
            if Mc.text == "Perdu!": 
                show_score(textX, textY)
                time.sleep(3)
                continuer = False

# Launching game
game(maze1, Mc, map, TEXTX, TEXTY)
