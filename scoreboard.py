import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard():

    def __init__(self,settings,screen,stats,ship):
        
        self.screen = screen

        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.ships = ship

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    #set score with updated value
    def prep_score(self):

        rounded_score = int(round(self.stats.score, -1))
        score = "{:,}".format(rounded_score)

        self.score_image =  self.font.render(score, True, self.text_color,self.settings.bg_color)

        #dimension of score
        self.scorerect = self.score_image.get_rect()
        self.scorerect.right = self.screen_rect.right - 20
        self.scorerect.top = 20

    #highscore display
    def prep_high_score(self):

        rounded_score = int(round(self.stats.high_score, -1))
        high_score = "{:,}".format(rounded_score)

        self.high_score_image =  self.font.render(high_score, True, self.text_color,self.settings.bg_color)

        #dimension of score
        self.highscorerect = self.high_score_image.get_rect()
        self.highscorerect.centerx = self.screen_rect.centerx
        self.highscorerect.top = self.screen_rect.top

    #level display
    def prep_level(self):

        self.level_image =  self.font.render(str(self.stats.level), True, self.text_color,self.settings.bg_color)

        #dimension of score
        self.levelrect = self.level_image.get_rect()
        self.levelrect.right = self.screen_rect.right - 20
        self.levelrect.top = self.scorerect.bottom + 10

    #draw remaining ship
    def prep_ship(self):

        self.ships = Group()

        for ship_count in range(self.stats.ships_left):

            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + ship_count*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def draw_score(self):

        self.screen.blit(self.score_image,self.scorerect)
        self.screen.blit(self.high_score_image,self.highscorerect)
        self.screen.blit(self.level_image,self.levelrect)
        self.ships.draw(self.screen)