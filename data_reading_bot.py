# -*- coding: utf-8 -*-
"""Data_Reading_Bot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12UdGvc9U4jzrVkBAXx7YbJaM2MxxJSfV
"""

import numpy as np
import nltk
import string 
import random

"""Reading the Corpus of Text"""

#upload your main data location path 
f = open('/content/datatext.txt','r',errors = 'ignore')
raw_doc = f.read()

raw_doc = raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

sentence_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

"""After token"""

sentence_tokens[3
                ]

word_tokens

"""Text-preprocessing steps"""

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
  return[lemmer.lemmatize(token) for token in tokens]
remove_punc_dict = dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.loer().translate(remove_punc_dict)))

"""greeting function"""

greet_inputs = ('hello','hi','hii','how are you?')
greet_responses = ('hey','hey there')
def greet(sentence):
  for word in sentence.split():
    if word.lower() in greet_inputs:
      return random.choice(greet_responses)

"""Response generation by the bot """

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
  robol_response = ''
  Tfidfvec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english')
  tfidf = Tfidfvec.fit_transform(sentence_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx = vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if (req_tfidf == 0):
    robo1_response = robo1_response + "I am sorrt. Unable to understand you!"
    return robo1_response
  else:
    robo1_response = robo1_response+ sentence_tokens[idx]
    return robo1_response

"""Define the chatflow"""

flag = True
print('Hello i am learning Bot. start typing your text after greeting to talk to me. For ending convo type bye!')
while(flag == True):
  user_response = input()
  user_response = user_response.lower()
  if(user_response != 'bye'):
    if(user_response == 'thank you' or user_response == 'thank'):
      flag = False
      print('Bot: You are Welcome..')
    else:
      if(greet(user_response) != None):
        print('Bot '+ greet(user_response))
      else:
        sentence_tokens.append(user_response)
        word_tokens = word_tokens + nltk.word_tokenize(user_response)
        final_words = list(set(word_tokens))
        print('Bot: ',end = '')
        print(response(user_response))
        sentence_tokens.remove(user_response)
  else:
    flag = False
    print('Bot: Goodbye!')