import utils


def add_to_json(passage,question,label,contest):
    data_ins={
    'passage': passage,
    'question': question,
    'answer': label,
    'contest': contest,
    'idx' : len(ent_dataset)+len(not_ent_dataset)
    }
    if(data_ins['answer'])==0: ent_dataset.append(data_ins)
    elif data_ins['answer']==2: not_ent_dataset.append(data_ins)
    else:neutral_dataset.append(data_ins)

def printinfo():
    print(f'Dataset length: {len(ent_dataset)+len(not_ent_dataset)+len(neutral_dataset)}')
    print("Contest\tYes\tNo\tDoesn't matter")
    for i in range(7):
        yes=utils.getinfo(ent_dataset,i+1)
        no=utils.getinfo(not_ent_dataset,i+1)
        neu=utils.getinfo(neutral_dataset,i+1)
        print(f'   {i+1}   \t {yes} \t{no}\t       {neu}')


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

boat_discover="""
bob and tom went on a boat trip
""".replace("\n","")

island_discover="""
bob and tom cast away on an island
""".replace("\n","")

final_discover="""
bob realized he ate lucy
""".replace("\n","")


entail_path='Training_data/entail_questions.json'
not_entail_path='Training_data/not_entail_questions.json'
neutral_path='Training_data/neutral_questions.json'
ent_dataset,not_ent_dataset,neutral_dataset = utils.get_datasets()

while(True):
    checker=True
    num=input("Choose what you want to do!\n"
              "0 :  Save questions to json\n1 :  Add general question\n2 :  Add pier question\n"
              "3 :  Add boat contest\n4 :  Add island question\n5 :  Add boat unlock sentence\n6 :  "
               "Add island unlock sentence\n7 :  Add win game sentence\n")
    try: num=int(num)
    except: continue
    if num==0:
        ent_dataset=utils.order_dataset(ent_dataset)
        not_ent_dataset=utils.order_dataset(not_ent_dataset)
        neutral_dataset=utils.order_dataset(neutral_dataset)
        utils.save_dataset(ent_dataset,entail_path)
        utils.save_dataset(not_ent_dataset,not_entail_path)
        utils.save_dataset(neutral_dataset,neutral_path)
        printinfo()
        print("Correctly saved. Closing")
        exit()
    elif num==1:
        passage=generalcontest
    elif num==2:
        passage=piercontest
    elif num==3:
        passage=boatcontest
    elif num==4:
        passage=general_islandcontest
    elif num==5:
        checker=False
        question=boat_discover
    elif num==6:
        checker=False
        question=island_discover
    elif num==7:
        checker=False
        question=final_discover
    else:
        print("Try again")
    if checker:
        print(f'contest:\n{passage}')
        question=input("Enter question:\n->")
        label=int(input("Enter answer (0: entailment, 1: neutral, 2: not entailment)\n->"))
    else:
        print(f'question:\n{question}')
        passage=input("Enter passage:\n->")
        label=int(input("Enter answer (0: entailment, 1: neutral, 2: not entailment)\n->"))
    
    if(label!=0 and label!=1 and label!=2):
        print("coglione")
        continue
    add_to_json(passage,question,label,num)
