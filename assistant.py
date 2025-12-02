import pyttsx3
import datetime
try:
    import speech_recognition as sr
    HAS_SPEECH_RECOGNITION = True
except Exception:
    sr = None
    HAS_SPEECH_RECOGNITION = False
import wikipedia
import webbrowser
import os
import requests
from dotenv import load_dotenv
import re

from currency_converter import convert_currency, convert_bitcoin

load_dotenv()
Weather_API_KEY = os.getenv("Weather_API_KEY")
News_API_KEY = os.getenv("News_API_KEY")

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
voices = engine.getProperty('voices')

print("Choose your preferred voice:")
speak("Choose your preferred voice.")
print("1. Male 👨")
engine.say("Option one - Male voice.")
engine.runAndWait()
print("2. Female 👩")
engine.say("Option two - Female voice.")
engine.runAndWait()
voice_choice = input("Enter 1 or 2: ")

# Set voice based on user preference
voices = engine.getProperty('voices')
if voice_choice == "1":
    engine.setProperty('voice', voices[0].id)  # Male
    print("You have selected Male Voice.\n")
    speak("Hello! You have selected male voice.")
else:
    engine.setProperty('voice', voices[1].id)  # Female
    print("You have selected Female Voice.\n")
    speak("Hello! You have selected female voice.")

# Set properties for speech
engine.setProperty('rate', 180)  # Set speech rate
engine.setProperty('volume', 1)  # Set volume level (0.0 to 1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function to get weather information
def get_weather(city):
    url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Weather_API_KEY}&units=metric"
    res=requests.get(url)
    if res.status_code == 200:
        data=res.json()
        temp= data['main']['temp']
        description = data['weather'][0]['description']
        emoji = get_weather_emoji(description)

        response = f"The weather in {city} is {description} {emoji} with a temperature of {temp}°C."
        print(response)
        speak(response)
    else:
        speak("Sorry, I couldn't fetch the weather for that location.")
#function to return emoji based on weather description
def get_weather_emoji(description):
 desc = description.lower()
 if "clear" in desc:
  return "☀️"
 elif "cloud" in desc:
  return "☁️"
 elif "rain" in desc:
  return "🌧️"
 elif "thunder" in desc:
  return "⛈️"
 elif "snow" in desc:
  return "❄️"
 elif "mist" in desc or "fog" in desc:
  return "🌫️"
 elif "drizzle" in desc:
  return "🌦️"
 else:
  return "🌡️"


# helper to parse a spoken amount into a float
def parse_amount(text):
    if not text:
        return None
    txt = text.replace(',', '').strip().lower()
    if txt == "none":
        return None
    try:
        return float(txt)
    except Exception:
        # try to extract the first number found in the spoken text
        m = re.search(r"(\d+(?:\.\d+)?)", txt)
        if m:
            try:
                return float(m.group(1))
            except Exception:
                return None
    return None

#function to get news headlines
def get_news(query='latest'):
    speak("Sure, let me get the latest news for you.")
    news_url = f'https://newsapi.org/v2/everything?q={query}&apiKey={News_API_KEY}'
    news_response = requests.get(news_url)
    if news_response.status_code == 200:
        news_data = news_response.json()
        articles = news_data['articles']
        if articles:
            for article in articles[:5]:
                title = article['title']
                description = article['description']
                speak(f"Title: {title}")
                if description:
                    speak(f"Description: {description}")
                    print(f"Title: {title}")
                    print(f"Description: {description}")

#function to launch games
def launch_game(game_choice):
   speak("Which game would you like to play?")
   print("Which game would you like to play?")
   print("1. Slowroads")
   speak("Option one - Slowroads.")
   print("2. Sort the Court")
   speak("Option two - Sort the Court.")
   print("3. Tough Love Arena")
   speak("Option three - Tough Love Arena.")
   game_choice= input("Enter 1, 2 or 3: ")
   if game_choice == "1":
     speak("Launching Slowroads.")
     webbrowser.open("https://slowroads.io/")
   elif game_choice == "2":
     speak("Launching Sort the Court.")
     webbrowser.open("https://graebor.itch.io/sort-the-court")
   elif game_choice == "3":
     speak("Launching Tough Love Arena.")
     webbrowser.open("https://toughlovearena.com/")
   else:
     speak("Invalid choice. Unavailable game.")

# function to wish the user based on the time of day
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!") 

    if voice_choice == "1":
     speak("I am Jarvis, your personal assistant. How can I help you today?")  
    else:
     speak("I am Friday, your personal assistant. How can I help you today?")     

def takeCommand():
    # Takes i/p from user using microphone if available, otherwise falls back to text input
    if not HAS_SPEECH_RECOGNITION:
        print("SpeechRecognition not available — falling back to text input.")
        return input("Type your command: ")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2  # Adjusted pause threshold for better recognition
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Sorry, I did not understand that. Please say it again.")
        return "None"
    return query
    
if __name__ == "__main__":
    wish_me()
    while True:
         query= takeCommand().lower()
         
         #Logic for executing tasks based on user query
         #Searching Wikipedia
         if 'wikipedia' in query:
             speak("Searching Wikipedia....")
             query=query.replace("wikipedia", "")
             results=wikipedia.summary(query,sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)

         #Opening websites
         elif 'open youtube' in query:
             webbrowser.open("youtube.com") 
         elif 'open google' in query:
             webbrowser.open("google.com")
         elif 'open spotify' in query:
             webbrowser.open("spotify.com") 
         elif 'open codedex' in query:
             webbrowser.open("codedex.io") 
         elif 'open github' in query:
                webbrowser.open("github.com")
         elif 'open linkedin' in query:
                webbrowser.open("linkedin.com")    
         elif 'open google classroom' in query:
                webbrowser.open("classroom.google.com")
         elif 'open chatgpt' in query:
                webbrowser.open("chat.openai.com")
         elif 'open notion' in query:
                webbrowser.open("notion.so")
         #Getting the current time
         elif 'the time' in query:
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Master, the time is {strTime}")

         #Opening application
         elif 'open vs code' in query:
             codepath="C:\\Users\\Sarthak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codepath)

         #Getting weather information     
         elif "weather" in query:
             speak("Sure, for which city?")
             city = takeCommand()
             get_weather(city)

         #Getting news     
         elif 'news' in query:
            get_news()

         # Currency conversion (fiat and bitcoin)
         elif 'convert' in query or 'currency' in query or 'bitcoin' in query:
            speak("Sure — do you want to convert Bitcoin or regular currency?")
            choice = takeCommand().lower()
            if 'bitcoin' in choice or 'btc' in choice:
                speak("How many bitcoins would you like to convert?")
                amt_text = takeCommand()
                amt = parse_amount(amt_text)
                if amt is None:
                    speak("I couldn't understand the amount. Please try again later.")
                else:
                    speak("Which currency should I convert Bitcoin to? Say the three-letter code like USD or INR.")
                    currency = takeCommand()
                    if not currency or currency.lower() == 'none':
                        speak("No currency provided. Cancelling conversion.")
                    else:
                        currency_code = ''.join(currency.split()).upper()
                        result = convert_bitcoin(amt, currency_code)
                        print(result)
                        speak(result)
            else:
                speak("How much would you like to convert? Say the amount.")
                amt_text = takeCommand()
                amt = parse_amount(amt_text)
                if amt is None:
                    speak("I couldn't understand the amount. Please try again later.")
                else:
                    speak("From which currency? Please say the three-letter currency code like USD or INR.")
                    from_curr = takeCommand()
                    if not from_curr or from_curr.lower() == 'none':
                        speak("No source currency provided. Cancelling conversion.")
                    else:
                        from_code = ''.join(from_curr.split()).upper()
                        speak("To which currency should I convert?")
                        to_curr = takeCommand()
                        if not to_curr or to_curr.lower() == 'none':
                            speak("No target currency provided. Cancelling conversion.")
                        else:
                            to_code = ''.join(to_curr.split()).upper()
                            result = convert_currency(amt, from_code, to_code)
                            print(result)
                            speak(result)
        
         #To get jokes or motivational quotes
         elif 'joke' in query:
            speak("Sure, let me tell you a joke.")
            joke_response = requests.get("https://official-joke-api.appspot.com/random_joke")
            if joke_response.status_code == 200:
                joke_data = joke_response.json()
                joke = f"{joke_data['setup']} {joke_data['punchline']}"
                print(joke)
                speak(joke)

         elif 'motivate me' in query or 'motivation' in query:
            speak("Sure, here is a motivational quote for you.")
            quote_res = requests.get("https://zenquotes.io/api/random")
            if quote_res.status_code == 200:
                quote_data = quote_res.json()[0]
                quote = f"{quote_data['q']} - {quote_data['a']}"
                print(quote)
                speak(quote)
         
         #To take notes
         elif 'note' in query:
            speak("Sure, what would you like to note down?")
            note = takeCommand()
            with open("notes.txt", "a") as file:
                file.write(note + "\n")
            speak("Note has been saved.")
            speak("Would you like to rename the file?")
            rename_choice = takeCommand().lower()
            if 'yes' in rename_choice:
                speak("Please provide the new name for the file.")
                new_name = takeCommand()
                os.rename("notes.txt", f"{new_name}.txt")
                speak(f"File has been renamed to {new_name}.txt")
            else:
                speak("Note saved without renaming the file.")
            speak("Would you like to read the notes?")
            read_choice = takeCommand().lower()
            if 'yes' in read_choice:
                speak("Here are your notes:")
                with open("notes.txt", "r") as file:
                    notes = file.read()
                    print(notes)
                    speak(notes)
            else:
                speak("Okay, I won't read the notes.")
                print("Okay, I won't read the notes.")

         # To-Do List Feature
         elif 'add task' in query:
          speak("What task would you like to add?")
          task = takeCommand().capitalize()
          with open("todo.txt", "a") as file:
           file.write(task + "\n")
           speak(f"I've added the task: {task}")
           print(f"Added task: {task}")

         elif 'show tasks' in query or 'read my tasks' in query:
          if os.path.exists("todo.txt"):
           with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
             speak("Here are your tasks:")
            for idx, task in enumerate(tasks, 1):
                speak(f"Task {idx}: {task.strip()}")
                print(f"{idx}. {task.strip()}")
            else:
             speak("Your to-do list is empty.")
             print("No tasks found.")
         
         elif 'remove task' in query or 'delete task' in query:
          speak("What task would you like to remove?")
          task_to_remove = takeCommand().capitalize()
          if os.path.exists("todo.txt"):
           with open("todo.txt", "r") as file:
            tasks = file.readlines()
           with open("todo.txt", "w") as file:
            for task in tasks:
             if task.strip() != task_to_remove:
              file.write(task)
             else:
              speak(f"I've removed the task: {task_to_remove}")
              print(f"Removed task: {task_to_remove}")
          else:
           speak("Your to-do list is empty.")
           print("No tasks found.")

         # To Play Game
         elif 'play game' in query or 'I want to play a game' in query or "Let's play a game" in query or 'game' in query:
             launch_game(query)

         # To exit the program
         elif 'quit' in query or 'bye' in query or 'exit' in query or 'stop' in query or 'goodbye' in query:
          speak("Thank you! Have a great day!")
          print("Thank you! Have a great day!")
          break 
         else:
          speak("I am sorry, I cannot help you with that. Please try something else.")
