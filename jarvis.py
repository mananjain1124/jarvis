import speech_recognition as sr
import win32com.client
import webbrowser
import subprocess
import os
import pyautogui 
import requests
import ctypes
import datetime
import time
import pythoncom
import msvcrt  # Built-in Windows library for keyboard input
from ai_handler import get_response 
from config import weather_apikey

# Initialize Text-to-Speech
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    """
    Speaks text. 
    Press 'SPACEBAR' in the console to stop immediately.
    """
    print(f"Jarvis: {text}")
    
    try:
        # 1. Speak the WHOLE text in the background (Async Mode)
        # We do NOT split sentences anymore. This fixes the "skipping" bug.
        speaker.Speak(text, 1) 

        # 2. Wait loop: Runs while Jarvis is speaking
        while speaker.Status.RunningState == 2:
            
            # Check if User pressed a key
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b' ': # ASCII for SPACEBAR
                    # Flag 2 = Purge (Kill all audio immediately)
                    speaker.Speak("", 2) 
                    print("\n[Muted by User]")
                    return

            # Tiny sleep to prevent CPU overload
            time.sleep(0.01)
            pythoncom.PumpWaitingMessages()
            
    except Exception as e:
        print(e)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("\nListening... (Click window and press SPACE to stop speaking)")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            query = r.recognize_google(audio, language="en-in")
            print(f"User: {query}")
            return query.lower()
        except Exception:
            return "none"

# --- SYSTEM CONTROLS ---
def system_control(command):
    if "volume up" in command:
        pyautogui.press("volumeup")
        speak("Volume increased")
    elif "volume down" in command:
        pyautogui.press("volumedown")
        speak("Volume decreased")
    elif "mute" in command:
        pyautogui.press("volumemute")
        speak("System muted")
    elif "screenshot" in command:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"screenshot_{timestamp}.png"
        pyautogui.screenshot(file_name)
        speak(f"Screenshot taken")
    elif "lock system" in command:
        speak("Locking system")
        ctypes.windll.user32.LockWorkStation()

# --- SYSTEM APPS ---
def open_system_app(command):
    if "notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
    elif "calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")
    elif "task manager" in command:
        speak("Opening Task Manager")
        subprocess.Popen("taskmgr")
    elif "settings" in command:
        speak("Opening Settings")
        subprocess.Popen("start ms-settings:", shell=True)
    elif "camera" in command:
        speak("Opening Camera")
        subprocess.run('start microsoft.windows.camera:', shell=True)
    elif "whatsapp" in command:
        speak("Opening WhatsApp")
        try:
            subprocess.run('start whatsapp:', shell=True)
        except:
            speak("Opening WhatsApp Web")
            webbrowser.open("https://web.whatsapp.com")

# --- WEATHER ---
def get_weather(city):
    try:
        city = city.replace("weather", "").replace("in ", "").replace("tell me", "").replace("the", "").strip()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_apikey}&units=metric"
        res = requests.get(url).json()
        if res["cod"] != 404:
            temp = res["main"]["temp"]
            desc = res["weather"][0]["description"]
            speak(f"It is {temp} degrees celsius in {city} with {desc}.")
        else:
            speak("I couldn't find that city.")
    except:
        speak("I am having trouble connecting to the weather service.")

# --- MAIN LOOP ---
if __name__ == '__main__':
    speak("Jarvis online. Click this window and press SPACEBAR to stop me.")

    while True:
        query = listen()
        if query == "none": continue

        # 1. Voice Stop
        if "stop" in query and "listening" not in query:
             speak("Pausing...")
             continue

        # 2. System Controls
        elif any(x in query for x in ["volume", "mute", "screenshot", "lock system"]):
            system_control(query)

        # 3. Open Apps
        elif any(x in query for x in ["notepad", "calculator", "task manager", "settings", "camera", "whatsapp"]):
            open_system_app(query)
 
        # 4. Web Sites
        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")
        elif "open github" in query:
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
        elif "open linkedin" in query:
            speak("Opening LinkedIn")
            webbrowser.open("https://linkedin.com")
        elif "open instagram" in query:
            speak("Opening Instagram")
            webbrowser.open("https://instagram.com")
        elif "open facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("https://facebook.com")
        elif "open stackoverflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")

        # 5. Weather
        elif "weather" in query:
            if " in " in query: get_weather(query)
            else:
                speak("Which city?")
                city = listen()
                if city != "none": get_weather(city)

        # 6. Shutdown
        elif "shutdown" in query:
            speak("Shutting down, sir.")
            break

        # 7. AI Brain
        else:
            response = get_response(query)
            speak(response)
