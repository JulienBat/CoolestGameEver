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
import levels
import utils
import cities
import platforms

from player import Player

def main():
    print(platforms.plat_dict)

def load_level(player,current_level_no):
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    if constants.FULLSCREEN:
        screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

    pygame.display.set_caption("This game is so cool OMG :O (level "+str(current_level_no)+")")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # Set the current level
    current_level = level_list[current_level_no]

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
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player.change_x < 0:
                    player.stop()
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.hitbox.rect.x >= (constants.SCREEN_WIDTH-400) and not current_level.is_end_level():
            diff = player.hitbox.rect.x - (constants.SCREEN_WIDTH-400)
            player.hitbox.rect.x = (constants.SCREEN_WIDTH-400)
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.hitbox.rect.x <= 300 and not current_level.is_begin_level():
            diff = 300 - player.hitbox.rect.x
            player.hitbox.rect.x = 300
            current_level.shift_world(diff)

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
