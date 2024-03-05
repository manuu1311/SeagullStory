import tensorflow.lite as tflite
from tokenizers import Tokenizer
from numpy import array,int64
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
    padded_input_ids = array(input.ids + [0] * (self.length - len(input.ids)),dtype=int64)
    padded_attention_mask = array(input.attention_mask + [0] * (self.length - len(input.attention_mask)),dtype=int64)
    padded_token_type_ids=array(input.type_ids+[0]*(self.length-len(input.type_ids)),dtype=int64)
    self.interpreter.set_tensor(self.input_details[0]['index'], [padded_attention_mask])
    self.interpreter.set_tensor(self.input_details[1]['index'], [padded_input_ids])
    self.interpreter.set_tensor(self.input_details[2]['index'],[padded_token_type_ids])
    self.interpreter.invoke()
    return self.interpreter.get_tensor(self.output_details[0]['index'])