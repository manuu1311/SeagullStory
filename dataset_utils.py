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
