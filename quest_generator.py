import json


def add_to_json(contest,question,label,dict):
    data_ins={
    'passage': contest,
    'question': question,
    'answer': label
    }
    dict.append(data_ins)

def save_json(dataset,path):
    with open(path,'w') as f:
        json.dump(dataset,f,indent=1)



generalcontest= """
bob tom and lucy are friends. bob and lucy are married. bob is blind. bob is not religious.
bob loves lucy. lucy loves bob. bob tom and lucy are middle aged.
""".replace("\n","")

piercontest="""
Bob and Tom are at a pier. They go to a restaurant. Bob orders seagull meat. The waiter brings him the seagull meat. Bob takes a bite.
Bob kills himself after taking the bite. bob and tom were exhausted. bob and tom had discussions
""".replace("\n","")

boatcontest="""
bob tom and lucy are having fun. they did not have an argument. what happened was not upon them.
there is a storm and the boat is wrecked. bob, tom, lucy cast away on an island. 
""".replace("\n","")

general_islandcontest="""
lucy dies in the shipwreck. bob and tom manage to survive. they are alone on the island. the island is desert. there are not
dangerous animals. bob and tom do not have to fight to survive. there is no one else on the island. there is not much food.
they resort to unconvential food sources. they did not have to fight. tom finds lucy's corpse.
""".replace("\n","")

specific_islandcontest="""
tom is compelled to eat lucy. he does not want to eat lucy. he eats lucy. bob also eats lucy. bob does not
know he is eating lucy. tom revolts while eating lucy. bob does not revolt while eating lucy. they manage to survive. there is a 
sailor passing by. the sailor saves bob and tom and brings them to a pier. the sailor is a good man. the sailor does not have
ill intentions. bob and tom are grateful to the sailor
""".replace("\n","")


print(len(specific_islandcontest),len(general_islandcontest))
path='questions.json'

with open(path, 'r') as file:
    dataset = json.load(file)
print(len(dataset))

while(True):
    num=int(input("Choose what you want to do!\n"
              "0 :  Save questions to json\n1 :  Add general question\n2 :  Add pier question\n"
              "3 :  Add boat contest\n4 :  Add general island question\n5 :  Add specific island question\n"))
    if num==0:
        save_json(dataset,path)
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
        passage=specific_islandcontest
    else:
        print("Try again")
    print(f'contest:\n{passage}')
    question=input("Enter question:\n->")
    label=int(input("Enter answer (0: entailment, 1: not entailment)\n->"))
    if(label!=0 and label!=1):
        print("coglione")
        continue
    add_to_json(passage,question,label,dataset)
