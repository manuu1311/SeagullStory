import json


def add_to_json(passage,question,label,contest):
    data_ins={
    'passage': passage,
    'question': question,
    'answer': label,
    'contest': contest
    }
    dataset.append(data_ins)

def save_json(dataset,path):
    with open(path,'w') as f:
        json.dump(dataset,f,indent=1)

path="ran_questions.json"
with open(path,'r') as f:
    dataset=json.load(f)

story="""
3 people cast away on a desert island. they don't have any tools, so they build new ones with anything they find. they are initially 
scattered in different places of the island, but as they explore the island they eventually find each other. so, they start cooperating.
although no deadly animal is present on the island, food is scarce, so surviving is challenging. they even managed to become friends 
with monkeys. after some time, they build more advanced tools and they are actually happy to be in that island and don't want to look back.
""".replace("\n","")
contest=3

while(True):
    num=(input("0: save\n1:add question\n"))
    try : 
        num=int(num)
    except:
        print("cogliò\n")
        continue
    if num==0:
        save_json(dataset,path)
        incont = list(filter(lambda x : x['contest']==contest,dataset))
        true_num=len(list(filter(lambda x : x['answer']==0,incont)))
        print("Yes questions: ",true_num," No questions: ",len(incont)-true_num)
        print("Total dataset questions: ",len(dataset))
        print("Correctly saved. Exiting")
        exit()
    elif num==1:
        print("story:\n"+story)
        question=input("Enter your question\n->")
        label=int(input("Enter answer (0: entailment, 1: not entailment)\n"))
        if(label!=0 and label!=1):
            print("coglione")
            continue
        add_to_json(story,question,label, contest)
