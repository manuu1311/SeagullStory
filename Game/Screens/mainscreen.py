import pygame

class mainscreen:
    def __init__(self,width,height,model):
        self.model=model
        self.background_path="Game/assets/sad.jpg"
        self.WHITE=(255,255,255)
        self.BLACK=(0,0,0)
        self.GREEN=(6,87,2)
        self.WIDTH=width
        self.HEIGHT=height

        #    BACKGROUND IMAGE
        self.background_surf=pygame.image.load(self.background_path).convert_alpha()
        self.background_surf = pygame.transform.scale(self.background_surf, (self.WIDTH,self.HEIGHT))
        self.background_rect=self.background_surf.get_rect(topleft=(0,0))

        #    QUESTION TEXT WIDGET
        self.font = pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(100, 100, 300, 32)
        self.input_box.centerx=self.WIDTH//2
        self.question=''
        self.text=''

        #    SUBMIT BUTTON
        self.submit_box=pygame.Rect(100,150,90, 26)
        self.submit_box.centerx=self.WIDTH//2
        self.submit_text='Submit'

        #    ANSWER FLAG
        self.response_flag=False
        self.response=''
        self.response_timer=120 #in fps
 

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            #GET QUESTION FROM USER
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    self.answer()
                elif event.key==pygame.K_BACKSPACE:
                    self.question=self.question[:-1]
                else:
                    self.question+=event.unicode
                self.text=self.question[-25:]
            #check for submit click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.submit_box.collidepoint(event.pos):
                        self.answer()

    def update(self):
        # Update MainMenu
        pass

    def render(self, screen):
        #background
        screen.blit(self.background_surf,(0,0))
        #user text
        pygame.draw.rect(screen, self.WHITE, self.input_box)
        text_surface = self.font.render(self.text, True, self.BLACK)
        screen.blit(text_surface, (self.input_box.x+5, self.input_box.y+3))
        #submit text
        pygame.draw.rect(screen, self.GREEN, self.submit_box)
        submit_surface=self.font.render(self.submit_text,True,self.WHITE)
        screen.blit(submit_surface, (self.submit_box.x+5,self.submit_box.y+2))
        #display answer
        if self.decrtimer(self.response_timer,self.response_flag):
            text = self.font.render(self.response, True, (255,255,255))
            screen.blit(text, (150,500))

    def answer(self):
        if self.question=='hello':
            self.response='Yes'
        elif self.question=='porco':
            self.response="Doesn't matter"
        else:
            self.response='No'
        self.text=''
        self.question=''
        self.response_timer=120
        self.response_flag=True
        pass

    def decrtimer(self, timer,flag):
        return True
        if flag:
            timer-=1
            if timer<0:
                flag=False
        return flag