import pygame

path="Game/assets/tutorialscreen/"

pygame.init()
pygame.display.set_caption("The seagull story")
screensize=(456,800)
screen = pygame.display.set_mode(screensize)

#    BACKGROUND IMAGES
pier_surf=pygame.image.load(path+"restaurant.jpg").convert_alpha()
pier_surf = pygame.transform.scale(pier_surf, screensize)

clock = pygame.time.Clock()

borderx=25
bordery=40
rect=pygame.Rect(borderx,bordery,456-borderx*2,800-bordery*2)
s = pygame.Surface((456-borderx*2,800-bordery*2))  # the size of your rect
s.fill((100,100,100))
incr=1
tmp=0

font = pygame.font.Font(None, 36)  # Use default font with size 36
text_lines = ["Text inside", "rectangle with", "multiple lines"]
rendered_text = [font.render(line, True, (255, 255, 255)) for line in text_lines]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((0,0,0))
    #background
    screen.blit(pier_surf,(0,0))
    screen.blit(s,rect)
    s.set_alpha(125)
    for i, text in enumerate(rendered_text):
        text.set_alpha(100)
        border=40
        text_rect = text.get_rect(center=(rect.centerx, rect.top + 30 + i * border))  # Adjust vertical position
        screen.blit(text, (rect.x+3,rect.y+5+i*40))

    clock.tick(60)
    pygame.display.update()

