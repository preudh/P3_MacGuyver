# CONSTANTS - SPRITES AND FILES

# Import modules
import pygame

# initialize pygame
pygame.init()

# Constants - variables
FILE = "file.txt" # File in wgich sprites: d = departure a = arrival m = wall 0 = empty 
NS = 15  # Lines & columns number
WHITE = (255, 255, 255)

# Sprites for characters, objetc, wall,...in the 2D list 
image_ground = ' '
image_tube = 'T'
image_needle = 'A'
image_ether = 'E'
image_guardian = 'G'
image_macgyver = 'M'
image_wall = 'X'
liste_image = [image_ground, image_tube, image_needle, image_ether, image_guardian,
image_macgyver, image_wall]

# Window setting up
W_SPRITE = 30
W_WINDOW = NS * W_SPRITE
WINDOWWITH = W_WINDOW
WINDOWHEIGHT = W_WINDOW
windowSurface = pygame.display.set_mode((W_WINDOW, W_WINDOW))
pygame.display.set_caption('Maze McGyver')

# Loading sprites images - will return a surface in the window
image_groundb = pygame.image.load("images/ground.png")
image_tubeb = pygame.image.load("images/tube_plastique.png")
image_needleb = pygame.image.load("images/aiguille.png")
image_etherb = pygame.image.load("images/ether.png")
image_guardianb = pygame.image.load("images/guardian.png")
image_macgyverb = pygame.image.load("images/macgyver.png")
image_wallb = pygame.image.load("images/wall.png")
liste_imageb = [image_groundb, image_tubeb, image_needleb, image_etherb, image_guardianb,
image_macgyverb, image_wallb]
image_syringe = pygame.image.load("images/syringe.png")

# To show number of objects collected and if game is over or win
font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 20)
TEXTX = 8*30 # x position of text
TEXTY = 12*30 # y position of text
