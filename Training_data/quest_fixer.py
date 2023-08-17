import utils
ent_dataset,not_ent_dataset,neutral_dataset=utils.get_datasets()

def printinfo():
    print(f'Dataset length: {len(ent_dataset)+len(not_ent_dataset)+len(neutral_dataset)}')
    print("Contest\tYes\tNo\t     Doesn't matter")
    for i in range(7):
        yes=utils.getinfo(ent_dataset,i+1)
        no=utils.getinfo(not_ent_dataset,i+1)
        neu=utils.getinfo(neutral_dataset,i+1)
        print(f'   {i+1}   \t {yes} \t{no}\t   {neu}')


entail_path='Training_data/entail_questions.json'
not_entail_path='Training_data/not_entail_questions.json'
neutral_path='Training_data/neutral_questions.json'

#for elem in dataset:
#    change_label(6,5,elem)
contest="""
A kind sailor saved Bob and Tom from an island and brought them to a pier with his boat. Now, they are sad and shocked. Bob does not know lucy  
is dead, Tom knows Lucy is dead. They go to a restaurant. Bob orders seagull meat. The waiter brings bob the seagull meat. 
Everything is ordinary. The seagull meat is perfectly fine and edible. After Bob takes a bite, he realizes he had never eaten seagull 
meat before and because of that Bob kills himself. Tom knew bob would suicide, so he is not surpirsed. Other people at the 
restaurant were surprised. Bob and tom were exhausted. bob and tom had discussions.  
Bob wanted to go to the restaurant in order to eat seagull, bob had this plan when he was on the island and nothing 
that happened changed bob's mind.
""".replace("\n","")
num_contest=2
print(contest)
print(len(contest.split()))

#ent_dataset=utils.change_contest(contest,num_contest,ent_dataset)
#not_ent_dataset=utils.change_contest(contest,num_contest,not_ent_dataset)
#neutral_dataset=utils.change_contest(contest,num_contest,neutral_dataset)

for i in range(len(ent_dataset)):
    ent_dataset[i]['passage']=ent_dataset[i]['passage'].replace("bob","Albert").replace("Bob","Albert").replace("tom","Dave").replace("Tom","Dave")
    ent_dataset[i]['question']=ent_dataset[i]['question'].replace("bob","Albert").replace("Bob","Albert").replace("tom","Dave").replace("Tom","Dave")
for i in range(len(not_ent_dataset)):    
    not_ent_dataset[i]['passage']=not_ent_dataset[i]['passage'].replace("bob","Albert").replace("Bob","Albert").replace("tom","Dave").replace("Tom","Dave")
    not_ent_dataset[i]['question']=not_ent_dataset[i]['question'].replace("bob","Albert").replace("Bob","Albert").replace("tom","Dave").replace("Tom","Dave")
for i in range(len(neutral_dataset)):
    neutral_dataset[i]['passage']=ent_dataset[i]['passage'].replace("bob","Albert").replace("Bob","Albert").replace("tom","Dave").replace("Tom","Dave")
    neutral_dataset[i]['question']=ent_dataset[i]['question'].replace("bob","Albert").replace("Bob","Albert").replace("tom","Dave").replace("Tom","Dave")

print(ent_dataset[0],ent_dataset[-1])
print(not_ent_dataset[20])
print(neutral_dataset[30])

utils.save_dataset(ent_dataset,entail_path)
utils.save_dataset(not_ent_dataset,not_entail_path)
utils.save_dataset(neutral_dataset,neutral_path)


printinfo()

