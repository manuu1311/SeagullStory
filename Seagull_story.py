#TODO: where the api will be called, need to handle all contests and pre-processing


#TODO: api caller
def get_answer_from_api(passage, question):
    #send api the 2 sentences and get response
    response="Not implemented yet"
    return response


#initializing all contests

generalcontest= """
bob tom and lucy are friends. bob and lucy are married. bob is blind. bob is not religious.
bob loves lucy. lucy loves bob. bob tom and lucy are middle aged. the story is set in the early 900's.
the story is completely plausible.
""".replace("\n","")

piercontest="""
Bob and Tom are at a pier. they are at the pier because something happened. they are sad and shocked. 
They go to a restaurant. Bob orders seagull meat. The waiter brings him the seagull meat. Bob takes a bite.
Bob kills himself after taking the bite. bob and tom were exhausted. bob and tom had discussions. tom knows 
bob would suicide. bob does not know lucy is dead
""".replace("\n","")

boatcontest="""
bob tom and lucy are having fun. they did not have an argument. what happened was not upon them.
there is a storm and the boat is wrecked. bob, tom, lucy cast away on an island. 
""".replace("\n","")

general_islandcontest="""
lucy dies in the shipwreck. bob and tom manage to survive. they are alone on the island. the island is desert. there are not 
dangerous animals. bob and tom do not have to fight to survive. there is no one else on the island. there is not much food.
they resort to unconvential food sources. they did not have to fight. tom finds lucy's corpse. they manage to survive.
tom is compelled to eat lucy. he does not want to eat lucy. he eats lucy. bob also eats lucy. bob does not
know he is eating lucy. tom revolts while eating lucy. bob does not revolt while eating lucy. tom tells bob he is eating seagull.
bob thinks he is eating seagull. bob is suspicious. there is a sailor passing by. the sailor saves bob and tom and brings them to a pier. the sailor is a good man.
 the sailor does not have ill intentions. bob and tom are grateful to the sailor.bob does not know lucy is dead
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

#true: print the contest before asking the question, false: do not print anything
print_flag=False
#infinite question asking loop
while(True):
    checker=True
    num=input(
        f"""
Choose what you want to do!
0 :  Enable/disable print flag (currently {"enabled" if print_flag else "disabled"})
1 :  Ask general question\n2 :  Ask pier question\n3 :  Ask boat contest
4 :  Ask island question\n5 :  Try boat unlock sentence\n6 :  Try island unlock sentence\n7 :  Try win game sentence
""")
    try: num=int(num)
    except: continue
    if num==1:
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
    elif num==0:
        print_flag=not print_flag
    else:
        print("Try again")
        continue
    if checker:
        if print_flag:
            print(f'contest:\n{passage}')
        question=input("Enter question:\n->")
    else:
        if print_flag:
            print(f'question:\n{question}')
        passage=input("Enter guess:\n->")
    response=get_answer_from_api(question,passage)
    print(f'Response: {response}')

