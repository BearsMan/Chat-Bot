import random
from typing import Pattern
import nltk
from nltk.chat.util import Chat, reflections
import datetime
import pytz
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')


'''
Hey Darius!! We'll go over these next class:
1. Creating a variable for the sentiment analysis analyzer
2. Fixing the timezone function

''' 

# Define the chatbot's responses
Pattern = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?| How is your day today?| How is it going?', ['I am doing well, thank you.', 'I am fine, thanks for asking.']),
    (r'what is your name', ['My name is Chatbot.', 'I am Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!']),
    (r'What is the weather today?', ['The weather today is sunny and warm.',"The weather today is cold."]),  
    (r'Tell me a joke', ["Knock knock, whose there? Dewayne, Dewayne who? Drain the tub, I'm  drowning."]),
  (r'LOL!|HAHA!|XD!|LOL', ['LOL!','HAHA!','XD']),]

def generate_joke():
  #Add jokes in the list below 
    jokes = [
        "Who is the coolest Doctor in the hospital? The hip Doctor!",
        "Why dont scientists trust atoms? Because they make up everything!",
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
  
  sid = SentimentIntensityAnalyzer()
  score = sid.polarity_scores(text)['compound']
  if score >= 0.05:
    return "You are very positive!"
  elif score <= -0.05:
    return "You are being negative."
  else:
    return "You are being neutral!"
def chat_with_bot():
    print("Hello! I am Chatbot. How can I assist you today?")
    while True:
        user_input = input("You:")
        respond = chat_bot.respond(user_input)
        sentiment = seniment_analysis(user_input)

        if "joke" in user_input:
          print("chat_bot", generate_joke())
        elif "time" in user_input:
          user_timezone = input("Please enter your timezone (e.g. America/New_York): ")
          current_time = get_current_time(user_timezone)
          print("The current time is:", current_time)
        elif user_input.lower() == 'quit':
          print("Chatbot: Goodbye!")
          break
        else:
          sentiment_category = seniment_analysis(user_input)
          response = chat_bot.respond(user_input)
        
        if sentiment_category is not None:
          
          response = f"(sentiment: {sentiment_category})"

          postive_respond = ["Tell me more about your day." + response, "Great job today, What else is new?" + response, "I am happy to hear that."+ response, "That's great to hear."+ response, "I am glad to hear that"+ response]
          
          neutral_respond = ["That is interesting."+ response, "That's cool."+ response, "I see."+ response, "That's good to know."+ response, "I understand."+ response]
          
          negative_respond = ["I am sorry that this has happened to you." + response, "I am so sorry to hear that"+ response, "If you need to talk, I am here."+ response, "I am here to listen."+ response, "I am here to help."+ response]
        if sentiment_category == "You are very positive!":
            print("chat_bot", random.choice(postive_respond))
        elif sentiment_category == "You are being negative.":
            print("chat_bot", random.choice(negative_respond))
        else:
            print("chat_bot", random.choice(neutral_respond))
        
          
        
        # print("Chatbot:", response)
if __name__ == "__main__":
  chat_with_bot()