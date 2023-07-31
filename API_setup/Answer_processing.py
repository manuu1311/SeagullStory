#supposing 2 sentences are sent to the api
from os.path import dirname

#transformers is needed
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import numpy as np

#loading model and tokenizer
checkpoint="distilbert-base-uncased"
path="/distilbert"
model = TFAutoModelForSequenceClassification.from_pretrained(f'{dirname(__file__)}/distilbert/')
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

#given passage and question, returns "yes" or "no"
def get_predict(passage,question):
  inputs=tokenizer(question,passage, return_tensors="tf")
  return model.config.id2label[np.argmax(model(**inputs).logits)]

