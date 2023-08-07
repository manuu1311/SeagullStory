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
 Bob and Tom face the challenge of surviving with limited food resources, while lucy is already dead. 
 They resort to unconventional means to sustain themselves but manage to do so as they navigate 
 their newfound circumstances. One day, while exploring the island, Tom makes a heartbreaking discovery. He stumbles
 upon Lucy's lifeless body, a painful reminder of the tragic shipwreck. Tom is devastated, and the loss of 
 their dear friend weighs heavily on him. As they continue their struggle for survival, Tom has no other options
 than eating some of Lucy's remains. He does not tell Bob the truth about their food source: Tom assures Bob 
 they are eating seagull meat. Bob remains doubtful, but decides to trust Tom's words for the time being. A fortunate 
 turn of events finally occurs. A passing sailor spots Bob and Tom and rushes to their rescue. The sailor is a good-hearted man, 
 genuinely concerned for their well-being. He helps them off the island and brings them to a nearby pier.
Bob and Tom are grateful for their rescue. They feel a mixture of relief and sorrow as they begin to cope 
with the aftermath of their island ordeal. As they return to civilization, the memory of Lucy stays with them.
""".replace("\n","")
num_contest=4
print(contest)
print(len(contest.split()))

ent_dataset=utils.change_contest(contest,num_contest,ent_dataset)
not_ent_dataset=utils.change_contest(contest,num_contest,not_ent_dataset)
utils.save_dataset(ent_dataset,entail_path)
utils.save_dataset(not_ent_dataset,not_entail_path)
printinfo()

