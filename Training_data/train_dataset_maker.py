import utils

ent,not_ent=utils.get_datasets()

trainset=[]
validset=[]
for i in range(7):
    truecont=utils.getinfo(ent,i+1)
    falsecont=utils.getinfo(not_ent,i+1)
    checker=truecont>=falsecont
    if checker:
        trainset.extend(ent[:falsecont])
        trainset.extend(not_ent[:falsecont])
        validset.extend(ent[falsecont:truecont])
    else:
        trainset.extend(ent[:truecont])
        trainset.extend(not_ent[:truecont])
        validset.extend(not_ent[truecont:falsecont])

    ent[:truecont]=[]
    not_ent[:falsecont]=[]

utils.save_dataset(trainset,"trainset.json")
utils.save_dataset(validset,"validset.json")