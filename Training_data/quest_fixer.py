import utils
ent_dataset,not_ent_dataset=utils.get_datasets()

def printinfo():
    print(f'Dataset length: {len(ent_dataset)+len(not_ent_dataset)}')
    print("Contest\tYes\tNo")
    for i in range(7):
        yes=utils.getinfo(ent_dataset,i+1)
        no=utils.getinfo(not_ent_dataset,i+1)
        print(f'   {i+1}   \t {yes} \t{no}')


#for elem in dataset:
#    change_label(6,5,elem)
contest="""
lucy dies in the shipwreck. bob and tom manage to survive. they are alone on the island. the island is desert. there are not 
dangerous animals. bob and tom do not have to fight to survive. there is no one else on the island. there is not much food.
they resort to unconvential food sources. they did not have to fight. tom finds lucy's corpse. they manage to survive.
tom is compelled to eat lucy. he does not want to eat lucy. he eats lucy. bob also eats lucy. bob does not
know he is eating lucy. tom revolts while eating lucy. bob does not revolt while eating lucy. tom tells bob he is eating seagull.
bob thinks he is eating seagull. bob is suspicious. there is a sailor passing by. the sailor saves bob and tom and brings them to a pier. the sailor is a good man.
 the sailor does not have ill intentions. bob and tom are grateful to the sailor.bob does not know lucy is dead
""".replace("\n","")

printinfo()

