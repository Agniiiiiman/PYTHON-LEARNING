import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import time
import os
import subprocess
import platform
import pyjokes


engine = pyttsx3.init()
engine.setProperty("rate", 180)

recognizer = sr.Recognizer()
recognizer.energy_threshold = 400
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.6
recognizer.non_speaking_duration = 0.3

APP_PATHS = {
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "paint": "mspaint.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}


def system_control(action):
    """Shutdown, restart, or log out of the system."""
    speak(f"Executing system {action} command...")

    if platform.system() == "Windows":
        if action == "shutdown":
            
            os.system("shutdown /s /t 0")
        elif action == "restart":
            os.system("shutdown /r /t 0")
        elif action == "logout":
            os.system("shutdown /l")
    else:
        speak("System commands are only supported on Windows right now.")


def speak(text):
    """Speak text (blocking)."""
    print(f"Jarvis: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
       
        print("TTS error:", e)


def open_app(app_key):
    """Open an application defined in APP_PATHS."""
    app_cmd = APP_PATHS.get(app_key)
    if not app_cmd:
        speak("I don't know where that application is installed.")
        return

    try:
        if os.path.isfile(app_cmd) or "\\" in app_cmd or ":" in app_cmd:
            os.startfile(app_cmd)
        else:
            subprocess.Popen(app_cmd)
    except Exception as e:
        print(f"Error opening {app_key}: {e}")
        speak(f"Sorry, I could not open {app_key}.")


def get_audio(source):
    """Listen once from the provided audio source and return recognized text."""
    print("\nListening...")
    try:
        audio = recognizer.listen(source, timeout=4, phrase_time_limit=6)
    except sr.WaitTimeoutError:
        print("Timeout: No speech detected.")
        return None

    print("Recognizing...")
    try:
        command = recognizer.recognize_google(audio, language="en-IN").lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Didn't understand.")
    except sr.RequestError as e:
        print("Internet/Service connection error:", e)

    return None


def process_command(command):
    """Interpret and execute a single recognized command string."""
    if not command:
        return

    # -------- EXIT JARVIS ONLY --------
    if any(x in command for x in ["stop a", "exit a", "quit a"]):
        speak("Jarvis shutting down. Goodbye.")
        return "shutdown"

    # -------- SYSTEM POWER COMMANDS --------
    if any(x in command for x in ["shutdown pc", "shut down pc", "turn off pc", "shutdown my computer", "shutdown computer"]):
        system_control("shutdown")
        return

    if any(x in command for x in ["restart pc", "restart computer", "reboot system", "reboot computer"]):
        system_control("restart")
        return

    if any(x in command for x in ["logout", "log out", "sign out"]):
        system_control("logout")
        return

    # -------- BASIC --------
    if "hello jarvis" in command or "hey jarvis" in command:
        speak("Hello, how can I help you?")

    elif "what is the time" in command or "tell me the time" in command:
        speak(datetime.datetime.now().strftime("The time is %I:%M %p"))

    # -------- WEB --------
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open netflix" in command:
        speak("Opening Netflix.")
        webbrowser.open("https://www.netflix.com/browse")

    elif "open whatsapp" in command:
        speak("Opening WhatsApp Web.")
        webbrowser.open("https://web.whatsapp.com")

    elif "tell me a joke" in command or "tell a joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    

    elif "search for" in command:
        query = command.split("search for", 1)[1].strip() if "search for" in command else ""
        if query:
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("Tell me what to search for.")

   
    elif "open word" in command:
        speak("Opening Microsoft Word.")
        open_app("word")

    elif "open paint" in command:
        speak("Opening Paint.")
        open_app("paint")

    elif "open notepad" in command:
        speak("Opening Notepad.")
        open_app("notepad")

    elif "open calculator" in command or "open calc" in command:
        speak("Opening Calculator.")
        open_app("calculator")

    else:
        speak("I don't know that command yet.")



if __name__ == "__main__":
    speak("Master, I am online and ready.")
    print("Speak now. Say 'stop ai' to exit only the assistant.")

    try:
        with sr.Microphone() as mic:
            print("\nCalibration (1 sec)...")
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            print("Calibration complete.")
            speak("Calibration completed.")

            while True:
                command = get_audio(mic)
                result = process_command(command)
                if result == "shutdown":
                    break
                time.sleep(0.15)

    except KeyboardInterrupt:
   
        print("\nInterrupted by user. Stopping TTS and exiting.")
        try:
            engine.stop()
        except Exception:
            pass
