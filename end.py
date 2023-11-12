import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import random
import spacy
from spacy.lang.ru.examples import sentences
import warnings
warnings.filterwarnings("ignore")
model_checkpoint = 'cointegrated/rubert-base-cased-nli-threeway'
filename ="output.csv"

reader = pd.read_csv(filename)
question = reader['question']
questions = []

for i in question:
  questions.append(i)

answers_merged = []
answer2 = reader['answers_merged']
for j in answer2:
  answers_merged.append(j)
ans_m = []
for i in range(len(answers_merged)):
  an = answers_merged[i][2:len(answers_merged[0]) - 2]
  an = an.replace(']', '')
  an = an.replace('\\n', '')
  an = an.replace("'", "").split('.,')
  ans_m.append(an)


answers = []
answer1 = reader['answer_summary']
for j in answer1:
  answers.append(j)

dic = {}
for i in range(len(answers)):
    dic[question[i]] = answers[i]





def semantic(text1, text2):

  tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
  model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint)
  if torch.cuda.is_available():
      model.cuda()
  with torch.inference_mode():
      out = model(**tokenizer (text1, text2, return_tensors='pt').to(model.device))
      proba = torch.softmax(out.logits, -1).cpu().numpy()[0]

  fin_dict = {v: proba[k] for k, v in model.config.id2label.items()}
  l1 = max(fin_dict, key=fin_dict.get)

  with torch.inference_mode():
      out = model(**tokenizer (text2, text1, return_tensors='pt').to(model.device))
      proba = torch.softmax(out.logits, -1).cpu().numpy()[0]

  fin_dict = {v: proba[k] for k, v in model.config.id2label.items()}

  l2 = max(fin_dict, key=fin_dict.get)
  if l2 == 'entailment':
    return l2
  else:
    return l1




nlp = spacy.load("ru_core_news_sm")

n = 0
keys = list(dic.keys())
def g_q():
  global n
  n = random.choice(keys)
  return n


def f_inp(inp):
  while True:
    if semantic(inp, dic[n]) == 'entailment':
      return 'Верно'
    else:
      return 'Неверно' + "\n" + dic[n]