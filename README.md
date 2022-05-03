
# ChatBot In Python

A simple chat bot in Python with links to smart conversational with this project [vicky](https://github.com/rebal221/vicky) for frontend and this [Chatbot_and_FlutterApp_API](https://github.com/rebal221/Chatbot_and_FlutterApp_API) for server
## Installation

First you must download the above projects and follow the steps

For create envermant for install the packages write this in the terminal :
```shel
     (your python version Ex 3)
        python3 -m venv venv
```
 
After that, you need to install the packages :
```shel
     pip3 install -r requirements.txt
```

Now change this links to your project path :
```python
     model = load_model('YOUR PATH /ChatBot/chatbot_model.h5')
```
```python
     intents = json.loads(open('YOUR PATH /ChatBot/assets/intents.json').read())
```
```python
     words = pickle.load(open('YOUR PATH /ChatBot/words.pkl','rb'))
```
```python
     classes = pickle.load(open('YOUR PATH /ChatBot/classes.pkl','rb'))
```

When completing Run the project :
```shel
     python3 chatapp.py
```

## Author

- [Rebal Aljrmani](https://github.com/rebal221)