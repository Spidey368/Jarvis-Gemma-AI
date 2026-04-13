# J.A.R.V.I.S. v5.0 (Stark Edition)
A sophisticated, voice-activated AI assistant running locally on Ubuntu. This project integrates Local LLMs with system-level diagnostics to create a professional-grade personal assistant.

## Key Features
- **Intelligent Reasoning:** Powered by **Gemma 3 (1B)** via Ollama, customized with a professional "Stark" persona.
- **System Awareness:** Real-time monitoring of CPU, RAM, and Battery status using `psutil`.
- **Direct Voice Navigation:** Command-based web launching (e.g., "Open my YouTube channel") and terminal initialization.
- **Advanced VAD:** Tuned Voice Activity Detection to allow for natural pauses and complex mathematical queries.
- **Hardware Hack:** Utilizes an Android device via DroidCam as a wireless microphone bridge to bypass Linux driver limitations.

## Tech Stack
- **OS:** Ubuntu Linux
- **Model:** Google Gemma 3 (1B)
- **Language:** Python 3.10+
- **Key Libraries:** `ollama`, `speech_recognition`, `pyttsx3`, `psutil`

##  Installation & Setup
1. **Initialize the Brain:**
   ```bash
   ollama run gemma3:1b
