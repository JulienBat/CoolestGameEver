"""
Program by Julien BATAILLE

Released under the GNU General Public License

Module containing all levels.
"""

import pygame

import constants
import platforms
import utils

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000
    bg_shift_speed = 3
    next_city = 0
    preced_city = 0

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """
        
        # Get the size of the background
        bg_x,bg_y = self.background.get_rect().size
        
        # Get the position of the background
        bg_pos = (self.world_shift // self.bg_shift_speed)
        bg_pos=bg_pos-((bg_pos//bg_x)*bg_x)

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(bg_pos-bg_x,0))
        screen.blit(self.background,(bg_pos,0))
        if bg_x<constants.SCREEN_WIDTH:
            screen.blit(self.background,(bg_pos+bg_x,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            
    def get_next_city(self):
        return self.next_city
        
    def get_preced_city(self):
        return self.preced_city
        
    def is_end_level(self):
        a = self.world_shift < self.level_limit
        return a
        
    def is_begin_level(self):
        b = self.world_shift > 0
        return b

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = utils.load_png_bg("BG.png")
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2000
        self.next_city = 0
        self.preced_city = 0

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 500, 600],
                  [platforms.GRASS_MIDDLE, 628, 600],
                  [platforms.GRASS_RIGHT, 756, 600],
                  [platforms.GRASS_LEFT, 950, 550],
                  [platforms.GRASS_MIDDLE, 1078, 550],
                  [platforms.GRASS_RIGHT, 1206, 550],
                  [platforms.GRASS_LEFT, 1400, 450],
                  [platforms.GRASS_MIDDLE, 1528, 450],
                  [platforms.GRASS_RIGHT, 1656, 450],
                  [platforms.TOP_GRASS_LEFT, 1750, 320],
                  [platforms.TOP_GRASS_MIDDLE, 1878, 320],
                  [platforms.TOP_GRASS_RIGHT, 2006, 320],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        
        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.GRASS_LEFT)
        block.rect.x = 2100
        block.rect.y = 280
        block.boundary_left = 2100
        block.boundary_right = 2400
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.GRASS_MIDDLE)
        block.rect.x = 2228
        block.rect.y = 280
        block.boundary_left = 2228
        block.boundary_right = 2528
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.GRASS_RIGHT)
        block.rect.x = 2356
        block.rect.y = 280
        block.boundary_left = 2356
        block.boundary_right = 2656
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = utils.load_png_bg("BG.png")
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2000
        self.next_city = 0
        self.preced_city = 0

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.TOP_GRASS_LEFT, 500, 600],
                  [platforms.TOP_GRASS_MIDDLE, 628, 600],
                  [platforms.TOP_GRASS_RIGHT, 756, 600],
                  [platforms.GRASS_LEFT, 950, 550],
                  [platforms.GRASS_MIDDLE, 1078, 550],
                  [platforms.GRASS_RIGHT, 1206, 550],
                  [platforms.TOP_GRASS_LEFT, 1400, 450],
                  [platforms.TOP_GRASS_MIDDLE, 1528, 450],
                  [platforms.TOP_GRASS_RIGHT, 1656, 450]
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        

