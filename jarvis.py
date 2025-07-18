import speech_recognition as sr
import wikipedia as wk
import openaiclient as opai
import pyaudio as paud
import win32com.client
import webbrowser
import subprocess
import os
from playsound import playsound 
import datetime
from AppOpener import open



speaker = win32com.client.Dispatch("SAPI.SpVoice")

sites = {
    "youtube" : "https://youtube.com",
    "classroom" : "https://classroom.google.com",
    "wikipedia" : "https://www.wikipedia.org/",
    "amazon": "https://www.amazon.in/",
    "flipkart": "https://www.flipkart.com/",
    "gmail": "https://mail.google.com/mail/u/0/#inbox",
    "github" : "https://github.com/",

}

drives={'c', 'd'}

apps={"camera", "calculator", "clock", "google chrome","whatsapp","telegram","notepad","vlc media player","microsoft edge","word","excel","powerpoint"}

def speak(text):
    speaker.Speak(text)

def listen():
    r = sr.Recognizer()
    
    

    try:
        with sr.Microphone() as source:
            r.pause_threshold = 1
            
            audio = r.listen(source)

            query = r.recognize_google(audio,language="en-in")
            return query

    except Exception:
        return "Sorry, unknown error occurred, Please try again"

if __name__ == '__main__':
    
    speak("Jarvis, your personal A.I.")

    while True:
        print("listening...")
        query = listen().lower()

        for site in sites:
            if f"open {site}" in query:
                speak(f"Opening {site} for you")
                webbrowser.open(sites[site])

        for drive in drives:
            if f"open {drive} drive" in query:
                speak(f"Opening {drive} drive for you")
                subprocess.Popen(f'explorer "{drive.upper()}:\\"')

        for app in apps:
            if f"open {app}" in query:
                speak(f"Opening {app} for you")
                open(f"{app}")


        if "play music" in query:
            speak(f"Playing Music for you")
            playsound(r"C:\Users\DELL\OneDrive\Documents\Sound Recordings\jarvis.mp3" )

        elif "what time" in query:
            speak("Current time is "+ datetime.datetime.now().strftime("%H:%M:%S"))
            
        elif "shutdown" in query:
            speak("Shutting down")
            break
      


