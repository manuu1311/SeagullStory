import json

def get_datasets():
    with open("entail_questions.json","r") as f:
        ent_dataset=json.load(f)
    with open("not_entail_questions.json","r") as f:
        not_ent_dataset=json.load(f)
    return ent_dataset,not_ent_dataset

def get_train():
    with open("trainset.json","r") as f:
            trainset=json.load(f)
    with open("validset.json","r") as f:
            validset=json.load(f)
    return trainset,validset

def change_contest(new_contest, num, x):
    if x['contest']==num: x['passage']=new_contest

def change_label(old,new,x):
    if x['contest']==old: x['contest']=new

def getinfo(dataset,contest):
    for _ in range(7):
        incont = len(list(filter(lambda x : x['contest']==contest,dataset)))
    return incont

def save_json(dataset,path):
    with open(path,'w') as f:
        json.dump(dataset,f,indent=1)


