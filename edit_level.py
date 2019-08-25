#!/usr/bin/env python
# coding: utf-8
"""
Program by Julien BATAILLE

Released under the GNU General Public License

Sources:
http://programarcadegames.com/python_examples/sprite_sheets/
https://www.gameart2d.com/free-platformer-game-tileset.html
http://gaurav.munjal.us/Universal-LPC-Spritesheet-Character-Generator/#
https://itch.io/game-assets/free/tag-2d
"""

VERSION = "0.0.1"

import pygame

import constants
import utils
import cities
import platforms
import edit_sprites

from player import Player

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    surroundings_list = None
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
        self.surroundings_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.surroundings_list.update()
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
        self.surroundings_list.draw(screen)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for surrounding in self.surroundings_list:
            surrounding.rect.x += shift_x

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
class Level_edition(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = utils.load_png_bg("BG.png")
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -10000
        self.next_city = 0
        self.preced_city = 0

def format_to_csv(platform_list):
    csv = ""
    for p in platform_list:
        csv=csv+p.name+","+str(p.real_x)+","+str(p.rect.y)+"\n"
    return csv

def main():
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT+210]
    screen = pygame.display.set_mode(size)
    if constants.FULLSCREEN:
        screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

    pygame.display.set_caption("Level Edition Console")
    
    edit_bg = pygame.Surface([constants.SCREEN_WIDTH,210])
    edit_bg.fill(constants.BLACK)
            
    #level_platforms = pygame.sprite.Group()
    
    actual_sprite = platforms.Platform_edit("X64_TOP_GRASS_MIDDLE")
    
    edit_icons = [["64_1.png","X64_TOP_GRASS_LEFT"],
                  ["64_2.png","X64_TOP_GRASS_MIDDLE"],
                  ["64_3.png","X64_TOP_GRASS_RIGHT"],
                  ["64_4.png","X64_MIDDLE_GRASS_LEFT"],
                  ["64_5.png","X64_MIDDLE_GRASS_MIDDLE"],
                  ["64_6.png","X64_MIDDLE_GRASS_RIGHT"],
                  ["64_7.png","X64_BOTTOM_GRASS_LEFT"],
                  ["64_8.png","X64_BOTTOM_GRASS_MIDDLE"],
                  ["64_9.png","X64_BOTTOM_GRASS_RIGHT"],
                  ["64_10.png","X64_GO_UP_GRASS_LEFT"],
                  ["64_11.png","X64_GO_DOWN_GRASS_LEFT"],
                  ["64_12.png","X64_GO_DOWN_GRASS_RIGHT"],
                  ["64_13.png","X64_GO_UP_GRASS_RIGHT"],
                  ["64_1.png","X128_TOP_GRASS_LEFT"],
                  ["64_2.png","X128_TOP_GRASS_MIDDLE"],
                  ["64_3.png","X128_TOP_GRASS_RIGHT"],
                  ["64_4.png","X128_MIDDLE_GRASS_LEFT"],
                  ["64_5.png","X128_MIDDLE_GRASS_MIDDLE"],
                  ["64_6.png","X128_MIDDLE_GRASS_RIGHT"],
                  ["64_7.png","X128_BOTTOM_GRASS_LEFT"],
                  ["64_8.png","X128_BOTTOM_GRASS_MIDDLE"],
                  ["64_9.png","X128_BOTTOM_GRASS_RIGHT"],
                  ["64_10.png","X128_GO_UP_GRASS_LEFT"],
                  ["64_11.png","X128_GO_DOWN_GRASS_LEFT"],
                  ["64_12.png","X128_GO_DOWN_GRASS_RIGHT"],
                  ["64_13.png","X128_GO_UP_GRASS_RIGHT"]]
                  
    edit_icons_surrounding = [["64_tree1.png","X64_TREE_1"]]
    
    icon_list = pygame.sprite.Group()
    edit_x = 0
    edit_y = constants.SCREEN_HEIGHT+10
    for i in edit_icons:
        e = edit_sprites.Icon(i[0],i[1],(edit_x,edit_y))
        icon_list.add(e)
        edit_x+=50
        if edit_x > (constants.SCREEN_WIDTH-50):
            edit_y+=50
            edit_x=0

    # Create the player
    player = Player()

    # Set the current level
    current_level = Level_edition(player)

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.hitbox_rect.height
    player.set_hitbox()
    active_sprite_list.add(player)
    player.stop()

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a: #left / q (french)
                    player.go_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # right / d (french)
                    player.go_right()
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE: # up / space
                    player.jump()
                if event.key == pygame.K_z: # w (french)
                    print(format_to_csv(current_level.platform_list))

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player.change_x < 0:
                    player.stop()
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player.change_x > 0:
                    player.stop()
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for i in icon_list:
                    if i.rect.collidepoint(pos):
                        actual_sprite=platforms.Platform_edit(i.name)
                        print("selected: "+i.name)
                if pos[1] < constants.SCREEN_HEIGHT:
                    #p = platforms.Platform(platforms.plat_dict[actual_sprite.name])
                    p = platforms.Platform_edit(actual_sprite.name)
                    p.rect.x = actual_sprite.rect.x
                    p.real_x = p.rect.x - current_level.world_shift
                    p.rect.y = actual_sprite.rect.y
                    current_level.platform_list.add(p)
                    

        # Update the editing sprite
        pos = pygame.mouse.get_pos()
        actual_sprite.rect.x=64*(pos[0]//64)
        actual_sprite.rect.y=64*(pos[1]//64)+(constants.SCREEN_HEIGHT%64)
        
        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.hitbox.rect.x >= (constants.SCREEN_WIDTH-400) and not current_level.is_end_level():
            diff = player.hitbox.rect.x - (constants.SCREEN_WIDTH-400)
            player.hitbox.rect.x = (constants.SCREEN_WIDTH-400)
            current_level.shift_world(-diff)
            for p in current_level.platform_list:
                p.rect.x -= diff

        # If the player gets near the left side, shift the world right (+x)
        if player.hitbox.rect.x <= 300 and not current_level.is_begin_level():
            diff = 300 - player.hitbox.rect.x
            player.hitbox.rect.x = 300
            current_level.shift_world(diff)
            for p in current_level.platform_list:
                p.rect.x += diff

        # If the player gets to the end of the level, go to the next level
        #current_position = player.hitbox.rect.x + current_level.world_shift
        #if current_position < current_level.level_limit:
        if player.hitbox.rect.x > constants.SCREEN_WIDTH:
            #player.hitbox.rect.x = 300
            done = True
            load_city(player,current_level.get_next_city())
            
        if current_level.player.hitbox.rect.x < 0:
            #player.hitbox.rect.x = 300
            done = True
            load_city(player,current_level.get_preced_city())

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        current_level.platform_list.draw(screen)
        
        #Editing
        screen.blit(edit_bg,(0,constants.SCREEN_HEIGHT))
        #screen.blit(edit_x64_tree_1,edit_x64_tree_1_pos)
        icon_list.draw(screen)
        screen.blit(actual_sprite.image,actual_sprite.rect)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 90 frames per second
        clock.tick(constants.GAME_SPEED)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
