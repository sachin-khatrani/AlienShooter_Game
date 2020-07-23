import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,settings,screen):

        super().__init__()
        self.screen = screen
        self.settings = settings
        #load image
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #display ship bottom
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx

        #continuous moving flag
        self.move_right = False
        self.move_left = False

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

    #display image on screen with particualr position
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update_position(self):

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center
    
    #when ship hit then move to center
    def center_ship(self):
        self.center = self.screen_rect.centerx