import speech_recognition as sr
import pyaudio
import numpy as np
import subprocess
import time
import pyttsx3  # New library for talking

# --- VOICE CONFIGURATION ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# On Linux, usually index 0 is a male voice and 11 is a female voice. 
# You can experiment with indices to find a voice you like.
engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 170) # Speed of speech (150-200 is natural)

def speak(text):
    """Makes Jarvis talk"""
    print(f"[JARVIS]: {text}")
    engine.say(text)
    engine.runAndWait()

# --- CLAP CONFIGURATION ---
CLAP_THRESHOLD = 12000  # Updated based on your previous test
CLAP_WINDOW = 4

def detect_claps(duration):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100,
                    input=True, frames_per_buffer=1024)
    
    # We don't want Jarvis talking while we clap, so we wait a split second
    time.sleep(0.5) 
    
    print(f"\nListening for claps for {duration}s...")
    count = 0
    start_time = time.time()
    
    while time.time() - start_time < duration:
        try:
            data = np.frombuffer(stream.read(1024, exception_on_overflow=False), dtype=np.int16)
            peak = np.max(np.abs(data))
            
            if peak > CLAP_THRESHOLD:
                count += 1
                print(f"   * CLAP {count} (Vol: {peak})")
                time.sleep(0.6) # Increased debounce for accuracy
        except:
            continue
            
    stream.stop_stream()
    stream.close()
    p.terminate()
    return count

def run_jarvis():
    r = sr.Recognizer()
    mic = sr.Microphone()

    print("\n==============================")
    print("      JARVIS IS ONLINE")
    print("==============================\n")

    with mic as source:
        print(">>> Calibrating...")
        r.adjust_for_ambient_noise(source, duration=1)
        
        while True:
            print("\nListening...")
            try:
                audio = r.listen(source, timeout=None, phrase_time_limit=3)
                text = r.recognize_google(audio).lower()
                
                if "jarvis" in text:
                    # 1. Jarvis Responds
                    speak("Yes boss")
                    
                    # 2. Jarvis listens for claps
                    claps = detect_claps(CLAP_WINDOW)
                    
                    # 3. Execution
                    if claps == 1:
                        speak("Opening Firefox")
                        subprocess.Popen(["firefox"])
                    elif claps == 2:
                        speak("Opening VS Code")
                        subprocess.Popen(["code"])
                    elif claps == 3:
                        speak("Opening Terminal")
                        subprocess.Popen(["gnome-terminal"])
                    elif claps > 0:
                        speak(f"I heard {claps} claps, but I have no orders for that.")
                        
            except sr.UnknownValueError:
                pass 
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    run_jarvis()
