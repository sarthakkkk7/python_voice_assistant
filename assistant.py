import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


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
    #Takes i/p from user using microphone

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")   

    except Exception as e:
        print("Sorry, I did not understand that. Please say it again.")
        return "None"   
    return query  
    
if __name__ == "__main__":
    wish_me()
    #while True:
    if 1:
         query= takeCommand().lower()
         
         #Logic for executing tasks based on user query
         if 'wikipedia' in query:
             speak("Searching Wikipedia....")
             query=query.replace("wikipedia", "")
             results=wikipedia.summary(query,sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com") 
         elif 'open google' in query:
             webbrowser.open("google.com")
         elif 'open spotify' in query:
             webbrowser.open("spotify.com") 
         elif 'open codedex' in query:
             webbrowser.open("codedex.io") 
         elif 'the time' in query:
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Master, the time is {strTime}")
         elif 'open vs code' in query:
             codepath="C:\\Users\\Sarthak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codepath)
         else:
                speak("I am sorry, I cannot help you with that. Please try something else.")


             



             

