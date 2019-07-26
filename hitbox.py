"""
Program by Julien BATAILLE

Released under the GNU General Public License

This module is used to hold the hitbox class.
"""
import pygame

import constants
import utils

class Hitbox(pygame.sprite.Sprite):
    """ This class represents the hitbox to manage collisions."""

    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(255,0,0))
        self.rect = self.image.get_rect()
       
        self.rect.x = x
        self.rect.y = y
        
    def update_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
        
    def get_rect(self):
        return self.rect
        
        