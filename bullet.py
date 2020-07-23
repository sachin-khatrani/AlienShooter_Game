import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,settings,screen,ship):

        super().__init__()
        self.screen = screen

        #set bullet with its dimension and correct position
        self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        #speed factor and color
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):

        #update the decima position of bullet
        self.y -= self.speed_factor
        #update rect position
        self.rect.y = self.y

    def draw_bullet_on_screen(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


        