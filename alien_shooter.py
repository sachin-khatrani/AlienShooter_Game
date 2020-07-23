import sys
import pygame
from pygame.sprite import Group

#import file
from settings import Settings
from ship import Ship
import game_functions as gf
from game_state import GameStat
from button import Button
from scoreboard import Scoreboard

#from alien import Alien
def start_game():

    #create settings object
    settings = Settings()
    pygame.init()


    #instanse of gamestat
    stats = GameStat(settings)

    #create scren object & set screen size and display title and background color
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Alien Shooter")

    #make ship object
    ship = Ship(settings,screen)

    #create group of bullets
    bullets = Group()

    #create group of aliens
    aliens = Group()

    #create button instance
    play_button = Button(settings, screen, "Play")

    #create scoreboard instance
    scoreboard = Scoreboard(settings, screen, stats,ship)

    gf.create_fleet(settings,screen,aliens,ship)

    #start the loop for game
    while(True):

        #detect user event
        gf.check_events(settings,screen,bullets,ship,play_button,stats,aliens,scoreboard)

        if(stats.gamestatus):
            
            ship.update_position()
            
            gf.delete_bullets(settings,screen,ship,aliens,bullets,stats,scoreboard)

            #update alien position every time 
            gf.update_aliens(settings,aliens,ship,stats,screen,bullets,scoreboard)

            #remove bullets when bullets touch on upper egdges
            gf.remove_bullets(bullets)
            
        gf.update_screen(settings,screen,bullets,ship,aliens,play_button,stats,scoreboard)
        
start_game()

        

