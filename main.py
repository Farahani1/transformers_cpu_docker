import os
from transformers import AutoConfig, AutoTokenizer, AutoModel

file_path = os.environ.get("BERT_FILES_PATH")

config = AutoConfig.from_pretrained(file_path)
tokenizer = AutoTokenizer.from_pretrained(file_path)
model = AutoModel.from_pretrained(file_path)

text = " هوش مصنوعی برای همه است"

t = tokenizer.tokenize(text)

print('end')

