# AI_Multifunctional_bot Documentation

## Link for the video of our team presentation https://drive.google.com/file/d/1wOqbvJZWaSoXGp-WM_8HB9loZY4vxlGp/view?usp=sharing

This program provides the following functionalities:

## Summarize text:
Given a block of text, it generates a concise summary of the text.
Paraphrase a sentence: Given a sentence, it generates a rephrased version of the sentence.
Chat with the ChatBot: The user can ask any question, and the ChatBot will try to provide a relevant answer.
Translate a text: Given a sentence and a language, it generates a translation of the sentence in the specified language.
Installation
To use this program, you will need Python 3.x installed on your system. You can download and install it from the official Python website: https://www.python.org/downloads/.

Once you have installed Python, you need to install the following dependencies:

requests: Used for making HTTP requests to the OpenAI API
json: Used for handling JSON data
re: Used for regular expression matching
You can install these dependencies using pip. Open your command prompt or terminal and enter the following command:

Copy code
```
pip install requests
```
Usage
To run the program, open your command prompt or terminal and navigate to the directory where the code is saved. Then, enter the following command:

Copy code
### AI_bot_Tech_titans.py
This will launch the program, and you will see a menu with the available options. Enter the number corresponding to the option you want to use, and follow the prompts.

Functions
The program has four main functions:

```
summarize(text)
```
Given a block of text, it generates a concise summary of the text.
```
paraphrase(text)
```
Given a sentence, it generates a rephrased version of the sentence.
```
chat()
```
Starts a conversation with the ChatBot.
```
translate(text, lang)
```
Given a sentence and a language, it generates a translation of the sentence in the specified language.
API Credentials
To use the OpenAI API, you need to set up an account and obtain an API key. You can create an account and obtain your API key from the OpenAI website: https://openai.com/.

Once you have your API key, replace the placeholder value in the API_KEY variable at the top of the chatbot.py file with your actual API key.

Limitations
The OpenAI API has usage limits, so you may run into issues if you use the program too frequently or with very large inputs. Additionally, the program may not always provide accurate or relevant responses, as the quality of the output depends on the underlying AI models used by the OpenAI API.
