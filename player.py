"""
Program by Julien BATAILLE

Released under the GNU General Public License

This module is used to hold the Player class. The Player represents the user-controlled sprite on the screen.
"""
import pygame, os

import constants
import utils

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
from hitbox import Hitbox

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right of our player
    idle_frames_l = []
    idle_frames_r = []
    walking_frames_l = []
    walking_frames_r = []
    
    # Frame to show
    frame = 0
    frame_speed = 12

    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet(os.path.join("ressources","images","player","sprite-sheet.png"))
        
        # Load all the idle images right
        image = sprite_sheet.get_image(0, 0, 50, 37)
        self.idle_frames_r.append(image)
        image = sprite_sheet.get_image(50, 0, 50, 37)
        self.idle_frames_r.append(image)
        image = sprite_sheet.get_image(100, 0, 50, 37)
        self.idle_frames_r.append(image)
        image = sprite_sheet.get_image(150, 0, 50, 37)
        self.idle_frames_r.append(image)
        image = sprite_sheet.get_image(0, 0, 50, 37)
        self.idle_frames_r.append(image)
        image = sprite_sheet.get_image(50, 0, 50, 37)
        self.idle_frames_r.append(image)
        image = sprite_sheet.get_image(100, 0, 50, 37)
        self.idle_frames_r.append(image)
        image = sprite_sheet.get_image(150, 0, 50, 37)
        self.idle_frames_r.append(image)
        
        # Load all the idle images left
        image = sprite_sheet.get_image(0, 0, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)
        image = sprite_sheet.get_image(50, 0, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)
        image = sprite_sheet.get_image(100, 0, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)
        image = sprite_sheet.get_image(150, 0, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)
        image = sprite_sheet.get_image(0, 0, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)
        image = sprite_sheet.get_image(50, 0, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)
        image = sprite_sheet.get_image(100, 0, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)
        image = sprite_sheet.get_image(150, 0, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)
        
        # Load all the right facing images
        image = sprite_sheet.get_image(0, 37, 50, 37)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(50, 37, 50, 37)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(100, 37, 50, 37)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(150, 37, 50, 37)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(200, 37, 50, 37)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(250, 37, 50, 37)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(300, 37, 50, 37)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(350, 37, 50, 37)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them to face left.
        image = sprite_sheet.get_image(0, 37, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(50, 37, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(100, 37, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(150, 37, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(200, 37, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(250, 37, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(300, 37, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(350, 37, 50, 37)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        
        """for i in range(8):
            self.idle_frames_l[i].scroll(-16,-5)
            self.idle_frames_r[i].scroll(-16,-5)
            self.walking_frames_l[i].scroll(-16,-5)
            self.walking_frames_r[i].scroll(-16,-5)"""

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect() #rect size: 50,37
        #self.rect.size = (20,30)
        
        self.diff_x=15
        self.diff_y=3
        self.hitbox = Hitbox(20,31,self.rect.x+self.diff_x,self.rect.y+self.diff_y)
        #self.hitbox_rect = pygame.Rect(self.rect.x+self.diff_x,self.rect.y+self.diff_y,20,31) #difference: 15,3
        self.hitbox_rect = self.hitbox.get_rect()

    def update(self):
        """ Move the player. """
        
        self.hitbox_rect = self.hitbox.get_rect()
        
        # Gravity
        self.calc_grav()

        # Move left/right
        #self.rect.x += self.change_x
        self.hitbox_rect.x += self.change_x
        """pos = self.hitbox_rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]"""
        self.frame=self.frame+1
        if self.frame>=8*8:
            self.frame=0
        if self.change_x!=0:
            if self.direction == "R":
                self.image = self.walking_frames_r[self.frame//self.frame_speed]
            else:
                self.image = self.walking_frames_l[self.frame//self.frame_speed]
        else:
            if self.direction == "R":
                self.image = self.idle_frames_r[self.frame//self.frame_speed]
            else:
                self.image = self.idle_frames_l[self.frame//self.frame_speed]

        # See if we hit anything
        self.hitbox.update_pos(self.hitbox_rect.x,self.hitbox_rect.y)
        block_hit_list = pygame.sprite.spritecollide(self.hitbox, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                #self.rect.right = block.rect.left-self.diff_x
                self.hitbox_rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                #self.rect.left = block.rect.right+self.diff_x
                self.hitbox_rect.left = block.rect.right

        # Move up/down
        #self.rect.y += self.change_y
        self.hitbox_rect.y += self.change_y

        # Check and see if we hit anything
        self.hitbox.update_pos(self.hitbox_rect.x,self.hitbox_rect.y)
        block_hit_list = pygame.sprite.spritecollide(self.hitbox, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                #self.rect.bottom = block.rect.top-self.diff_y
                self.hitbox_rect.bottom = block.rect.top
            elif self.change_y < 0:
                #self.rect.top = block.rect.bottom+self.diff_y
                self.hitbox_rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                #self.rect.x += block.change_x
                self.hitbox_rect.x += block.change_x
        
        # Update image
        self.rect.x=self.hitbox_rect.x-self.diff_x
        self.rect.y=self.hitbox_rect.y-self.diff_y
        self.hitbox.update_pos(self.hitbox_rect.x,self.hitbox_rect.y)

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.hitbox_rect.y >= constants.SCREEN_HEIGHT - self.hitbox_rect.height and self.change_y >= 0:
            self.change_y = 0
            self.hitbox_rect.y = constants.SCREEN_HEIGHT - self.hitbox_rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.hitbox_rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self.hitbox, self.level.platform_list, False)
        self.hitbox_rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.hitbox_rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        
    def set_hitbox(self):
        self.hitbox.update_pos(self.rect.x+self.diff_x,self.rect.y+self.diff_y)
