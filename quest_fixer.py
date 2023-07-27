import utils
ent_dataset,not_ent_dataset=utils.get_train()

#for elem in dataset:
#    change_label(6,5,elem)
contest="""
Bob and Tom are at a pier. they are at the pier because something happened. they are sad and shocked. 
They go to a restaurant. Bob orders seagull meat. The waiter brings him the seagull meat. Bob takes a bite.
Bob kills himself after taking the bite. bob and tom were exhausted. bob and tom had discussions. tom knows 
bob would suicide. bob does not know lucy is dead
""".replace("\n","")

"""
not_ent_dataset=sorted(not_ent_dataset, key=lambda x: x['contest'])


with open("entail_questions.json","w") as f:
    dataset=json.dump(ent_dataset,f,indent=2)
with open("not_entail_questions.json","w") as f:
    dataset=json.dump(not_ent_dataset,f,indent=2)
"""

def getinfo(dataset,contest,answer):
    for _ in range(7):
        incont = len(list(filter(lambda x : x['contest']==contest and x['answer']==answer,dataset)))
    return incont


print(f'Contest\tTrue\tFalse')
for i in range(7):
    true_incont=getinfo(ent_dataset,i+1,0)
    false_incont=getinfo(ent_dataset,i+1,1)
    print(f'  {i+1}  \t {true_incont} \t {false_incont} ')

