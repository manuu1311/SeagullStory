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
In a peaceful village, there lived a kind-hearted girl named Mia. Every morning, she fed the birds in the park and helped the elderly with
 their groceries. One day, she found a wounded kitten and nursed it back to health. As they became inseparable, the village praised Mia's compassion.
   Little did she know, her act of kindness would lead to an unexpected adventure.
""".replace("\n","")
contest=10

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
