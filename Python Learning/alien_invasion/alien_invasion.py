#__Author__=Youzhi Gu
#Learn Python at Zhejiang University

import sys
import pygame

from settings import  Settings
from ship import  Ship
#from alien import  Alien
import  game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import  Button

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    play_button= Button(ai_settings,screen,"Play")
    pygame.display.set_caption("Alien Invasion")
    stats=GameStats(ai_settings)
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            gf.update_ship(ship)
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings, screen,stats,ship,aliens,bullets,play_button)

run_game()


