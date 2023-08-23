# SeagullStory
This is a simple game being developed by two Computer Science students in their free time.

## The game
Two friends, Bob and Tom are at a pier. They go to a restaurant, Bob orders seagull meat, he takes a bite and then he shoots himself.  
  
This is the final part of a story. It does not make sense at first, but in the end you can be sure it will actually make sense.  
  
You can ask boolean questions to which you will receive one of the following answers: 
  
"Yes" if it is true  
"No" if it is not true  
"Doesn't matter" if what you're asking is not important to understand the whole story.  
  
Example: Bob liked the restaurant                                   
--Answer: Doesn't matter  
         Bob shot himself because he did not have money to pay      
         --Answer: No  
  
## How we approached the problem
We reduced the problem to a NLI task. We used a BERT-like model fine-tuned on NLI datasets and finally our own dataset. Then, we want to deploy the model 
and use It with an API. This way, we want to be able to play It as a github app, using a telegram bot and finally make It a mobile app.  

## The model
The model base is [DeBERTa-v3](https://huggingface.co/microsoft/deberta-v3-base). It has been fine-tuned on [multi-nli](https://huggingface.co/datasets/multi_nli), [anli](https://huggingface.co/datasets/anli), 
[fever](https://huggingface.co/datasets/fever) datasets accessible on [🤗Hugging Face](https://huggingface.co/) and [finally our own dataset](https://github.com/manuu1311/SeagullStory/tree/main/Training_data).  
  
Then, we used an auxiliary model based on (xtremedistil)[https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased]. 
This model will predict binary labels, "Yes" and "No". We will use this model in order to monitor user progress. It has been fine tuned 
on several nli datasets where the "Neutral" and "Conctradiction" labels have been merged since the difference is irrelevant (with the weights being adjusted 
accordingly during training).  
We want to deploy the model within the app, so it has been quantized and converted to tflite (the final size is 12.4 Mb).

|                                                  |        |
| -------------------------------------------------|:------:|  
| Creating dataset based on our story              |   ✅    |  
| Find suitable models                             |   ✅    |  
| Fine-tuning the models                           |   ✅    |  
| Deploy model as API                              |   ✅    |  
| Convert auxiliary model to tflite                |   ✅    |  
| Mobile app                                       |   🔲    |  



(This hugging face space)[https://huggingface.co/spaces/manuu01/SeagullStory] hosts a demo of the final model inference.


