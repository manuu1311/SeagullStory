import pygame
from utils.info_helper import info_helper,key_fact

class mainscreen:
    def __init__(self,width,height,model,info):
        self.path='Game/assets/mainscreen/'
        self.id2label=['Yes','No']
        self.model=model
        self.info=info
        self.WHITE=(255,255,255)
        self.BLACK=(0,0,0)
        self.GREEN=(6,87,2)
        self.WIDTH=width
        self.HEIGHT=height
        self.return_state=None

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
        self.background_surfaces=[self.background_surf_boat,self.background_surf_island,self.background_surf_pier,self.background_surf_general]
        self.contest=2
        self.background_rect=self.background_surf_pier.get_rect(topleft=(0,0))
        self.background_surf_quest=pygame.image.load(self.path+"questionbg.jpg").convert_alpha()
        self.background_surf_quest = pygame.transform.scale(self.background_surf_quest, (self.WIDTH,self.HEIGHT))

        #    QUESTION TEXT WIDGET
        self.font = pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(100, 100, 300, 32)
        #self.input_box.centerx=self.WIDTH//2
        #self.question=''
        #self.text=''
        #self.response_coords=(80,195)

        #    SUBMIT BUTTON
        self.submit_box=pygame.Rect(100,150,90, 26)
        self.submit_box.centerx=self.WIDTH//2
        self.submit_text='Submit'


        #    BOTTOM BAR LOGOS
        r=40

        self.generallogo_surf=pygame.image.load(self.path+"generallogo.jpg").convert_alpha()
        self.generallogo_surf = pygame.transform.smoothscale(self.generallogo_surf, (r,r))
        self.generallogo_rect=self.generallogo_surf.get_rect(center=(399,775))
        
        self.pierlogo_surf=pygame.image.load(self.path+"pierlogo.jpg").convert_alpha()
        self.pierlogo_surf = pygame.transform.smoothscale(self.pierlogo_surf, (r,r))
        self.pierlogo_rect=self.pierlogo_surf.get_rect(center=(285,775))

        self.boatlogo_surf=pygame.image.load(self.path+"boatlogo.jpg").convert_alpha()
        self.boatlogo_surf = pygame.transform.smoothscale(self.boatlogo_surf, (r,r))
        self.boatlogo_rect=self.boatlogo_surf.get_rect(center=(57,775))

        self.islandlogo_surf=pygame.image.load(self.path+"islandlogo.jpg").convert_alpha()
        self.islandlogo_surf = pygame.transform.smoothscale(self.islandlogo_surf, (r,r))
        self.islandlogo_rect=self.islandlogo_surf.get_rect(center=(171,775))

        self.characterslogo_surf=pygame.image.load(self.path+"characterslogo.jpg").convert_alpha()
        self.characterslogo_surf = pygame.transform.smoothscale(self.characterslogo_surf, (r*1.5,r*1.5))
        self.characterslogo_rect=self.islandlogo_surf.get_rect(topleft=(0,0))

        self.unklogo_surf=pygame.image.load(self.path+"unklogow.jpg")
        self.unklogo_surf = pygame.transform.smoothscale(self.unklogo_surf, (r,r))
        self.contest_flags=self.info.contest_flags

        self.logo_surfaces=[self.unklogo_surf, self.unklogo_surf,self.pierlogo_surf,self.generallogo_surf]
        self.real_logo_surfaces=[self.boatlogo_surf,self.islandlogo_surf,self.pierlogo_surf,self.generallogo_surf]
        self.logos_rects=[self.boatlogo_rect,self.islandlogo_rect,self.pierlogo_rect,self.generallogo_rect]

        #    QUESTION STATE
        self.contest_question_state=0
        self.unlock_questions=info.unlockers

        self.close_surf=pygame.image.load(self.path+"closeicon.jpg").convert_alpha()
        self.close_surf = pygame.transform.smoothscale(self.close_surf, (25,25))
        self.close_rect=self.close_surf.get_rect(center=(380,180))

        #standard text
        self.question_box = pygame.Rect(200, 220, 300, 32)
        self.question_box.centerx=self.WIDTH//2-10
        self.question_font = pygame.font.Font(None, 38)
        self.question_font.italic=True
        self.question_font.bold=True

        #key facts
        self.facts=self.info.facts
        self.facts_counter=self.count_facts()

        #pop up message
        #surf
        self.popup_surf=pygame.image.load(self.path+"dialogbox.jpg").convert_alpha()
        self.popup_surf = pygame.transform.smoothscale(self.popup_surf, (450,350))
        self.popup_rect=self.popup_surf.get_rect(center=(self.WIDTH/2,self.HEIGHT/2))
        #rect
        self.closepopup_surf=pygame.image.load(self.path+"closeicon.jpg").convert_alpha()
        self.closepopup_surf = pygame.transform.smoothscale(self.closepopup_surf, (25,25))
        self.closepopup_rect=self.closepopup_surf.get_rect(center=(370,350))
        #flag
        self.popup_flag=None
        #text
        self.popuptext=[]

        self.reset_state()


    def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.return_state='quit'
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
                        if self.popup_flag:
                            if self.popup_rect.collidepoint(event.pos):
                                self.popup_flag=False
                        if not self.question_flag:
                            if self.submit_box.collidepoint(event.pos):
                                self.guess_onclick()
                            else:
                                for i,rect in enumerate(self.logos_rects):
                                    if rect.collidepoint(event.pos):
                                        if self.contest_flags[i]:
                                            self.reset_state()
                                            self.contest=i
                                        else:
                                            self.question_flag=True
                                            self.prepare_question_state()
                                            self.contest_question_state=i
                        else:
                            if self.close_rect.collidepoint(event.pos):
                                self.question_flag=False
                                self.reset_state()



    def update(self):
        # Update MainMenu
        return self.return_state

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
            #bottom bar
            #black rect
            pygame.draw.rect(screen,(0,0,0),(0,750,450,50))
            #logos
            for i, surf in enumerate(self.logo_surfaces):
                screen.blit(surf,self.logos_rects[i])

         
            screen.blit(self.characterslogo_surf, self.characterslogo_rect)
            #progress bar
            self.DrawBar((10,200),(25,400),(0,0,0),(190,40,50),self.facts_counter/7,screen)
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
        #popup messages
        if self.popup_flag:
            screen.blit(self.popup_surf,self.popup_rect)
            screen.blit(self.closepopup_surf,self.closepopup_rect)
            for i,text in enumerate(self.popuptext):
                text=self.font.render(text,True,(255,255,255))
                screen.blit(text,(self.popup_rect.x+75,self.popup_rect.y+110+30*i))

        #display answer
        text = self.font.render(self.response, True, (0,0,0))
        screen.blit(text, self.response_coords)


    def local_predict(self,unlock_question,question):
        res=self.model.get_predict(unlock_question, question)[0]
        return res[1]<res[0]
    
    def guess_onclick(self):
        if not self.question_flag:
            for keyfact in self.info.facts[self.contest]:
                if not keyfact.flag:
                    if self.local_predict(keyfact.fact,self.question):
                        keyfact.flag=True
                        self.reset_state()
                        self.popup_flag=True
                        self.popuptext=keyfact.text
                        self.facts_counter=self.count_facts()
                        return
            try:
                self.local_predict()
            except:
                self.response='No'
        else:
            try:
                if self.local_predict(self.unlock_questions[self.contest_question_state], self.question):
                    #TODO: popup message
                    self.question_flag=False
                    self.contest_flags[self.contest_question_state]=True
                    self.contest=self.contest_question_state
                    self.reset_state()
                    self.response=''
                    self.logo_surfaces[self.contest_question_state]=self.real_logo_surfaces[self.contest_question_state]
                    self.popup_flag=True
                    self.popuptext=self.info.popupcontext_text[self.contest_question_state]
                else:
                    self.response='No'
            except:
                self.response='No'
        self.question=''
        self.text=''
        self.facts_counter=self.count_facts()


    #unlock contest preparation
    def prepare_question_state(self):
        self.input_box.centerx=self.WIDTH//2
        self.input_box.centery=350
        self.question=''
        self.text=''
        self.response_coords=(90,550) 
        self.response=''
    
    #close question state
    def reset_state(self):
        self.input_box.top=100
        self.input_box.centerx=self.WIDTH//2
        self.response=''
        self.question=''
        self.text=''
        self.response_coords=(80,195)
        self.popup_flag=False

    def count_facts(self):
        count=0
        for fact in self.info.allfacts:
            if fact.flag:
                count+=1
        for unlk in self.contest_flags:
            if unlk:
                count+=1
        return count-2
    
    def DrawBar(self, pos, size, borderC, barC, progress,screen):
        ysize=size[1]
        pygame.draw.rect(screen, borderC, (*pos, *size), 1)
        innerPos  = (pos[0]+3, (pos[1]-3)+(ysize-2)*(1-progress))
        innerSize = ((size[0]-6), (ysize-5)*progress)
        pygame.draw.rect(screen, barC, (*innerPos, *innerSize))

