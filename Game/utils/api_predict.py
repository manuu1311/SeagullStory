from gradio_client import Client



class api_predict:
    def __init__(self):
        self.api =Client("https://manuu01-seagullstory.hf.space/")

    def api_predict(self,question, passage):
        result = self.api.predict(
                        passage,	# str (Option from: ['General', 'Pier', 'Boat', 'Island'])
                        question,	# str in 'enter your question' Textbox component
                        api_name="/predict"
        )
        return result
