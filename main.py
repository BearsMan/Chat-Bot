import random
from typing import Pattern
import nltk
from nltk.chat.util import Chat, reflections
import datetime
import pytz
from nltk.sentiment import SentimentIntensityAnalyzer

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
def get_current_time(user_timezone):
  try:
    # Parse the user's timezone input
    timezone = pytz.timezone(user_timezone)
    get_current_time = datetime.datetime.now(timezone)
    return get_current_time.strftime("%H:%M:%S")
  except pytz.exceptions.UnknownTimeZoneError:
    return "Invalid timezone. Please enter a valid timezone."
    eastern = pytz.timezone('US/Eastern')
    western = pytz.timezone('US/Pacific')
    northern = pytz.timezone('US/Central')
    southern = pytz.timezone('US/Mountain')
def seniment_analysis(text):
  # Get the user's input
  user_input = input("Enter a sentence: ")
  sid = SentimentIntensityAnalyzer()
  score = sid.polarity_scores(text)['compound']
  if score >= 0.05:
    return "You are very positive!"
  elif score <= -0.05:
    return "You are neutral."
  else:
    return "You are very neutral!"
def chat_with_bot():
    print("Hello! I am Chatbot. How can I assist you today?")
    while True:
        user_input = input("You:")
        sentiment = seniment_analysis(user_input)
        if sentiment is not None:
          
          respond = f"(sentiment: {sentiment})"
          print(f"sentiment: {sentiment}")
        if "joke" in user_input:
            print("chat_bot", generate_joke())
        elif "time" in user_input:
            user_timezone = input("Please enter your timezone (e.g., America/New_York): ")
            current_time = get_current_time(user_timezone)
            print("The current time is:", current_time)
        else:
            print(respond)
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chat_bot.respond(user_input)
        # print("Chatbot:", response)
if __name__ == "__main__":
  chat_with_bot()