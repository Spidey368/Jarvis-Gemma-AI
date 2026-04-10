import speech_recognition as sr
import pyttsx3
import ollama
import subprocess
import webbrowser
import psutil # For system diagnostics
import time
import os

# --- CONFIGURATION ---
MODEL_NAME = 'gemma3:1b'
# REPLACE with your actual YouTube channel URL
MY_YOUTUBE_CHANNEL = "https://www.youtube.com/@YourChannelName"

# --- J.A.R.V.I.S. HUD (ASCII) ---
JARVIS_LOGO = r"""
   ██ █████  ██████  ██    ██ ██ ███████ 
   ██ ██   ██ ██   ██ ██    ██ ██ ██      
   ██ ███████ ██████  ██    ██ ██ ███████ 
██ ██ ██   ██ ██   ██  ██  ██  ██      ██ 
 ██  ██   ██ ██   ██   ████   ██ ███████ 
      [ SYSTEM VERSION: 5.0 LOCAL ]
"""

engine = pyttsx3.init()
engine.setProperty('rate', 190)

def speak(text):
    print(f"\n[JARVIS]: {text}")
    engine.say(text)
    engine.runAndWait()

def get_system_status():
    """Iron Man style system diagnostic"""
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    status = f"CPU is at {cpu} percent. Memory usage is at {ram} percent."
    if battery:
        status += f" Power is at {battery.percent} percent."
    return status

def get_ai_response(user_input):
    print(">>> JARVIS is calculating...")
    try:
        system_prompt = (
            "You are J.A.R.V.I.S., Tony Stark's sophisticated AI. "
            "You are helpful, witty, and respond with 'Sir'. "
            "You are running on an Acer laptop with Ubuntu and specialize in Computer Engineering."
        )
        response = ollama.chat(model=MODEL_NAME, messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input}
        ])
        return response['message']['content']
    except Exception as e:
        return "I'm afraid there's a glitch in my neural network, Sir."

def run_jarvis():
    r = sr.Recognizer()
    r.pause_threshold = 1.5 
    
    os.system('clear')
    print(JARVIS_LOGO)
    
    # --- STARTUP DIAGNOSTIC ---
    status = get_system_status()
    speak(f"Systems online. {status} I am standing by, Sir.")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        while True:
            print("\nListening for commands...")
            try:
                audio = r.listen(source, timeout=None, phrase_time_limit=10)
                text = r.recognize_google(audio).lower()
                print(f"Transcript: {text}")

                if "jarvis" in text:
                    # 1. SMART APP/WEB LOGIC
                    if "firefox" in text:
                        if "my youtube" in text or "my channel" in text:
                            speak("Opening your YouTube channel immediately, Sir.")
                            webbrowser.open(MY_YOUTUBE_CHANNEL)
                        else:
                            speak("Initializing Firefox.")
                            subprocess.Popen(["firefox"])
                    
                    elif "terminal" in text or "console" in text:
                        speak("Opening a secure terminal for you.")
                        subprocess.Popen(["gnome-terminal"])

                    # 2. SYSTEM STATUS COMMAND
                    elif "status" in text or "diagnostics" in text:
                        speak(f"Scanning systems. {get_system_status()}")

                    # 3. INTELLIGENT CHAT/MATH
                    else:
                        prompt = text.replace("jarvis", "").strip()
                        if prompt:
                            answer = get_ai_response(prompt)
                            speak(answer)
                
            except Exception: pass

if __name__ == "__main__":
    run_jarvis()
