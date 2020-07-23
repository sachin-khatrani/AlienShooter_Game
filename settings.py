class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (27, 56, 105)


        #ship settings
        self.ship_limit = 3


        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 10

        #alien setting
        self.alien_drop_speed =  10
        self.alien_point = 20
       
        #speed of game level by level
        self.speedup_factor = 1.1
        self.score_increase_factor = 1.4
        self.reset_settings()

    def reset_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_point = 20

        #right = 1 left = -1
        self.alien_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_factor
        self.bullet_speed_factor *= self.speedup_factor
        self.alien_speed_factor *= self.speedup_factor
        self.alien_point = int(self.alien_point*self.score_increase_factor)

        
