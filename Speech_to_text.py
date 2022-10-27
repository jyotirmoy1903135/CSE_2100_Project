import speech_recognition as sr
import time

def SpeechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything:")
        time.sleep(0.1)
        print("Recognizing....")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        speech = format(text.lower())
        print("You said:", speech)
    except:
        print("Sorry, couldn't recognize your voice!")
        SpeechToText()

SpeechToText()
