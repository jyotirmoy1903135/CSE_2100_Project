import webbrowser
import time

speech = input("Input command: ")
speech = speech.lower()
if "open facebook" in speech:
    print("Opening facebook, sir")
    time.sleep(0.5)
    webbrowser.open("facebook.com")
