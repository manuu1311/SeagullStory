import json


def add_to_json(passage,question,label,contest):
    data_ins={
    'passage': passage,
    'question': question,
    'answer': label,
    'contest': contest,
    'idx' : len(ent_dataset)+len(not_ent_dataset)
    }
    if(data_ins['answer'])==0: ent_dataset.append(data_ins)
    else: not_ent_dataset.append(data_ins)

def save_json(dataset,path):
    with open(path,'w') as f:
        json.dump(dataset,f,indent=1)


boat_contest="""
bob and tom went on a boat trip
""".replace("\n","")

island_contest="""
bob and tom cast away on an island
""".replace("\n","")

final_contest="""
bob realized he ate lucy
""".replace("\n","")



entail_path='entail_questions.json'
not_entail_path='not_entail_questions.json'
with open(entail_path, 'r') as file:
    ent_dataset = json.load(file)
with open(not_entail_path, 'r') as file:
    not_ent_dataset = json.load(file)

while(True):
    num=input("Choose what you want to do!\n"
              "0 :  Save tries to json\n1 :  Add boat unlock sentence\n2 :  Add island unlock sentence\n"
              "3 :  Add win game sentence\n")
    try: num=int(num)
    except: continue
    if num==0:
        save_json(not_ent_dataset,not_entail_path)
        save_json(ent_dataset,entail_path)
        print("Correctly saved. Closing")
        exit()
    elif num==1:
        question=boat_contest
    elif num==2:
        question=island_contest
    elif num==3:
        question=final_contest
    else:
        print("Try again")
    print(f'phrase to entail:\n{question}')
    sent=input("Enter sentence:\n->")
    label=int(input("Enter answer (0: unlock, 1: not unlock)\n->"))
    if(label!=0 and label!=1):
        print("coglione")
        continue
    add_to_json(sent,question,label,num+4)

