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

path="Training_data/ran_questions.json"
with open(path,'r') as f:
    dataset=json.load(f)

story="""
lucy died in the shipwreck
""".replace("\n","")
contest=11

# true: unlock guess false: story question
unlock_flag=True
question=""
if unlock_flag: question=story
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
        print("story:\n"+question if unlock_flag else story)
        if unlock_flag:
            story=input("Enter your guess\n->")
        else:
            question=input("Enter your question\n->")
        label=int(input("Enter answer (0: entailment, 1: not entailment)\n"))
        if(label!=0 and label!=1):
            print("coglione")
            continue
        add_to_json(story,question,label, contest)
