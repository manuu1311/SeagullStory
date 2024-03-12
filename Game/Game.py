import pygame
from sys import exit
#from utils.model_predict import Model
from Screens.mainscreen import mainscreen
from Screens.tutorialscreen import tutorialscreen
from Screens.characterscreen import characterscreen
from utils.info_helper import info_helper

#model
#model=Model("Game/utils/Model/")
model=None
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
mscreen=mainscreen(*screensize,model,info)
charscreen=characterscreen(*screensize,model,info)
current_screen = tutscreen 

current_screen=charscreen

while True:
    current_screen.handle_events()
  # Switch screens based on return value from handle_events
    screen_change = current_screen.update()
    if screen_change=='mainscreen':
        current_screen=mscreen
    elif screen_change=='characters':
        current_screen=charscreen
    elif screen_change == "quit":
        pygame.quit()
        exit()
    current_screen.render(screen)
    clock.tick(60)
    pygame.display.update()