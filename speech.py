import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except Exception as e:
            print("Sorry, I didn't catch that. Please try again.")
            return "None"
        return command.lower()
def get_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {now}")

def get_date():
    today = datetime.date.today()
    speak(f"Today's date is {today}")

def search_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    speak(f"According to Wikipedia: {results}")

def open_website(url):
    webbrowser.open(url)
    speak(f"Opening {url}")
def main():
    speak("Hello, how can I help you today?")
    
    while True:
        command = listen()
        
        if 'time' in command:
            get_time()
        elif 'date' in command:
            get_date()
        elif 'wikipedia' in command:
            speak("What should I search on Wikipedia?")
            query = listen()
            search_wikipedia(query)
        elif 'open' in command:
            speak("Which website should I open?")
            website = listen().replace(' ', '')
            open_website(f"https://{website}.com")
        elif 'stop' in command:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand that command.")

if __name__ == "_main_":
    main()