import pygame
from sys import exit
from Game.utils.api_predict import api_predict
from Game.utils.model_predict import Model
from Game.Screens.mainscreen import mainscreen
from Game.Screens.tutorialscreen import tutorialscreen
from Game.Screens.characterscreen import characterscreen
from Game.Screens.winscreen import winscreen
from Game.utils.info_helper import info_helper

#model
model=Model("Game/utils/Model/")
#model=None
api=api_predict()
info=info_helper()

pygame.init()
pygame.display.set_caption("The seagull story")
screensize=(456,800)
screen = pygame.display.set_mode(screensize)
logo_path="Game/assets/logo.jpg"
logo_surf=pygame.image.load(logo_path)
pygame.display.set_icon(logo_surf)
clock = pygame.time.Clock()


tutscreen = tutorialscreen(*screensize) 
mscreen=mainscreen(*screensize,model,api,info)
charscreen=characterscreen(*screensize,model,info)
win=winscreen(*screensize)
current_screen = tutscreen 

#current_screen=winscreen

while True:
    current_screen.handle_events()
  # Switch screens based on return value from handle_events
    screen_change = current_screen.update()
    if screen_change=='mainscreen':
        current_screen=mscreen
        current_screen.reset_state()
    elif screen_change=='characters':
        current_screen=charscreen
        current_screen.reset()
    elif screen_change=='win':
        current_screen=win
    elif screen_change == "quit":
        pygame.quit()
        exit()
    current_screen.render(screen)
    clock.tick(60)
    pygame.display.update()