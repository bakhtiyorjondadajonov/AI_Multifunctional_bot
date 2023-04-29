import requests
import json
import re

# Set up OpenAI API credentials
API_KEY = "Open AI API key"


def summarize(text):
    prompt = f"Please summarize the following text:\n{text}"
    response = query_api(prompt)
    summary = response.strip()
    return summary


def paraphrase(text):
    prompt = f"Please paraphrase the following sentence:\n{text}"
    response = query_api(prompt)
    paraphrase = response.strip()
    return paraphrase


def translate(text, lang):
    prompt = f"Please translate  the following sentence into {lang} language:\n{text}"
    response = query_api(prompt)
    paraphrase = response.strip()
    return paraphrase


def chat():
    print("Hi, I am your ChatBot. How may I assist you?")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "bye":
            print("ChatBot: Bye!")
            break
        elif "?" in user_input:
            prompt = f"Q: {user_input}\nA:"
            response = query_api(prompt)
            chatbot_response = response.strip()
            print("ChatBot:", chatbot_response)
        else:
            print(
                "ChatBot: I'm sorry, I can only answer questions. Please ask a question.")


def query_api(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    data = {
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 60,
        "n": 1,
        "stop": None,
    }
    response = requests.post("https://api.openai.com/v1/engines/text-davinci-002/completions", headers=headers,
                             data=json.dumps(data))
    response_json = json.loads(response.text)
    text = response_json["choices"][0]["text"]
    return text


if name == 'main':
    print("Welcome to the AI Chatbot!")
    print("This program can summarize, paraphrase, and chat with you.\n")
    while True:
        print("Please select an option:")
        print("1. Summarize text")
        print("2. Paraphrase a sentence")
        print("3. Chat with the ChatBot")
        print("4. Translate a text")
        print("5. Exit program\n")
        user_input = input("Enter your choice (1/2/3/4/5): ")
        if user_input == "1":
            text = input("\nEnter the text to summarize: ")
            summary = summarize(text)
            print("\nSummary:", summary)
        elif user_input == "2":
            text = input("\nEnter the sentence to paraphrase: ")
            paraphrase = paraphrase(text)
            print("\nParaphrase:", paraphrase)
        elif user_input == "3":
            chat()
        elif user_input == "4":
            lang = input("Please enter the language that you want translate: ")
            text = input("Enter the sentence to translate: ")
            translate = translate(text, lang)
            print(f"\nTranslation: {translate}")
        elif user_input == "5":
            print("\nThank you for using the AI Chatbot!")
            break

        else:
            print("\nInvalid choice. Please try again.")
