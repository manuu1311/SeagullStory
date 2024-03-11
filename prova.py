import pygame

path="Game/assets/tutorialscreen/"

pygame.init()
pygame.display.set_caption("The seagull story")
screensize=(456,800)
screen = pygame.display.set_mode(screensize)

def DrawBar(pos, size, borderC, barC, progress, screen):
    ysize=size[1]
    pygame.draw.rect(screen, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+3, (pos[1]-3)+ysize*(1-progress))
    innerSize = ((size[0]-6), (ysize-6)*progress)
    pygame.draw.rect(screen, barC, (*innerPos, *innerSize))


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

length=400


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill((0,0,0))
    #background
    screen.blit(pier_surf,(0,0))
    DrawBar((380,150),(25,400),(0,0,0),(200,30,20),1/7,screen)

    clock.tick(60)
    pygame.display.update()

