import json

def get_datasets():
    with open("Training_data/entail_questions.json","r") as f:
        ent_dataset=json.load(f)
    with open("Training_data/not_entail_questions.json","r") as f:
        not_ent_dataset=json.load(f)
    with open("Training_data/neutral_questions.json","r") as f:
        neutral_dataset=json.load(f)
    return ent_dataset,not_ent_dataset,neutral_dataset

def get_train():
    with open("Training_data/trainset.json","r") as f:
            trainset=json.load(f)
    with open("Training_data/validset.json","r") as f:
            validset=json.load(f)
    return trainset,validset

def change_contest(new_contest, num,dataset):
    for i in range(len(dataset)):
        if dataset[i]['contest']==num: dataset[i]['passage']=new_contest
    return dataset

def change_label(old,new,x):
    if x['contest']==old: x['contest']=new

def getinfo(dataset,contest):
    for _ in range(7):
        incont = len(list(filter(lambda x : x['contest']==contest,dataset)))
    return incont

def save_dataset(dataset,path):
    with open(path,'w') as f:
        json.dump(dataset,f,indent=2)

def order_dataset(dataset):
     dataset=sorted(dataset, key= lambda x : x['contest'])
     return dataset


