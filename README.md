# Jarvis: Local AI Voice Assistant
A voice-activated assistant built with Python that runs entirely locally on Ubuntu.

## Features
- **Voice Recognition:** Uses Google Speech Recognition API.
- **Local LLM:** Powered by **Gemma 3 (1B)** via Ollama for privacy and speed.
- **Custom Hardware Solution:** Bypassed internal Intel 54c8 audio driver issues by using an Android phone as a wireless mic via DroidCam.
- **App Control:** Triggered by the wake-word "Jarvis" followed by specific clap patterns.

## Tech Stack
- **OS:** Ubuntu Linux
- **Model:** Gemma 3 (1B)
- **Language:** Python 3.10+
- **Audio Routing:** ALSA & PipeWire with DroidCam loopback.

## How to Run
1. Start Ollama: `ollama run gemma3:1b`
2. Connect mobile device via DroidCam (ensure Audio is checked).
3. Run `python3 jarvis.py`.
