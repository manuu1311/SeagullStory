import pygame

class characterscreen:
    def __init__(self,width,height,model,info):
        self.WIDTH=width
        self.HEIGHT=height
        self.path="Game/assets/characterscreen/"
        self.model=model
        self.response_state=None
        self.info=info

        #    BACKGROUND IMAGES
        self.background_surf=pygame.image.load(self.path+"background.jpg").convert_alpha()
        self.background_surf = pygame.transform.scale(self.background_surf, (self.WIDTH,self.HEIGHT)) 

        self.font = pygame.font.Font(None, 32)

        #back button
        self.backbutton_surf=pygame.image.load(self.path+'back.png').convert_alpha()
        self.backbutton_surf = pygame.transform.scale(self.backbutton_surf, (30,30))
        self.backbutton_rect=self.backbutton_surf.get_rect(center=(25,780))
        #magnifying glass
        self.glass_surf=pygame.image.load(self.path+'magglass.png').convert_alpha()
        self.glass_surf = pygame.transform.scale(self.glass_surf, (30,30))
        self.glass_rect=self.glass_surf.get_rect(center=(425,780))
        #facts screen
        self.fact_flag=False
        #facts text
        self.fact_to_print=[]
        #fact close button
        self.closebutton_surf=pygame.image.load(self.path+'close.png').convert_alpha()
        self.closebutton_surf = pygame.transform.scale(self.closebutton_surf, (50,50))
        self.closebutton_rect=self.closebutton_surf.get_rect(center=(410,40))

        #final guess
        self.finalguess_rect=pygame.Rect(178,765,100,30)
        self.finalguess_surf = pygame.Surface((self.finalguess_rect.size))  # the size of your rect
        self.finalguess_surf.fill((10,10,10))
        self.finalguess_surf.set_alpha(255)
        self.finalflag=False
        #popup window for final guess
        borderx=25
        bordery=200
        self.guess_rect=pygame.Rect(borderx,bordery,self.WIDTH-borderx*2,self.HEIGHT-bordery*2)
        self.guess_surf = pygame.Surface((self.WIDTH-borderx*2,self.HEIGHT-bordery*2))  # the size of your rect
        self.guess_surf.fill((100,100,100))
        self.guess_surf.set_alpha(200)
        self.closeguess_rect=self.closebutton_surf.get_rect(center=(400,225))
        self.submitguess_rect=pygame.Rect(0,0,50,30)
        self.submitguess_rect.center=(200,550)
        #question
        self.question=''
        self.text=''
        self.response=''

        self.reset()

    
    def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.response_state= 'quit'
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if self.backbutton_rect.collidepoint(event.pos):
                        self.response_state='mainscreen'
                        return
                    elif self.closebutton_rect.collidepoint(event.pos):
                        self.fact_flag=False
                        return
                    elif self.glass_rect.collidepoint(event.pos):
                        self.fact_flag=True
                        return
                    elif self.finalguess_rect.collidepoint(event.pos):
                        self.finalflag=True
                    elif self.closeguess_rect.collidepoint(event.pos):
                        self.finalflag=False
                        self.response=''
                        self.question=''
                        self.text=''
                    elif self.submitguess_rect.collidepoint(event.pos):
                        try:
                            self.question=''
                            self.text=''
                            if self.guess_onclick():
                                self.response_state='win'
                                return
                            else:
                                self.question=''
                                self.text=''
                                self.response='No'
                        except:
                            self.question=''
                            self.text=''
                            self.response='No'
                    for i,rect in enumerate(self.rects):
                        if rect.collidepoint(event.pos):
                            self.character=i
                            self.to_print=self.character_prints[i]
                elif event.type == pygame.KEYDOWN:
                    if self.finalflag:
                        if event.key==pygame.K_RETURN:
                            try:
                                if self.guess_onclick():
                                    self.response_state='win'
                                    return
                                else:
                                    self.question=''
                                    self.text=''
                                    self.response='No'
                            except:
                                self.question=''
                                self.text=''
                                self.response='No'                            
                        elif event.key==pygame.K_BACKSPACE:
                            self.question=self.question[:-1]
                        else:
                            self.question+=event.unicode
                        self.text=self.question[-25:]
                        
                    
                            
                
    def update(self):
        # Update screen
        return self.response_state
    
    def render(self, screen):
        screen.fill((0,0,0))
        #background
        screen.blit(self.background_surf,(0,0))
        if not self.fact_flag:
            for i,surf in enumerate(self.surfs):
                screen.blit(surf, self.rects[i])
            #print message
            for i,text in enumerate(self.to_print):
                    text=self.font.render(text,True,(0,0,0))
                    screen.blit(text,(30,300+30*i))
        else:
            offset=30
            for i,text in enumerate(self.fact_to_print):
                    offset+=60
                    for j,note in enumerate(text):
                        text=self.font.render(note,True,(0,0,0))
                        screen.blit(text,(30,offset))
                        offset+=22
            screen.blit(self.closebutton_surf,self.closebutton_rect)

        screen.blit(self.backbutton_surf,self.backbutton_rect)
        screen.blit(self.glass_surf,self.glass_rect)
        screen.blit(self.finalguess_surf,self.finalguess_rect)
        submitxt=self.font.render('Guess',True,(40,200,20))
        screen.blit(submitxt,(self.finalguess_rect.x+16,self.finalguess_rect.y+5))
        #final guess
        if self.finalflag:
            #why albert ended his life
            screen.blit(self.guess_surf,self.guess_rect)
            text=self.font.render('Why did Albert end his life?',True,(0,0,0))
            screen.blit(text,(self.guess_rect.x+50,self.guess_rect.y+50))
            #close button
            screen.blit(self.closebutton_surf,self.closeguess_rect)
            #submit button
            text=self.font.render('SUBMIT',True,(0,0,0))
            screen.blit(text,(self.submitguess_rect.x+10,self.submitguess_rect.y+5))
            #user question print
            text=self.font.render(self.text,True,(0,0,0))
            screen.blit(text,(self.guess_rect.x+5,self.guess_rect.y+120))
            #response print
            text=self.font.render(self.response,True,(0,0,0))
            screen.blit(text,(self.guess_rect.x+5,self.guess_rect.y+150))
        
    def guess_onclick(self):
        res=self.model.get_predict('Albert realized he ate Lucy', self.question)[0]
        answer=res[1]<res[0]
        return answer
        
    def reset(self):
        #people
        if self.info.allfacts[0].flag:
            if self.info.allfacts[1].flag:
                if self.info.allfacts[4].flag:
                    albertpath='alblindsad.png'
                else:
                    albertpath='alblindhappy.png'
            else:
                albertpath='alblind.png'
        else:
            if self.info.allfacts[1].flag:
                if self.info.allfacts[4].flag:
                    albertpath='albsad.png'
                else:
                    albertpath='albhappy.png'
            else:
                albertpath='albert.png'

        davepath='dave.png'
        waiterpath='waiter.png'
        if self.info.allfacts[1].flag:
            if self.info.allfacts[4].flag:
                lucypath='lucydead.png'
            else:
                lucypath='lucy.png'
        else:
            lucypath='unkn.jpg'
        if self.info.allfacts[3].flag:
            sailorpath='sailor.png'
        else:
            sailorpath='unkn.jpg'

        self.albert_surf=pygame.image.load(self.path+albertpath).convert_alpha()
        self.albert_surf = pygame.transform.scale(self.albert_surf, (120,120))
        self.albert_rect=self.albert_surf.get_rect(center=(70,75))

        self.dave_surf=pygame.image.load(self.path+davepath).convert_alpha()
        self.dave_surf = pygame.transform.scale(self.dave_surf, (120,120))
        self.dave_rect=self.dave_surf.get_rect(center=(220,75))

        self.waiter_surf=pygame.image.load(self.path+waiterpath).convert_alpha()
        self.waiter_surf = pygame.transform.scale(self.waiter_surf, (120,120))
        self.waiter_rect=self.waiter_surf.get_rect(center=(370,75))

        self.lucy_surf=pygame.image.load(self.path+lucypath).convert_alpha()
        self.lucy_surf = pygame.transform.scale(self.lucy_surf, (120,120))
        self.lucy_rect=self.lucy_surf.get_rect(center=(70,210))

        self.sailor_surf=pygame.image.load(self.path+sailorpath).convert_alpha()
        self.sailor_surf = pygame.transform.scale(self.sailor_surf, (120,120))
        self.sailor_rect=self.sailor_surf.get_rect(center=(220,210))

        #messages i want to print
        self.to_print=[]
        self.surfs=[self.albert_surf,self.dave_surf,self.waiter_surf,self.lucy_surf,self.sailor_surf]
        self.rects=[self.albert_rect,self.dave_rect,self.waiter_rect,self.lucy_rect,self.sailor_rect]
        
        #notes for each character
        albertnotes=['Albert']
        lucynotes=['Lucy']
        if self.info.allfacts[0].flag:
            albertnotes.append('Is blind')
        if self.info.allfacts[1].flag:
            albertnotes.append('Has a girlfriend, Lucy')
        if self.info.allfacts[4].flag:
            lucynotes=[('Is dead')]
        self.character_prints=[albertnotes,['Dave'],['Waiter'],lucynotes,['Sailor']]

        #which character am i focusing on?
        self.character=0
        self.response_state=None
        #fact flag to false
        self.fact_flag=False
        #facts to print
        elsetxt=['??????????????????']
        boatxt,islandtxt,alblind,albgf,cannib,lucydead,sailorsave=elsetxt,elsetxt,elsetxt,elsetxt,elsetxt,elsetxt,elsetxt
        if self.info.contest_flags[0]:
            boatxt=['Albert and Dave went on a boat trip']
        if self.info.contest_flags[1]:
            islandtxt=['Albert and Dave cast away','on a desert island']
        if self.info.allfacts[0].flag:
            alblind=['Albert is blind']
        if self.info.allfacts[1].flag:
            albgf=['Albert has a girlfriend,','you can refer to her as Lucy']
        if self.info.allfacts[2].flag:
            cannib=['Albert and Dave resorted to','cannibalism in order to survive']
        if self.info.allfacts[3].flag:
            sailorsave=['A sailor saves Albert and Dave','from the island']
        if self.info.allfacts[4].flag:
            lucydead=['Lucy died in the castaway']
        self.fact_to_print=[boatxt,islandtxt,alblind,albgf,cannib,lucydead,sailorsave]
        #finalflag
        self.finalflag=False
        #text and question
        self.text=''
        self.question=''
        self.response=''