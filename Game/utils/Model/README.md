## How we approached the problem
I reduced the problem to a NLI task and used two BERT-like models. The primary one is larger, while the other is used as a utility for tracking user progress. Both are trained on appropriate datasets, as well as my own specific to this story.  I deployed the bigger model as an API (thanks to [HuggingFace](https://huggingface.co/) spaces), the other is deployed locally. For that reason, the latter has been quantized and converted to tflite, achieving the final size of 12.4Mb.

## The model
The [bigger model](https://huggingface.co/manuu01/DeBERTa-SeagullStory) is based on [DeBERTa-v3](https://huggingface.co/microsoft/deberta-v3-base), while the auxiliary model is based on [xtremedistil-l6-h256](https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased).  
This model predicts binary labels, "Yes" and "No". This model is used to track user progress and to enable unlocking new scenarios. It has been fine-tuned on several datasets where the "Neutral" and "Conctradiction" labels have been merged since the difference is irrelevant (with the weights being adjusted accordingly during training).
  
## Answer processing
We defined several key facts for progression and for unlocking new scenarios.
Both the models accept a passage and a question, then, they output the predicted label. For the local model, the user question is used as 'passage', while each key fact  is used as 'question' (which is equivalent to asking: 'does the user question entail the key fact? If so, It means he found out about It). 
In the main model, instead, the passage is a thorough description of what happens in a specific scenario, and the question is of course the user's.  

Ultimately, when the user asks a question in a scenario, this is what happens:
User question   
▶️ auxiliary model inference: for each key fact, did the user find out about It?  
Yes ▶️ popup message for the user, for guidance, progress bar increases  
No  ▶️ main model inference via API  
▶️ Answer(Yes,No,Doesn't matter)  
