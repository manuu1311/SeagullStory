class key_fact():
    def __init__(self,flag,fact,trigger=False):
        self.flag=flag
        self.fact=fact
        #trigger popup flag
        self.trigger=trigger

class info_helper():
    def __init__(self):
        ### PASSAGES
        generalcontest= """
        Albert Dave and lucy are friends. they are completely normal people. Albert and lucy are happily married. Albert and lucy are 
        loyal and really love each other, their love is true. Albert loves lucy. lucy loves Albert. Albert Dave and lucy are middle aged. 
        Albert is blind. Albert is not religious. 
        the story is set in the early 900's. the story is completely plausible and does not involve anything not realistic.
        """.replace("\n","")
        piercontest="""
        A kind sailor saved Albert and Dave from an island and brought them to a pier with his boat. Now, they are sad and shocked. 
        Albert does not know lucy  is dead, Dave knows Lucy is dead. They go to a restaurant. Albert orders seagull meat. 
        The waiter brings Albert the seagull meat. Everything is ordinary. The seagull meat is perfectly fine and edible. 
        After Albert takes a bite, he realizes he had never eaten seagull meat before and because of that Albert kills himself. 
        Dave knew Albert would suicide, so he is not surpirsed. Other people at the restaurant were surprised. 
        Albert and Dave were exhausted. Albert and Dave had discussions.  Albert wanted to go to the restaurant 
        in order to eat seagull, Albert had this plan when he was on the island and nothing that happened changed Albert's mind.
        """.replace("\n","")

        boatcontest="""
        Albert Dave and lucy are having fun. they did not have any argument. 
        what happened was not upon them. there is a storm and the boat is wrecked. Albert, Dave, lucy cast away on an island.  
        """.replace("\n","")

        general_islandcontest="""
        lucy dies in the shipwreck. Albert and Dave manage to survive. they are alone on the island. there is no one else on the island. 
        there are not dangerous animals. Albert and Dave do not have to fight to survive. there is no one else on the island. 
        there is not much food.they resort to unconvential food sources. they did not have to fight. Dave finds lucy's corpse. 
        they manage to survive.Dave is compelled to eat lucy. Dave does not want to eat lucy. Dave eats lucy. Albert also eats lucy. 
        because Albert is blind, Albert does not know he is eating lucy. Dave knows he is eating lucy. Dave revolts while eating lucy. 
        Albert does not revolt while eating lucy. Dave tells Albert he is eating seagull. Albert thinks he is eating seagull. 
        Albert is suspicious. there is a sailor passing by. the sailor saves Albert and Dave and brings them to a pier. 
        the sailor is a good man. the sailor does not have ill intentions. Albert and Dave are grateful to the sailor. 
        Albert does not know lucy is dead. Dave knows lucy is dead.
        """.replace("\n","")
        self.passages=[boatcontest,general_islandcontest,piercontest,generalcontest]

        ### FLAGS
        self.contest_flags=[False,False,True,True]
        ### UNLOCK PHRASES
        self.unlockers=['Albert and Dave went on a boat trip','Albert and Dave cast away on an island',None,None]
        ### KEY FACTS
        #pier
        albertgf_fact=key_fact(False, "Albert has a girlfriend",True)
        lucydead_fact=key_fact(False, "Lucy is dead")
        #boat
        #none
        #island
        cannib_fact=key_fact(False,"Albert ate Lucy")
        sailor_fact=key_fact(False,"A sailor saves Albert")
        #general
        albertblind_fact=key_fact(False,"Albert is blind")
        self.allfacts=[albertblind_fact,albertgf_fact,cannib_fact,sailor_fact,lucydead_fact]
        self.facts=[[lucydead_fact,cannib_fact,sailor_fact],[],[albertgf_fact,lucydead_fact],[albertgf_fact,lucydead_fact,albertblind_fact]]

    
