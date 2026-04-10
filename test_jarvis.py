import speech_recognition as sr
import pyttsx3
import ollama
import numpy as np
import pyaudio
import sys

def check_system():
    print("--- JARVIS SYSTEM HEALTH CHECK ---\n")
    
    # 1. Check Python Libraries
    print("[1/3] Checking Libraries...")
    try:
        print(f"  - SpeechRecognition: {sr.__version__}")
        print(f"  - Numpy: {np.__version__}")
        print("  - PyAudio: Found")
        print("  - pyttsx3: Found")
        print("  - ollama: Found")
    except Exception as e:
        print(f"  [!] ERROR: Missing library: {e}")
        return

    # 2. Check Gemma 3 Connection
    print("\n[2/3] Checking Gemma 3 Brain...")
    try:
        # We send a tiny prompt to see if the CPU can handle it
        response = ollama.generate(model='gemma3:1b', prompt='hi')
        print("  - Gemma 3 is responding! (Status: Online)")
    except Exception as e:
        print(f"  [!] ERROR: Could not talk to Ollama. Is it running? {e}")

    # 3. Check Audio Hardware
    print("\n[3/3] Checking Audio Devices...")
    p = pyaudio.PyAudio()
    device_count = p.get_device_count()
    print(f"  - Found {device_count} audio devices.")
    
    # Look for DroidCam or Pulse/Pipewire
    found_mic = False
    for i in range(device_count):
        dev = p.get_device_info_by_index(i)
        if dev['maxInputChannels'] > 0:
            print(f"  - Mic Found: {dev['name']}")
            found_mic = True
            
    if not found_mic:
        print("  [!] WARNING: No input devices (microphones) detected!")
    
    p.terminate()
    print("\n--- HEALTH CHECK COMPLETE ---")

if __name__ == "__main__":
    check_system()
