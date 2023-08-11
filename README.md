# SeagullStory
This is a simple game being developed by two Computer Science students in their free time.

## The game
Two friends, Bob and Tom are at a pier. They go to a restaurant, Bob orders seagull meat, he takes a bite and then he shoots himself.\n\n

This is the final part of a story. It does not make sense at first, but in the end you can be sure it will actually make sense.\n
You can ask boolean questions to which you will receive one of the following answers:\n
"Yes" if it is true\n
"No" if it is not true\n
"Doesn't matter" if what you're asking is not important to understand the whole story.\n
Example: Bob liked the restaurant                                   --Answer: Doesn't matter\n
         Bob shot himself because he did not have money to pay      --Answer: No\n

## How we approached the problem
We reduced the problem to a NLI task. We used a BERT-like model fine-tuned on NLI datasets and finally our own dataset. Then, we want to deploy the model 
and use It with an API. This way, we want to be able to play It as a github app, using a telegram bot and finally make It a mobile app.

## The model
The model base is DeBERTa-v2. It has been fine-tuned on [multi-nli](https://huggingface.co/datasets/multi_nli), [anli](https://huggingface.co/datasets/anli), 
[fever](https://huggingface.co/datasets/fever) datasets accessible on [🤗Hugging Face](https://huggingface.co/) and [finally our own dataset](link al dataset).\n


| -------------------------------------------------|:------:|
| Creating dataset based on our story              |   ✅    |
| Find a suitable model                            |   ✅    |
| Fine-tuning the model                            |   ✅    |
| Deploy model as API                              |   🔲    |
| Github app                                       |   🔳    |
| Telegram bot                                     |   🔳    |
| Mobile app                                       |   🔳    |


