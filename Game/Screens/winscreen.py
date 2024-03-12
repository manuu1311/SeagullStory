import pygame

class winscreen:
    def __init__(self,width,height):
        self.WIDTH=width
        self.HEIGHT=height
        self.path="Game/assets/winscreen/"
        self.response_state=None

        #    BACKGROUND IMAGES
        self.background_surf=pygame.image.load(self.path+"win.jpg").convert_alpha()
        #self.background_surf = pygame.transform.scale(self.pier_surf, (self.WIDTH,self.HEIGHT))
        self.background_rect=self.background_surf.get_rect(center=(self.WIDTH/2,self.HEIGHT/2))

    
    def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.response_state= 'quit'
                            
                
    def update(self):
        # Update screen
        return self.response_state
    
    def render(self, screen):
        screen.fill((0,0,0))
        #background
        screen.blit(self.background_surf,self.background_rect)