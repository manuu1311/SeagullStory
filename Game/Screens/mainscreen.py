import pygame

class mainscreen:
    def __init__(self,width,height,model):
        self.path='Game/assets/'
        self.id2label=['Yes','No']
        self.model=model
        self.WHITE=(255,255,255)
        self.BLACK=(0,0,0)
        self.GREEN=(6,87,2)
        self.WIDTH=width
        self.HEIGHT=height

        #    STATE FLAG
        self.question_flag=False

        #    BACKGROUND IMAGES
        self.background_surf_pier=pygame.image.load(self.path+"pier.jpg").convert_alpha()
        self.background_surf_pier = pygame.transform.scale(self.background_surf_pier, (self.WIDTH,self.HEIGHT))
        self.background_surf_boat=pygame.image.load(self.path+"boat.jpg").convert_alpha()
        self.background_surf_boat = pygame.transform.scale(self.background_surf_boat, (self.WIDTH,self.HEIGHT))
        self.background_surf_island=pygame.image.load(self.path+"island.jpg").convert_alpha()
        self.background_surf_island = pygame.transform.scale(self.background_surf_island, (self.WIDTH,self.HEIGHT))
        self.background_surf_general=pygame.image.load(self.path+"generalbackground.jpg").convert_alpha()
        self.background_surf_general = pygame.transform.scale(self.background_surf_general, (self.WIDTH,self.HEIGHT))
        self.background_surfaces=[self.background_surf_general,self.background_surf_pier,self.background_surf_boat,self.background_surf_island]
        self.contest=1
        self.background_rect=self.background_surf_pier.get_rect(topleft=(0,0))
        self.background_surf_quest=pygame.image.load(self.path+"questionbg.jpg").convert_alpha()
        self.background_surf_quest = pygame.transform.scale(self.background_surf_quest, (self.WIDTH,self.HEIGHT))

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

        #    ANSWER TEXT
        self.response=''

        #    BOTTOM BAR LOGOS
        r=40

        self.generallogo_surf=pygame.image.load(self.path+"generallogo.jpg").convert_alpha()
        self.generallogo_surf = pygame.transform.smoothscale(self.generallogo_surf, (r,r))
        self.generallogo_rect=self.generallogo_surf.get_rect(center=(57,775))
        
        self.pierlogo_surf=pygame.image.load(self.path+"pierlogo.jpg").convert_alpha()
        self.pierlogo_surf = pygame.transform.smoothscale(self.pierlogo_surf, (r,r))
        self.pierlogo_rect=self.pierlogo_surf.get_rect(center=(171,775))

        self.boatlogo_surf=pygame.image.load(self.path+"boatlogo.jpg").convert_alpha()
        self.boatlogo_surf = pygame.transform.smoothscale(self.boatlogo_surf, (r,r))
        self.boatlogo_rect=self.boatlogo_surf.get_rect(center=(285,775))

        self.islandlogo_surf=pygame.image.load(self.path+"islandlogo.jpg").convert_alpha()
        self.islandlogo_surf = pygame.transform.smoothscale(self.islandlogo_surf, (r,r))
        self.islandlogo_rect=self.islandlogo_surf.get_rect(center=(399,775))

        self.characterslogo_surf=pygame.image.load(self.path+"characterslogo.jpg").convert_alpha()
        self.characterslogo_surf = pygame.transform.smoothscale(self.characterslogo_surf, (r*1.5,r*1.5))
        self.characterslogo_rect=self.islandlogo_surf.get_rect(topleft=(0,0))

        self.unklogo_surf=pygame.image.load(self.path+"unklogow.jpg")
        self.unklogo_surf = pygame.transform.smoothscale(self.unklogo_surf, (r,r))
        self.contest_flags=[True,True,False,False]
        self.logo_surfaces=[self.generallogo_surf,self.pierlogo_surf,self.unklogo_surf, self.unklogo_surf]

        self.logos_rects=[self.generallogo_rect,self.pierlogo_rect,self.boatlogo_rect,self.islandlogo_rect]

        #    QUESTION STATE
        self.unlock_phrase=None
        self.unlock_questions=[None,None,"bob is good", "bob is blind"]

        self.close_surf=pygame.image.load(self.path+"closeicon.jpg").convert_alpha()
        self.close_surf = pygame.transform.smoothscale(self.close_surf, (25,25))
        self.close_rect=self.close_surf.get_rect(center=(380,180))

        #standard text
        self.question_box = pygame.Rect(200, 220, 300, 32)
        self.question_box.centerx=self.WIDTH//2-10
        self.question_font = pygame.font.Font(None, 38)
        self.question_font.italic=True
        self.question_font.bold=True


    def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
                #GET QUESTION FROM USER
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        self.guess_onclick()
                        
                    elif event.key==pygame.K_BACKSPACE:
                        self.question=self.question[:-1]
                    else:
                        self.question+=event.unicode
                    self.text=self.question[-25:]
                #check for click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not self.question_flag:
                            if self.submit_box.collidepoint(event.pos):
                                self.guess_onclick()
                            else:
                                for i,rect in enumerate(self.logos_rects):
                                    if rect.collidepoint(event.pos):
                                        if self.contest_flags[i]:
                                            self.contest=i
                                        else:
                                            self.unlock_phrase=self.unlock_questions[i]
                                            self.question_flag=True
                                            self.prepare_question_state()



    def update(self):
        # Update MainMenu
        pass

    def render(self, screen):
        if not self.question_flag:
            #background
            screen.blit(self.background_surfaces[self.contest],(0,0))
            #user text
            pygame.draw.rect(screen, self.WHITE, self.input_box)
            text_surface = self.font.render(self.text, True, self.BLACK)
            screen.blit(text_surface, (self.input_box.x+5, self.input_box.y+3))
            #submit text
            pygame.draw.rect(screen, self.GREEN, self.submit_box)
            submit_surface=self.font.render(self.submit_text,True,self.WHITE)
            screen.blit(submit_surface, (self.submit_box.x+5,self.submit_box.y+2))
            #display answer
            text = self.font.render(self.response, True, (0,0,0))
            screen.blit(text, (80,195))
            #bottom bar
            #black rect
            pygame.draw.rect(screen,(0,0,0),(0,750,450,50))
            #logos
            screen.blit(self.logo_surfaces[0],self.generallogo_rect)
            screen.blit(self.logo_surfaces[1],self.pierlogo_rect)
            screen.blit(self.logo_surfaces[2],self.boatlogo_rect)
            screen.blit(self.logo_surfaces[3],self.islandlogo_rect)
            screen.blit(self.characterslogo_surf, self.characterslogo_rect)
        else:
            #question state
            screen.blit(self.background_surf_quest,(0,0))
            screen.blit(self.close_surf,self.close_rect)
            #standard text
            text_surface = self.question_font.render("What happened before?", True, self.BLACK)
            screen.blit(text_surface, (self.question_box.x, self.question_box.y+3))
            #user text
            text_surface = self.font.render(self.text, True, self.BLACK)
            screen.blit(text_surface, (self.input_box.x+5, self.input_box.y+3))
        #always

    def answer(self):
        res=self.model.get_predict("bob is blind", self.question)[0]
        lblid=0
        if res[1]>res[0]:
            lblid=1
        self.response=self.id2label[lblid]
    
    def guess_onclick(self):
        try:
            self.answer()
        except:
            self.response='No'
        self.question=''
        self.text=''

    def prepare_question_state(self):
        self.input_box.centerx=self.WIDTH//2
        self.input_box.centery=350
        self.question=''
        self.text=''
