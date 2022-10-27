import webbrowser
import time

speech = input("Input command: ")
speech = speech.lower()
if "open youtube" in speech:
    print("Opening youtube, sir")
    time.sleep(0.5)
    webbrowser.open("youtube.com")
