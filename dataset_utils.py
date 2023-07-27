import json
from random import shuffle

path="questions.json"
with open(path,'r') as f:
    dataset = json.load(f)
shuffle(dataset)
tokenized_dataset=[]
labels=[]

"""
import pandas as pd

df = pd.DataFrame.from_dict(dataset)
dataset = datasets.Dataset.from_pandas(pd.DataFrame.from_dict(df))

def tokenize_func(example):
    return tokenizer(example['question'],example['passage])

for elem in dataset: tokenized_dataset.append(tokenize_func(elem))
"""
#for x in dataset: labels.append(0 if x['answer']==1 else 1)

print(dataset[:5])


"""
import json
import datasets
from random import shuffle

path="questions.json"
with open(path,'r') as f:
    dataset = json.load(f)
shuffle(dataset)
tokenized_dataset=[]
labels=[]


import pandas as pd
for x in dataset: labels.append(0 if x['answer']==1 else 1)

df = pd.DataFrame.from_dict(dataset)
df = df.drop('answer',axis=1)
df['labels']=labels
trainset=df[:75]
validset=df[75:]
trainset = datasets.Dataset.from_pandas(pd.DataFrame.from_dict(trainset))
validset = datasets.Dataset.from_pandas(pd.DataFrame.from_dict(validset))

def tokenize_func(example):
    return tokenizer(example['question'],example['passage'], truncation=True)

trainset=trainset.map(tokenize_func, batched=True)
validset=validset.map(tokenize_func, batched=True)


from torch.utils.data import DataLoader

trainset = trainset.remove_columns(["passage", "question", "idx","contest"])
trainset.set_format("torch")
validset = validset.remove_columns(["passage", "question", "idx","contest"])
validset.set_format("torch")

train_dataloader = DataLoader(
    trainset, shuffle=True, batch_size=8, collate_fn=data_collator
)
eval_dataloader = DataLoader(
    validset, batch_size=8, collate_fn=data_collator
)

from transformers import AdamW

optimizer = AdamW(model.parameters(), lr=5e-5)

from transformers import get_scheduler

num_epochs = 2
num_training_steps = num_epochs * len(train_dataloader)
lr_scheduler = get_scheduler(
    "linear",
    optimizer=optimizer,
    num_warmup_steps=0,
    num_training_steps=num_training_steps,
)


"""
