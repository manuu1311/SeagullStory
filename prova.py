from API_setup.Answer_processing import Model
import numpy as np
from gradio_client import Client

model=Model()

to_guess="bob has a girlfriend"
client = Client("https://manuu01-seagullstory.hf.space/")

id2label=["Yes","No"]
while(True):
    question=input("Enter your question\n")
    result = client.predict(
                    "Pier",	# str (Option from: ['General', 'Pier', 'Boat', 'Island'])
                    question,	# str in 'enter your question' Textbox component
                    api_name="/predict"
    )
    print(result)

