import utils

ent,not_ent,neut=utils.get_datasets()

trainset=[]
validset=[]
percentage=1
for i in range(7):
    truecont=utils.getinfo(ent,i+1)
    falsecont=utils.getinfo(not_ent,i+1)
    neutcont=utils.getinfo(neut,i+1)
    if truecont<=falsecont and truecont<=neutcont:
        num=round(truecont*percentage)
    elif falsecont<=neutcont:
        num=round(falsecont*percentage)
    else:
        num=round(neutcont*percentage)
    
    ent_temp=ent[:truecont]
    notent_temp=not_ent[:falsecont]
    neut_temp=neut[:neutcont]
    trainset.extend(ent_temp[:num])
    trainset.extend(notent_temp[:num])
    trainset.extend(neut_temp[:num])
    validset.extend(not_ent[num:falsecont])
    validset.extend(ent[num:truecont])
    validset.extend(neut_temp[num:neutcont])

    ent[:truecont]=[]
    not_ent[:falsecont]=[]
    neut[:neutcont]=[]

utils.save_dataset(trainset,"Training_data/trainset.json")
utils.save_dataset(validset,"Training_data/validset.json")

print(f'Dataset length: {len(trainset)}')
print("Contest\tYes\tNo\tDoesn't matter")
for i in range(7):
    yes=utils.getinfo(trainset,i+1)
    print("contest: ",i+1,yes)

