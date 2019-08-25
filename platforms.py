"""
Program by Julien BATAILLE

Released under the GNU General Public License

Module for managing platforms.
"""
import pygame, os

import utils

from spritesheet_functions import SpriteSheet


plat_dict = {
    #x64
    "X64_TOP_GRASS_LEFT": os.path.join("tiles","x64","1.png"),
    "X64_TOP_GRASS_MIDDLE": os.path.join("tiles","x64","2.png"),
    "X64_TOP_GRASS_RIGHT": os.path.join("tiles","x64","3.png"),
    "X64_MIDDLE_GRASS_LEFT": os.path.join("tiles","x64","4.png"),
    "X64_MIDDLE_GRASS_MIDDLE": os.path.join("tiles","x64","5.png"),
    "X64_MIDDLE_GRASS_RIGHT": os.path.join("tiles","x64","6.png"),
    "X64_BOTTOM_GRASS_LEFT": os.path.join("tiles","x64","7.png"),
    "X64_BOTTOM_GRASS_MIDDLE": os.path.join("tiles","x64","8.png"),
    "X64_BOTTOM_GRASS_RIGHT": os.path.join("tiles","x64","9.png"),
    "X64_GO_UP_GRASS_LEFT": os.path.join("tiles","x64","10.png"),
    "X64_GO_DOWN_GRASS_LEFT": os.path.join("tiles","x64","11.png"),
    "X64_GO_DOWN_GRASS_RIGHT": os.path.join("tiles","x64","12.png"),
    "X64_GO_UP_GRASS_RIGHT": os.path.join("tiles","x64","13.png"),
    "X64_PLATFORM_GRASS_LEFT": os.path.join("tiles","x64","14.png"),
    "X64_PLATFORM_GRASS_MIDDLE": os.path.join("tiles","x64","15.png"),
    "X64_PLATFORM_GRASS_RIGHT": os.path.join("tiles","x64","16.png"),

    "X64_TOP_WATER": os.path.join("tiles","x64","17.png"),
    "X64_TOP_WATER": os.path.join("tiles","x64","18.png"),

    "X64_BUSH_1": os.path.join("tiles","x64","Bush_1.png"),
    "X64_BUSH_2": os.path.join("tiles","x64","Bush_2.png"),
    "X64_BUSH_3": os.path.join("tiles","x64","Bush_3.png"),
    "X64_BUSH_4": os.path.join("tiles","x64","Bush_4.png"),
    "X64_CRATE": os.path.join("tiles","x64","Crate.png"),
    "X64_MUSHROOM_1": os.path.join("tiles","x64","Mushroom_1.png"),
    "X64_MUSHROOM_2": os.path.join("tiles","x64","Mushroom_2.png"),
    "X64_SIGN_1": os.path.join("tiles","x64","Sign_1.png"),
    "X64_SIGN_LEFT": os.path.join("tiles","x64","Sign_left.png"),
    "X64_SIGN_RIGHT": os.path.join("tiles","x64","Sign_right.png"),
    "X64_STONE": os.path.join("tiles","x64","Stone.png"),
    "X64_TREE_1": os.path.join("tiles","x64","Tree_1.png"),
    "X64_TREE_2": os.path.join("tiles","x64","Tree_2.png"),
    "X64_TREE_3": os.path.join("tiles","x64","Tree_3.png"),

    #x128
    "X128_TOP_GRASS_LEFT": os.path.join("tiles","x128","1.png"),
    "X128_TOP_GRASS_MIDDLE": os.path.join("tiles","x128","2.png"),
    "X128_TOP_GRASS_RIGHT": os.path.join("tiles","x128","3.png"),
    "X128_MIDDLE_GRASS_LEFT": os.path.join("tiles","x128","4.png"),
    "X128_MIDDLE_GRASS_MIDDLE": os.path.join("tiles","x128","5.png"),
    "X128_MIDDLE_GRASS_RIGHT": os.path.join("tiles","x128","6.png"),
    "X128_BOTTOM_GRASS_LEFT": os.path.join("tiles","x128","7.png"),
    "X128_BOTTOM_GRASS_MIDDLE": os.path.join("tiles","x128","8.png"),
    "X128_BOTTOM_GRASS_RIGHT": os.path.join("tiles","x128","9.png"),
    "X128_GO_UP_GRASS_LEFT": os.path.join("tiles","x128","10.png"),
    "X128_GO_DOWN_GRASS_LEFT": os.path.join("tiles","x128","11.png"),
    "X128_GO_DOWN_GRASS_RIGHT": os.path.join("tiles","x128","12.png"),
    "X128_GO_UP_GRASS_RIGHT": os.path.join("tiles","x128","13.png"),
    "X128_PLATFORM_GRASS_LEFT": os.path.join("tiles","x128","14.png"),
    "X128_PLATFORM_GRASS_MIDDLE": os.path.join("tiles","x128","15.png"),
    "X128_PLATFORM_GRASS_RIGHT": os.path.join("tiles","x128","16.png"),

    "X128_TOP_WATER": os.path.join("tiles","x128","17.png"),
    "X128_TOP_WATER": os.path.join("tiles","x128","18.png"),

    "X128_BUSH_1": os.path.join("tiles","x128","Bush_1.png"),
    "X128_BUSH_2": os.path.join("tiles","x128","Bush_2.png"),
    "X128_BUSH_3": os.path.join("tiles","x128","Bush_3.png"),
    "X128_BUSH_4": os.path.join("tiles","x128","Bush_4.png"),
    "X128_CRATE": os.path.join("tiles","x128","Crate.png"),
    "X128_MUSHROOM_1": os.path.join("tiles","x128","Mushroom_1.png"),
    "X128_MUSHROOM_2": os.path.join("tiles","x128","Mushroom_2.png"),
    "X128_SIGN_1": os.path.join("tiles","x128","Sign_1.png"),
    "X128_SIGN_LEFT": os.path.join("tiles","x128","Sign_left.png"),
    "X128_SIGN_RIGHT": os.path.join("tiles","x128","Sign_right.png"),
    "X128_STONE": os.path.join("tiles","x128","Stone.png"),
    "X128_TREE_1": os.path.join("tiles","x128","Tree_1.png"),
    "X128_TREE_2": os.path.join("tiles","x128","Tree_2.png"),
    "X128_TREE_3": os.path.join("tiles","x128","Tree_3.png")
}

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)
        
        # Grab the image for this platform
        self.image,self.rect = utils.load_png(sprite)

class Platform_edit(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)
        
        # Grab the image for this platform
        self.image,self.rect = utils.load_png(plat_dict[sprite])
        self.name = sprite
        self.real_x = 0


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player.hitbox)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.hitbox.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.hitbox.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player.hitbox)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.hitbox.rect.bottom = self.rect.top
            else:
                self.player.hitbox.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
