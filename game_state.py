import pygame

class GameStat():

    def __init__(self,settings):

        self.settings = settings

        #check gam eactive or not
        self.gamestatus = False
        self.high_score = 0
        self.resetstat()

    #reset settings when game end
    def resetstat(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
