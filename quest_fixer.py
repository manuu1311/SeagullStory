import json

with open("questions.json","r") as f:
    dataset=json.load(f)

def change_contest(new_contest, num, x):
    if x['contest']==num: x['passage']=new_contest

def change_label(old,new,x):
    if x['contest']==old: x['contest']=new


#for elem in dataset:
#    change_label(6,5,elem)
contest="""
Bob and Tom are at a pier. they are at the pier because something happened. they are sad and shocked. 
They go to a restaurant. Bob orders seagull meat. The waiter brings him the seagull meat. Bob takes a bite.
Bob kills himself after taking the bite. bob and tom were exhausted. bob and tom had discussions. tom knows
bob would suicide. bob does not know lucy is dead
""".replace("\n","")

for x in dataset: change_contest(contest,2,x)
print(len(contest.split()))
with open("questions.json","w") as f:
    dataset=json.dump(dataset,f,indent=2)

