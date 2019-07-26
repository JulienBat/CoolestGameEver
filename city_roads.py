"""
Program by Julien BATAILLE

Released under the GNU General Public License

Module for managing platforms.
"""
import pygame, os

import utils

ONE = "13.png"
TWO = "15.png"

class Road(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, img, lvl):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)
        
        # Grab the image for this platform
        self.image,self.rect = utils.load_png_road(img)
        
        self.level = lvl

    def get_level(self):
        return self.level
