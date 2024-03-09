import pygame

class tutorialscreen:
    def __init__(self,width,height):
        self.WIDTH=width
        self.HEIGHT=height
        self.path="Game/assets/tutorialscreen/"

        #    BACKGROUND IMAGES
        self.background_surf=pygame.image.load(self.path+"pier.jpg").convert_alpha()
        self.background_surf = pygame.transform.scale(self.background_surf, (self.WIDTH,self.HEIGHT))
        self.dummy=lambda: 0

        self.reset()

    
    def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    self.timer=255
                    self.fader=self.faderbwd
                
    def update(self):
        # Update MainMenu
        self.fader()
        pass

    def render(self, screen):
        screen.fill((0,0,0))
        #background
        screen.blit(self.background_surf,(0,0))
    
    def faderfwd(self):
        if self.timer>0:
            self.timer-=3
        else:
            self.fader=self.dummy
        self.background_surf.set_alpha(255-self.timer)

    def faderbwd(self):
        if self.timer>0:
            self.timer-=3
        else:
            self.fader=self.dummy
        self.background_surf.set_alpha(self.timer)
    
    def reset(self):
        self.timer=255
        self.fader=self.faderfwd