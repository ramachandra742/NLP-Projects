import json

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import *

with open("/home/rama/Desktop/Rama/NLP projects/BERTModel-for-Sentiment-Analysis/app/config.json") as json_file:
    config=json.load(json_file)

class SentimentClassifier(nn.Module):
    def __init__(self,n_classes):
        super(SentimentClassifier,self).__init__()
        self.bert = BertModel.from_pretrained(config['BERT_MODEL'])
        self.drop = nn.Dropout(p=0.5)
        self.out = nn.Linear(self.bert.config.hidden_size, n_classes)

    def forward(self,input_ids,attention_mask):
        last_hidden_state, pooled_output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        output = self.drop(pooled_output)
        return self.out(output)
