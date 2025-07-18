# Jarvis: Voice Assistant with Speech, Web, and AI Integration

This project implements a **simple desktop voice assistant** named Jarvis. It uses speech recognition, text-to-speech, web automation, and OpenAI's GPT language model for answering queries. Inspired by everyday digital assistant tasks, Jarvis can open websites, launch apps, play music, fetch information from Wikipedia, interact with the file system, and answer questions conversationally using AI.

---

## 📌 Features

- **Voice Command Processing:**  
  Listens to voice queries and converts them into actionable commands.

- **Web Automation:**  
  Opens popular websites like YouTube, Wikipedia, Gmail, Amazon, and Flipkart using voice commands.

- **Desktop Application Control:**  
  Launches common desktop applications such as Notepad, Calculator, Clock, browsers, WhatsApp, Telegram, and Microsoft Office Suite.

- **File System Navigation:**  
  Voice-controlled opening of drives (C, D, etc.).

- **Music Playback:**  
  Plays a preset music file with a specific command.

- **Current Time Reporting:**  
  Reads out the system time on demand.

- **Wikipedia Summaries:**  
  Fetches and speaks Wikipedia search results.

- **Conversational AI (OpenAI):**  
  Responds to custom queries using OpenAI's GPT-3.5-turbo language model.

- **Graceful Shutdown:**  
  Can be stopped via a voice command.

---

## 📂 Code Structure

- **jarvis.py**  
  The main script handling speech input, voice responses, web/app launching, system integration, and main event loop.

- **openaiclient.py**  
  Small client for making queries to OpenAI's API using the API key stored in `config.py`.

- **config.py**  
  Stores the OpenAI API key (`apikey`).

---

## 🛠️ Requirements

- Python 3.x
- `speech_recognition`
- `wikipedia`
- `openai`
- `pyaudio`
- `win32com.client` (Windows only)
- `webbrowser`
- `subprocess`
- `playsound`
- `AppOpener`
- Internet connection (for Wikipedia and OpenAI API)
- Windows OS (for voice synth and certain system app launches)

---

## 🚀 Quick Start

1. **Install Requirements:**

