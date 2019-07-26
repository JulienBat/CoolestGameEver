"""
Program by Julien BATAILLE

Released under the GNU General Public License

Module containing all cities.
"""

import pygame

import constants
import utils
import city_roads

class City():
    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    level_list = None

    # Background image
    background = None
    
    def __init__(self, player):
        self.player = player
        self.level_list = pygame.sprite.Group()
    
    def update(self):
        self.level_list.update()
        
    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(0,0))

        # Draw all the sprite lists that we have
        self.level_list.draw(screen)

class City_01(City):
    def __init__(self, player):
        City.__init__(self, player)
        
        self.background = utils.load_png_city("city_01.png")
        self.background.set_colorkey(constants.WHITE)

        # Array with type of platform, and x, y location of the platform.
        roads = [ ["level_01.png", 20, 200,(0,"1")],
                  ["level_02.png", 1100, 550,(1,"2")]
                  ]

        # Go through the array above and add platforms
        for road in roads:
            r = city_roads.Road(road[0],road[3])
            r.rect.x = road[1]
            r.rect.y = road[2]
            r.player = self.player
            self.level_list.add(r)
        
