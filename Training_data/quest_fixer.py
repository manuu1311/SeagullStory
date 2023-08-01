import utils
ent_dataset,not_ent_dataset=utils.get_datasets()

def printinfo():
    print(f'Dataset length: {len(ent_dataset)+len(not_ent_dataset)}')
    print("Contest\tYes\tNo")
    for i in range(7):
        yes=utils.getinfo(ent_dataset,i+1)
        no=utils.getinfo(not_ent_dataset,i+1)
        print(f'   {i+1}   \t {yes} \t{no}')


entail_path='Training_data/entail_questions.json'
not_entail_path='Training_data/not_entail_questions.json'

#for elem in dataset:
#    change_label(6,5,elem)
contest="""
Bob and Tom are at a pier. they are at the pier because something happened. they are sad and shocked. 
They go to a restaurant. Bob orders seagull meat. The waiter brings him the seagull meat. Bob takes a bite.
Bob kills himself after taking the bite. bob and tom were exhausted. bob and tom had discussions. tom knows 
bob would suicide. bob does not know lucy is dead. tom knows lucy is dead.
""".replace("\n","")
num_contest=2

ent_dataset=utils.change_contest(contest,num_contest,ent_dataset)
not_ent_dataset=utils.change_contest(contest,num_contest,not_ent_dataset)
utils.save_dataset(ent_dataset,entail_path)
utils.save_dataset(not_ent_dataset,not_entail_path)
printinfo()

