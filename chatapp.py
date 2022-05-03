from tokenize import String
from typing import Literal
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model
model = load_model('/home/rebal/Projects/Python_Projects/ChatBot/chatbot_model.h5')
import json
import random
import tkinter
from tkinter import *
from flask import Flask, request 
   
intents = json.loads(open('/home/rebal/Projects/Python_Projects/ChatBot/assets/intents.json').read())
words = pickle.load(open('/home/rebal/Projects/Python_Projects/ChatBot/words.pkl','rb'))
classes = pickle.load(open('/home/rebal/Projects/Python_Projects/ChatBot/classes.pkl','rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words
    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words) 
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))
    
def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result
def chatbot_response(text):
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res

def chat(inp):
    msg = inp
    if msg != '':
        res = chatbot_response(msg)
        return res  

# Setup flask server
app = Flask(__name__) 
@app.route('/', methods = ['POST']) 
def getData(): 
    data = request.get_data(as_text=Literal[False]) 
    result = chat(data)  
    print(result)
    return str(result)
   
if __name__ == "__main__": 
    app.run(port=5000)
