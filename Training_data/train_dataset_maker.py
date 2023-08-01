import utils

ent,not_ent=utils.get_datasets()

trainset=[]
validset=[]
for i in range(7):
    truecont=utils.getinfo(ent,i+1)
    falsecont=utils.getinfo(not_ent,i+1)
    checker=truecont>=falsecont
    if checker:
        num=round(falsecont*0.8)
        temp_data=ent[:num]
        temp_data.extend(not_ent[:num])
        trainset.extend(temp_data)
        validset.extend(not_ent[num:falsecont])
        validset.extend(ent[num:truecont])
    else:
        num=round(truecont*0.8)
        temp_data=ent[:num]
        temp_data.extend(not_ent[:num])
        trainset.extend(temp_data)
        validset.extend(not_ent[num:falsecont])
        validset.extend(ent[num:truecont])

    ent[:truecont]=[]
    not_ent[:falsecont]=[]

utils.save_dataset(trainset,"Training_data/trainset.json")
utils.save_dataset(validset,"Training_data/validset.json")