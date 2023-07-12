import json


def add_to_json(contest,question,label,dict):
    data_ins={
    'passage': generalcontest,
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

path='questions.json'

with open(path, 'r') as file:
    dataset = json.load(file)

while(True):
    num=int(input("Choose what you want to do!\n"
              "0 :  Save questions to json\n1 :  Add general question\n2 :   Add pier question\n"))
    if num==0:
        save_json(dataset,path)
        print("Correctly saved. Closing")
        exit()
    elif num==1:
        passage=generalcontest
    elif num==2:
        passage=piercontest
    else:
        print("Try again")
    print(f'contest:\n{passage}')
    question=input("Enter question:\n->")
    label=int(input("Enter answer (0: entailment, 1: not entailment)\n->"))
    if(label!=0 and label!=1):
        print("coglione")
        continue
    add_to_json(passage,question,label,dataset)
