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
import csv

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
    
def load_png_edit_icon(name):
    #Charge une image et retourne un objet image
    fullname = os.path.join("ressources","images","edit_icons",name)
    image = pygame.image.load(fullname)
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()
    return image, image.get_rect()
    
def load_level(name):
    s_name = os.path.join("levels",name+".s")
    p_name = os.path.join("levels",name+".p")
    s_file = open(s_name)
    p_file = open(p_name)
    sur = []
    pla = []
    s_csv = csv.reader(s_file, delimiter=',')
    p_csv = csv.reader(p_file, delimiter=',')
    for s in s_csv:
        #sur.append([s[0],s[1],s[2]])
        sur.append(s)
    for p in p_csv:
        #pla.append([p[0],p[1],p[2]])
        pla.append(p)
    return sur,pla
    
    
























