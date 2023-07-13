import json

with open("questions.json","r") as f:
    dataset=json.load(f)

def change_contest(new_contest, num, x):
    if x['contest']==num: x['passage']=new_contest

def change_label(old,new,x):
    if x['contest']==old: x['contest']=new


#for elem in dataset:
#    change_label(6,5,elem)

for x in dataset: change_label(5,4,x)

with open("questions.json","w") as f:
    dataset=json.dump(dataset,f,indent=2)

