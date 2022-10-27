import webbrowser
import time

speech = input("Input your command:")
if "open a website" in speech:
    speech = input("Please say the name of the website you want to open: ")
    print(f"Opening {speech}, sir.")
    time.sleep(0.5)
    webbrowser.open(speech)
