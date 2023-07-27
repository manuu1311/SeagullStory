import json

path="questions.json"
with open(path,'r') as f:
    dataset = json.load(f)

entail_dataset=[]
not_entail_dataset=[]

for x in dataset:
    if x['answer']==1: not_entail_dataset.append(x)
    else: entail_dataset.append(x)

print(len(entail_dataset),len(not_entail_dataset))

with open("entail_questions.json", "w")as f:
    json.dump(entail_dataset,f,indent=1)
with open("not_entail_questions.json", "w")as f:
    json.dump(not_entail_dataset,f , indent=1)
