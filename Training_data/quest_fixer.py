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
bob tom and lucy are friends. bob and lucy are married. bob is blind. bob is not religious.
bob loves lucy. lucy loves bob. bob tom and lucy are middle aged. the story is set in the early 900's.
the story is completely plausible.
""".replace("\n","")

ent_dataset=utils.change_contest(contest,1,ent_dataset)
not_ent_dataset=utils.change_contest(contest,1,not_ent_dataset)
utils.save_dataset(ent_dataset,entail_path)
utils.save_dataset(not_ent_dataset,not_entail_path)
printinfo()

