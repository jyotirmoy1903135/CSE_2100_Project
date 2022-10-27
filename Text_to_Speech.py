import pyttsx3
def speak(string):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1)
    engine.say(string)
    engine.runAndWait()

S = input("Write what to want to hear: ")
speak(S)
