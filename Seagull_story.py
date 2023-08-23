#TODO: where the api will be called, need to handle all contests and pre-processing
#from API_setup.Answer_processing import get_predict
from App import ui
from App.GUI import controller


#initializing all contests

generalcontest= """
In the early 900's, Bob, Tom, and Lucy are middle-aged friends. Bob and Lucy are happily married, despite Bob being blind. 
Religion doesn't play a significant role in this story. Bob's love for Lucy and Lucy's love for Bob create a strong and 
enduring bond between them. This story is completely plausible
""".replace("\n","")

piercontest="""
Bob and Tom find themselves at the pier due to a distressing event, leaving them feeling sad and shocked. Unaware of Lucy's fate, 
Bob engages in discussions with Tom, who carries the burden of knowing that Lucy has passed away. The weight of their emotions
 adds an additional layer of complexity to their already difficult situation. Seeking a respite from their
 emotions, they head to a nearby restaurant. Bob, emotionally drained, decides to order seagull meat. The waiter promptly 
 serves Bob the dish, Bob takes a bite. Then, Bob kills himself. Lucy is Bob's wife, the seagull meat was perfectly fine. The reason 
 behind Bob's extreme act is to be found in something that happened long before, not because of something that happened at the pier 
 or at the restaurant.
""".replace("\n","")

boatcontest="""
Bob, Tom, and Lucy are enjoying a delightful time together on a boat, free from any conflicts or disagreements. However, their joyful 
outing takes a dramatic turn when they encounter a violent storm that wrecks their boat. As a result, the three friends 
find themselves stranded on a remote island, facing the challenges of survival in a place far from their initial plans.
""".replace("\n","")

general_islandcontest="""
 Bob and Tom face the challenge of surviving with limited food resources, while lucy is already dead. 
 They resort to unconventional means to sustain themselves but manage to do so as they navigate 
 their newfound circumstances. One day, while exploring the island, Tom makes a heartbreaking discovery. He stumbles
 upon Lucy's lifeless body, a painful reminder of the tragic shipwreck. Tom is devastated, and the loss of 
 their dear friend weighs heavily on him. As they continue their struggle for survival, Tom has no other options
 than eating some of Lucy's remains. He does not tell Bob the truth about their food source: Tom assures Bob 
 they are eating seagull meat. Bob remains doubtful, but decides to trust Tom's words for the time being. A fortunate 
 turn of events finally occurs. A passing sailor spots Bob and Tom and rushes to their rescue. The sailor is a good-hearted man, 
 genuinely concerned for their well-being. He helps them off the island and brings them to a nearby pier.
Bob and Tom are grateful for their rescue. They feel a mixture of relief and sorrow as they begin to cope 
with the aftermath of their island ordeal. As they return to civilization, the memory of Lucy stays with them.
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

'''
#true: print the contest before asking the question, false: do not print anything
print_flag=False
#where to save the questions asked
quest_path="Training_data/QuestionDB.txt"
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
        continue
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
    response=get_predict(question,passage)
    with open(quest_path,'a') as f:
        f.write(f'Contest: {num}\nPassage: {passage}\nQuestion: {question}\nAnswer: {response}')
    print(f'Response: {response}')
'''

gui=controller()
gui.changescene(ui.Ui_MainWindow()) 
