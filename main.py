import random
from typing import Pattern
import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot's responses
Pattern = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I am fine, thanks for asking.']),
    (r'what is your name', ['My name is Chatbot.', 'I am Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!']),
    (r'(.*)', ['I am sorry, I did not understand your question.'])
]
chat_bot = Chat(Pattern, reflections)
def chat_with_bot():
    print("Hello! I am Chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chat_bot.respond(user_input)
        print("Chatbot:", response)
if __name__ == "__main__":
  chat_with_bot()