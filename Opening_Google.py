import webbrowser
import time

speech = input("Input command: ")
speech = speech.lower()
if "open google" in speech:
    print("Opening google, sir")
    time.sleep(0.5)
    webbrowser.open("google.com")
