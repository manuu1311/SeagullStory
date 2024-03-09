import pygame
from sys import exit
from utils.model_predict import Model
from Screens.mainscreen import mainscreen
from Screens.tutorialscreen import tutorialscreen

#model
model=Model("Game/utils/Model/")
#model=None

pygame.init()
pygame.display.set_caption("The seagull story")
screensize=(456,800)
screen = pygame.display.set_mode(screensize)
logo_path="Game/assets/logo.jpg"
logo_surf=pygame.image.load(logo_path)
pygame.display.set_icon(logo_surf)
clock = pygame.time.Clock()

current_screen = tutorialscreen(*screensize) 

while True:
    screen_change = current_screen.handle_events()
    current_screen.update()
    current_screen.render(screen)
    clock.tick(60)
    pygame.display.update()
    # Switch screens based on return value from handle_events
    if screen_change == "quit":
        pygame.quit()
        exit()