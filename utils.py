"""
Program by Julien BATAILLE

Released under the GNU General Public License
"""


import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

def load_png(name):
    #Charge une image et retourne un objet image
    fullname = os.path.join("ressources","images",name)
    image = pygame.image.load(fullname)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image, image.get_rect()
        
def load_png_bg(name):
    #Charge une image et retourne un objet image
    fullname = os.path.join("ressources","images","backgrounds",name)
    image = pygame.image.load(fullname)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image
        
def load_png_menu(name):
    #Charge une image et retourne un objet image
    fullname = os.path.join("ressources","images","menu",name)
    image = pygame.image.load(fullname)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image        
        
def load_png_city(name):
    #Charge une image et retourne un objet image
    fullname = os.path.join("ressources","images","cities",name)
    image = pygame.image.load(fullname)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image

def load_png_road(name):
    #Charge une image et retourne un objet image
    fullname = os.path.join("ressources","images","roads",name)
    image = pygame.image.load(fullname)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image, image.get_rect()
    
    