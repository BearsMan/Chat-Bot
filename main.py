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
    (r'What is the weather today?', ['The weather today is sunny and warm.',"The weather today is cold."]),  
    (r'Tell me a joke', ["Knock knock, whose there? Dewayne, Dewayne who? Drain the tub, I'm  drowning."]),
  (r'LOL!|HAHA!|XD!|LOL', ['LOL!','HAHA!','XD']),]
def generate_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!", "Why did the toy cross the road? To get to chicken the other side!",]
    return random.choice(jokes)
# Create the chatbot
chat_bot = Chat(Pattern, reflections)
def chat_with_bot():
    print("Hello! I am Chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if "Joke" in user_input:
            print("chat_bot", generate_joke())
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chat_bot.respond(user_input)
        print("Chatbot:", response)
if __name__ == "__main__":
  chat_with_bot()