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
lucy dies in the shipwreck. bob and tom manage to survive. they are alone on the island. there is no one else on the island. there are 
not dangerous animals. bob and tom do not have to fight to survive. there is no one else on the island. there is not much food.
they resort to unconvential food sources. they did not have to fight. tom finds lucy's corpse. they manage to survive.
tom is compelled to eat lucy. tom does not want to eat lucy. tom eats lucy. bob also eats lucy. because bob is blind, bob does not 
know he is eating lucy. tom knows he is eating lucy. tom revolts while eating lucy. bob does not revolt while eating lucy. 
tom tells bob he is eating seagull. bob thinks he is eating seagull. bob is suspicious. there is a sailor passing by. 
the sailor saves bob and tom and brings them to a pier. the sailor is a good man. the sailor does not have ill intentions. 
bob and tom are grateful to the sailor.bob does not know lucy is dead. tom knows lucy is dead.
""".replace("\n","")
num_contest=4
print(contest)
print(len(contest.split()))

ent_dataset=utils.change_contest(contest,num_contest,ent_dataset)
not_ent_dataset=utils.change_contest(contest,num_contest,not_ent_dataset)
neutral_dataset=utils.change_contest(contest,num_contest,neutral_dataset)

utils.save_dataset(ent_dataset,entail_path)
utils.save_dataset(not_ent_dataset,not_entail_path)
utils.save_dataset(neutral_dataset,neutral_path)
printinfo()

