import re
import wikipedia
import speech_recognition as sr
import time

# global speech
# def SpeechToText():
#     global speech
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Speak anything:")
#         time.sleep(0.1)
#         print("Recognizing....")
#         audio = r.listen(source)
#
#     try:
#         text = r.recognize_google(audio)
#         speech = format(text.lower())
#         print("You said:", speech)
#     except:
#         print("Sorry, couldn't recognize your voice!")
#         #SpeechToText()
#
#
# SpeechToText()
speech = input("Enter your keyword: ")
print(wikipedia.summary(speech, sentences = 2))
