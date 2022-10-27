import webbrowser
import time

speech = input("Input command: ")
speech = speech.lower()
if "open instagram" in speech:
    print("Opening instagram, sir")
    time.sleep(0.5)
    webbrowser.open("instagram.com")
