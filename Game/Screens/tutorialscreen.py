import pygame

class tutorialscreen:
    def __init__(self,width,height):
        self.WIDTH=width
        self.HEIGHT=height
        self.path="Game/assets/tutorialscreen/"
        self.sequence=self.go_next()
        self.response_state=None

        #    BACKGROUND IMAGES
        self.pier_surf=pygame.image.load(self.path+"pier.jpg").convert_alpha()
        self.pier_surf = pygame.transform.scale(self.pier_surf, (self.WIDTH,self.HEIGHT))
        self.rest_surf=pygame.image.load(self.path+"restaurant.jpg").convert_alpha()
        self.rest_surf = pygame.transform.scale(self.rest_surf, (self.WIDTH,self.HEIGHT))
        self.waiter_surf=pygame.image.load(self.path+"waiter.jpg").convert_alpha()
        self.waiter_surf = pygame.transform.scale(self.waiter_surf, (self.WIDTH,self.HEIGHT))

        self.background_surf=self.pier_surf

        #    TEXT PART
        self.text_flag=False
        self.text_lines=[]
        self.font=pygame.font.Font(None, 36)

        borderx=25
        bordery=40
        self.text_rect=pygame.Rect(borderx,bordery,self.WIDTH-borderx*2,self.HEIGHT-bordery*2)
        self.text_surf = pygame.Surface((self.WIDTH-borderx*2,self.HEIGHT-bordery*2))  # the size of your rect
        self.text_surf.fill((100,100,100))
        self.text_surf.set_alpha(128)
        self.reset()

        self.to_fade=[self.background_surf]

    
    def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.response_state= 'quit'
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if self.timer>0:
                        self.timer=1
                    else:
                        if self.text_flag:
                            self.fader=self.faderbwd
                            self.timer=255
                        elif self.fader==self.faderfwd:
                            self.text_flag=True
                            self.sequence.__next__()
                            
                
    def update(self):
        # Update screen
        self.fader()
        return self.response_state
    
    def render(self, screen):
        screen.fill((0,0,0))
        #background
        screen.blit(self.background_surf,(0,0))
        if self.text_flag:
            #screen.blit(self.text_surf,self.text_rect)
            for i, text in enumerate(self.rendered_text):
                #text.set_alpha(200)
                border=40
                screen.blit(text, (self.text_rect.x+3,self.text_rect.y+5+i*border))
    
    def faderfwd(self):
        if self.timer>0:
            self.timer-=3
            self.background_surf.set_alpha(255-self.timer)

    def faderbwd(self):
        if self.timer>0:
            self.timer-=3
            for faded in self.to_fade:
                faded.set_alpha(self.timer)
        else:
            try:
                self.sequence.__next__()
                self.background_surf.set_alpha(0)
            except:
                self.response_state= 'mainscreen'
    
    def reset(self):
        self.timer=255
        self.fader=self.faderfwd

    def go_next(self):
        #first passage
        text_lines = ["Albert and Dave are at a pier."]
        self.rendered_text = [self.font.render(line, True, (255, 255, 255)) for line in text_lines]
        self.to_fade=[self.background_surf,self.text_surf, *self.rendered_text]
        yield
        #second image
        self.text_flag=False
        self.text_surf.set_alpha(0)
        self.background_surf=self.rest_surf
        self.fader=self.faderfwd
        self.timer=255
        yield
        #second passage
        text_lines = ["Together, they go to a restaurant."]
        self.rendered_text = [self.font.render(line, True, (255, 255, 255)) for line in text_lines]
        self.to_fade=[self.background_surf,self.text_surf, *self.rendered_text]
        yield
        self.text_flag=False
        #third image
        self.background_surf=self.waiter_surf
        self.fader=self.faderfwd
        self.timer=255
        yield
        #third passage
        text_lines = ["Albert orders seagull meat.","The waiter brings him.","He takes a bite and suddenly ","ends his life."]
        self.rendered_text = [self.font.render(line, True, (0, 0, 0)) for line in text_lines]
        self.to_fade=[self.background_surf,self.text_surf, *self.rendered_text]
        yield
        #TODO: add small tutorial
