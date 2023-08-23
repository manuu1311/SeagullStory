import tflite_runtime.interpreter as tflite
from tokenizers import Tokenizer



class Model:
  def __init__(self,path):
        self.length=128     #max input length
        self.tokenizer=Tokenizer.from_file(path+"tokenizer.json")
        self.interpreter = tflite.Interpreter(model_path=path+"model.tflite")
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()



  def get_predict(self,passage,question):
    input=self.tokenizer.encode(passage,question)
    padded_input_ids = input.ids + [0] * (self.length - len(input.ids))
    padded_attention_mask = input.attention_mask + [0] * (self.length - len(input.attention_mask))
    padded_token_type_ids=input.type_ids+[0]*(self.length-len(input.type_ids))
    self.interpreter.set_tensor(self.input_details[0]['index'], [padded_attention_mask])
    self.interpreter.set_tensor(self.input_details[1]['index'], [padded_input_ids])
    self.interpreter.set_tensor(self.input_details[2]['index'],[padded_token_type_ids])
    self.interpreter.invoke()
    return self.interpreter.get_tensor(self.output_details[0]['index'])


