import webbrowser
import time

speech = input("Input command: ")
speech = speech.lower()
if "open twitter" in speech:
    print("Opening twitter, sir")
    time.sleep(0.5)
    webbrowser.open("twitter.com")
