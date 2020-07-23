import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien
#when down key pressed
def check_keydown_events(event,settings,bullets,ship,screen):

    if(event.key == pygame.K_q):
        sys.exit()
    elif(event.key == pygame.K_RIGHT):
        #move ship right
        ship.move_right = True
    elif(event.key == pygame.K_LEFT):
        #move ship left
        ship.move_left = True

    # when spacebar is pressed then we simply create new bullet and add to bullets group
    elif(event.key == pygame.K_SPACE):
        fire_bullet(settings, screen, ship, bullets)
        


#when up key pressed
def check_keyup_events(event,ship):
    
    # when key is not pressed then we set value of right & left flag False
    if(event.key == pygame.K_RIGHT):
        ship.move_right = False
    elif(event.key == pygame.K_LEFT):
        ship.move_left = False

def check_events(settings,screen,bullets,ship,play_button,stats,aliens,scoreboard):

    for event in pygame.event.get():

        
        #if user click on close button then the application will be stopped
        if(event.type == pygame.QUIT):
            sys.exit()
        
        elif(event.type == pygame.KEYDOWN):
            check_keydown_events(event,settings,bullets,ship,screen)

        elif ( event.type == pygame.KEYUP):
            check_keyup_events(event,ship)
            
        elif(event.type == pygame.MOUSEBUTTONDOWN):

            mousex, mousey = pygame.mouse.get_pos()
            
            if(play_button.rect.collidepoint(mousex, mousey) and not stats.gamestatus):

                #reseting speed of all factor
                settings.reset_settings()
                pygame.mouse.set_visible(False)

                #reset statistics
                stats.resetstat()
                stats.gamestatus = True

                scoreboard.prep_score()
                scoreboard.prep_high_score()
                scoreboard.prep_level()
                scoreboard.prep_ship()

                bullets.empty()
                aliens.empty()

                create_fleet(settings, screen,aliens,ship)
                ship.center_ship()
            


            

def update_screen(settings,screen,bullets,ship,aliens,play_button,stats,scoreboard):

    #screen fill with color & display ship & alien
    screen.fill(settings.bg_color)

    #draw ship
    ship.blitme()

    #draw aliens
    for alien in aliens.sprites():
        alien.blitme()

    #draw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet_on_screen()

    #draw score
    scoreboard.draw_score()

    #draw button if gamestatus is false
    if(not stats.gamestatus):
        play_button.draw_button()
    # every time draw new game element with some changes
    pygame.display.flip()

#remove old bullets which leaves from screen
def remove_bullets(bullets):

    bullets.update()
    for bullet in bullets.copy():

        if(bullet.rect.bottom <= 0):
            bullets.remove(bullet)

#create new bullet if limit not reached
def fire_bullet(settings, screen, ship, bullets):

    if(len(bullets) < settings.bullets_allowed):
        bullet = Bullet(settings,screen,ship)
        bullets.add(bullet)


#number of aliens in a one row
def number_of_aliens_in_row(settings,alien_width):
    available_space = settings.screen_width - 3*alien_width
    number_of_aliens = int(available_space/(3*alien_width))

    return number_of_aliens

#get number of rows fit in horizontal
def number_of_row(settings,ship_height,alien_height):

    available_space_hori = settings.screen_height - 3*alien_height - ship_height

    number_of_rows = int(available_space_hori/(4*alien_height))
    return number_of_rows

#create alien and set appropriate dimenssion and add in aliens group
def create_alien(settings,screen,aliens,alien_number,row_number):

    alien = Alien(settings,screen)

    alien_width = alien.rect.width
    alien.x = alien_width + 3*alien_width*alien_number

    alien.y = alien.rect.height + 3 * alien.rect.height * row_number

    alien.rect.x = alien.x
    alien.rect.y = alien.y+100
    aliens.add(alien)

def create_fleet(settings,screen,aliens,ship):

    alien = Alien(settings,screen)
    number_of_aliens = number_of_aliens_in_row(settings,alien.rect.width)    

    number_of_rows = number_of_row(settings,ship.rect.height,alien.rect.height)

    for row in range(number_of_rows):
        for col in range(number_of_aliens):
            create_alien(settings,screen,aliens,col,row)

#update alien position every time 
def update_aliens(settings,aliens,ship,stats,screen,bullets,scoreboard):

    check_fleet_edges(settings,aliens)
    aliens.update()

    #check collision between alien and ship

    if(pygame.sprite.spritecollideany(ship,aliens)):
        ship_hit(settings, stats, screen, ship, aliens, bullets,scoreboard)
    
    #if alien touch with bottom screen then ship is hit
    check_alien_bottom(settings, stats, screen, ship, aliens, bullets,scoreboard)

#check if aliens is touch on left edge or right edges then change direction in decrease speed
def check_fleet_edges(settings,aliens):

    for alien in aliens.sprites():

        if(alien.check_edges()):
            change_fleet_direction(settings,aliens)
            break
    
def change_fleet_direction(settings,aliens):

    for alien in aliens.sprites():
        alien.rect.y += settings.alien_drop_speed


    settings.alien_direction *= -1

#when bullets collision with alien then alien and bullets is disapper and increase score
def delete_bullets(settings,screen,ship,aliens,bullets,stats,scoreboard):

    
    collision_group = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collision_group:

        for alienses in collision_group.values():
            stats.score += settings.alien_point*len(alienses)
            scoreboard.prep_score()
        compare_high_score(stats, scoreboard)
    if(len(aliens) == 0):

        #increase speed each new level
        settings.increase_speed()
        bullets.empty()
        create_fleet(settings,screen,aliens,ship)

        #increase lvl
        stats.level += 1
        scoreboard.prep_level()


def ship_hit(settings, stats, screen, ship, aliens, bullets,scoreboard):

    if stats.ships_left > 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        scoreboard.prep_ship()
        create_fleet(settings,screen,aliens,ship)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.gamestatus = False
        pygame.mouse.set_visible(True)


def check_alien_bottom(settings, stats, screen, ship, aliens, bullets,scoreboard):

    screen_rect = screen.get_rect()

    for alien in aliens.sprites():

        if(alien.rect.bottom >= screen_rect.bottom):
            ship_hit(settings, stats, screen, ship, aliens, bullets,scoreboard)
            break

def compare_high_score(stats,scoreboard):

    if(stats.high_score <  stats.score):
        stats.high_score = stats.score
        scoreboard.prep_high_score()
