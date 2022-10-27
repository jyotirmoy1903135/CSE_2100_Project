import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import time
import re
import os
import datetime
import webbrowser
import wikipedia
import pyttsx3
import speech_recognition as sr

#Importing .py versions of .qrc files:
from Used_Images import First_Image
from Used_Images import Second_Image
from Used_Images import Third_Image
from Used_Images import Fourth_Image

#Audio
from pygame import mixer
mixer.init()
mixer.music.load("Button_click_ogg.ogg")

GenderBoolean = False
GenderEntry = "None"

Wish_according_to_time = ""
speech = ""


def wishMe():
    hour = int(datetime.datetime.now().hour)
    global Wish_according_to_time
    if hour>=0 and hour<4:
        Wish_according_to_time = "Welcome, sir! I am David, your PC assistant. Not to sleep yet? Anyway, how may I help you?"

    elif hour>=4 and hour<12:
        Wish_according_to_time = "Good morning, sir! I am David, your PC assistant. How may I help you?"

    elif hour>=12 and hour<4:
        Wish_according_to_time = "Welcome, sir! How's your day going? I am David, your PC assistant. How may I help you?"

    elif hour>=4 and hour<6:
        Wish_according_to_time = "Good afternoon, sir! I am David, your PC assistant. How may I help you?"

    elif hour>=6 and hour<8:
        Wish_according_to_time = "Good evening, sir! I am David, your PC assistant. How may I help you?"

    else:
        Wish_according_to_time = "Welcome, sir! How did the day go? I am David, your PC assistant. How may I help you?"


def speak(string):
    engine = pyttsx3.init()
    engine.setProperty('rate', 300)
    engine.setProperty('volume', 1)
    engine.say(string)
    engine.runAndWait()



def SpeechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything:")
        time.sleep(0.1)
        print("Recognizing....")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        global speech
        speech = format(text.lower())
    except:
        print("Sorry, couldn't recognize your voice!")
        SpeechToText()


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen1.ui", self)
        self.START.clicked.connect(self.gotoSecondLayer)
        self.EXIT.clicked.connect(self.gotoExit)
        #self.create.clicked.connect(self.gotocreate)

    def gotoSecondLayer(self):
        mixer.music.play()
        time.sleep(0.8)
        a = SecondLayer()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoExit(self):
        mixer.music.play()
        time.sleep(0.8)
        exit()

class SecondLayer(QDialog):
    def __init__(self):
        super(SecondLayer, self).__init__()
        loadUi("authentication1.ui", self)
        self.LogIn.clicked.connect(self.gotoLogIn)
        self.CreateAccount.clicked.connect(self.gotoCreateAccount)
        self.Back.clicked.connect(self.gotoBack)


    def gotoLogIn(self):
        mixer.music.play()
        time.sleep(0.8)
        a = LogIn()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCreateAccount(self):
        mixer.music.play()
        time.sleep(0.8)
        a = CreateAccount()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoBack(self):
        mixer.music.play()
        #time.sleep(0.8)
        a = WelcomeScreen()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi("CreateAccount.ui", self)

        lis = list()
        for i in range(1901, 2021): lis.append(str(i))
        self.Back.clicked.connect(self.gotoBack)
        self.Submit.clicked.connect(self.gotoSubmit)

        self.BirthYear.addItems(lis)
        self.BirthYear.activated.connect(self.gotoBirthYearSeleced)
        self.BirthDate.activated.connect(self.gotoBirthDateSeleced)

        self.Male.toggled.connect(lambda: self.gotoGenderSelected(self.Male))
        self.Female.toggled.connect(lambda: self.gotoGenderSelected(self.Female))
        self.ThirdGender.toggled.connect(lambda: self.gotoGenderSelected(self.ThirdGender))

    def gotoBack(self):
        a = SecondLayer()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoBirthYearSeleced(self):
        if int(self.BirthYear.currentText())%4 == 0 and int(self.BirthYear.currentText())%100 != 0:
            self.BirthMonth.clear()
            lis = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
            for i in range(10, 32): lis.append(str(i))
            self.BirthMonth.addItem("01", lis)
            lis.pop()
            lis.pop()
            self.BirthMonth.addItem("02", lis)
            lis.append("30")
            lis.append("31")
            self.BirthMonth.addItem("03", lis)
            lis.pop()
            self.BirthMonth.addItem("04", lis)
            lis.append("31")
            self.BirthMonth.addItem("05", lis)
            lis.pop()
            self.BirthMonth.addItem("06", lis)
            lis.append("31")
            self.BirthMonth.addItem("07", lis)
            self.BirthMonth.addItem("08", lis)
            lis.pop()
            self.BirthMonth.addItem("09", lis)
            lis.append("31")
            self.BirthMonth.addItem("10", lis)
            lis.pop()
            self.BirthMonth.addItem("11", lis)
            lis.append("31")
            self.BirthMonth.addItem("12", lis)
            self.BirthMonth.activated.connect(self.gotoBirthMonthSeleced)
        else:
            self.BirthMonth.clear()
            lis = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
            for i in range(10, 32): lis.append(str(i))
            self.BirthMonth.addItem("01", lis)
            lis.pop()
            lis.pop()
            lis.pop()
            self.BirthMonth.addItem("02", lis)
            lis.append("30")
            lis.append("31")
            self.BirthMonth.addItem("03", lis)
            lis.pop()
            self.BirthMonth.addItem("04", lis)
            lis.append("31")
            self.BirthMonth.addItem("05", lis)
            lis.pop()
            self.BirthMonth.addItem("06", lis)
            lis.append("31")
            self.BirthMonth.addItem("07", lis)
            self.BirthMonth.addItem("08", lis)
            lis.pop()
            self.BirthMonth.addItem("09", lis)
            lis.append("31")
            self.BirthMonth.addItem("10", lis)
            lis.pop()
            self.BirthMonth.addItem("11", lis)
            lis.append("31")
            self.BirthMonth.addItem("12", lis)
            self.BirthMonth.activated.connect(self.gotoBirthMonthSeleced)

    def gotoBirthMonthSeleced(self, index):
        self.BirthDate.clear()
        self.BirthDate.addItems(self.BirthMonth.itemData(index))

    def gotoBirthDateSeleced(self):
        pass

    def gotoGenderSelected(self, para):
        global GenderBoolean
        GenderBoolean = para.isChecked()
        global GenderEntry
        GenderEntry = para.text()

    def gotoSubmit(self):
        a = self.Username.text()
        b = self.Password.text()
        c = self.ConfirmPassword.text()
        d = self.PasswordHint.text()
        e = self.BirthYear.currentText()
        f = self.BirthMonth.currentText()
        g = self.BirthDate.currentText()

        A = open("Database.txt", "r")
        previous_entry = False
        for line in A:
            line = line[1:len(line) - 2]
            user_info = line.split("][")
            if user_info[0] == a:
                previous_entry = True
                break
        A.close()

        if previous_entry == True:
            self.errorLabelUsername.setText("* Username already exists !")
        elif len(a)==0 or len(a)>20 or '[' in a or ']' in a or len(b)==0 or len(b)<6 or len(b)>30 or '[' in b or ']' in b \
        or b!=c or len(d)==0 or len(d)>30 or '[' in d or ']' in d or len(g)==0 or GenderBoolean==False:
            if len(a) == 0:
                self.errorLabelUsername.setText("* Username cannot be empty !")
            elif len(a) > 20:
                self.errorLabelUsername.setText("* Username cannot have more than 20 characters !")
            elif '[' in a or ']' in a:
                self.errorLabelUsername.setText("* Username cannot contain '[' or ']' !")
            else:
                self.errorLabelUsername.setText("")
            if len(b) == 0:
                self.errorLabelPassword.setText("* Password cannot be empty !")
            elif len(b) < 6:
                self.errorLabelPassword.setText("* Password must contain at least 6 characters !")
            elif len(b) > 30:
                self.errorLabelPassword.setText("* Password cannot have more than 30 characters !")
            elif '[' in b or ']' in b:
                self.errorLabelPassword.setText("* Password cannot contain '[' or ']' !")
            else:
                self.errorLabelPassword.setText("")
            if b != c:
                self.errorLabelConfirmPassword.setText("* Passwords do not match !")
            else:
                self.errorLabelConfirmPassword.setText("")
            if len(d) == 0:
                self.errorLabelPasswordHint.setText("* Password cannot be empty !")
            elif len(d) > 30:
                self.errorLabelPasswordHint.setText("* Password Hint cannot have more than 30 characters !")
            elif '[' in d or ']' in d:
                self.errorLabelPasswordHint.setText("* Password Hint cannot contain '[' or ']' !")
            else:
                self.errorLabelPasswordHint.setText("")
            if len(g) == 0:
                self.errorLabelDateOfBirth.setText("* You must select your Date of Birth !")
            else:
                self.errorLabelDateOfBirth.setText("")
            if GenderBoolean == False:
                self.errorLabelGender.setText("* You must select your Gender !")
            else:
                self.errorLabelGender.setText("")
        else:
            self.successLabel.setText("Account created succeessfully!")
            mixer.music.play()
            #time.sleep(0.8)
            A = open("Database.txt", "a")
            global GenderEntry
            A.write(f"[{a}][{b}][{d}][{g}/{f}/{e}][{GenderEntry}]\n")
            A.close()
            time.sleep(1.0)
            a = SecondLayer()
            widget.addWidget(a)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class LogIn(QDialog):
    def __init__(self):
        super(LogIn, self).__init__()
        loadUi("LogIn.ui", self)
        self.Back.clicked.connect(self.gotoBack)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ForgotPassword.clicked.connect(self.gotoForgotPassword)
        self.Enter.clicked.connect(self.gotoEnter)

    def gotoBack(self):
        a = SecondLayer()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoForgotPassword(self):
        a = self.Username.text()
        A = open("Database.txt", "r")
        previous_entry = False
        for line in A:
            line = line[1:len(line) - 2]
            user_info = line.split("][")
            if user_info[0] == a:
                self.errorLabelUsername.setText("")
                self.LabelPasswordHint.setText(f"Password Hint: {user_info[2]}")
                previous_entry = True
                break
        if previous_entry == False:
            self.successLabel.setText("")
            self.errorLabelUsername.setText("* Username not found in database !")
        A.close()

    def gotoEnter(self):
        a = self.Username.text()
        b = self.Password.text()
        A = open("Database.txt", "r")
        previous_entry = False
        for line in A:
            line = line[1:len(line) - 2]
            user_info = line.split("][")
            #print(user_info)
            if user_info[0] == a:
                previous_entry = True
                self.errorLabelUsername.setText("")
                if user_info[1] == b:
                    self.LabelPasswordHint.setText("")
                    self.errorLabelPassword.setText("")
                    mixer.music.play()
                    time.sleep(0.8)
                    self.successLabel.setText("Log in successful !")
                    a = SelectTask()
                    widget.addWidget(a)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                    break
                else:
                    self.successLabel.setText("")
                    self.errorLabelPassword.setText("* Wrong  password !")
        if previous_entry == False:
            self.successLabel.setText("")
            self.errorLabelUsername.setText("* Username not found in database !")
        A.close()




class SelectTask(QDialog):
    def __init__(self):
        super(SelectTask, self).__init__()
        loadUi("SelectTask.ui", self)

        self.InitializeScreen.clicked.connect(self.gotoInitializeScreen)
        self.Back.clicked.connect(self.gotoBack)

    def gotoInitializeScreen(self):
        global Wish_according_to_time
        wishMe()
        self.LabelFirstSpeech.setText(Wish_according_to_time)
        speak(self.LabelFirstSpeech.text())
        self.gotoInitializeScreen = self.sender()
        self.gotoInitializeScreen.deleteLater()
        self.labelGetStarted.setText("")
        #time.sleep(1)

        SpeechToText()
        global speech
        print(speech)
        #speech = "what's the time"
        if "search in wikipedia" in speech:
            speak("Mention what you want to search in wikipedia")
            SpeechToText()
            speak(f"According to wikipedia, {wikipedia.summary(speech, sentences=2)}")
            print(f"According to wikipedia, {wikipedia.summary(speech, sentences=2)}")
        elif "open youtube" in speech:
            speak("Opening youtube, sir")
            time.sleep(0.5)
            webbrowser.open("youtube.com")
        elif "open google" in speech:
            speak("Opening google, sir")
            time.sleep(0.5)
            webbrowser.open("google.com")
        elif "open facebook" in speech:
            speak("Opening facebook, sir")
            time.sleep(0.5)
            webbrowser.open("facebook.com")
        elif "open instagram" in speech:
            speak("Opening facebook, sir")
            time.sleep(0.5)
            webbrowser.open("instagram.com")
        elif "open twitter" in speech:
            speak("Opening twitter, sir")
            time.sleep(0.5)
            webbrowser.open("twitter.com")
        elif "open a website" in speech:
            speak("Please say the name of the website you want to open")
            SpeechToText()
            speak(f"Opening {speech}, sir")
            time.sleep(0.5)
            webbrowser.open(speech)
        elif "what's the time" in speech:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the current time according to your area is {strTime}")

        elif "open codeblocks" in speech or "open code blocks" in speech:
            speak("Opening codeblocks, sir")
            time.sleep(0.5)
            os.startfile(
                r"C:\Users\ASUS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\CodeBlocks\CodeBlocks.lnk")
        elif "open microsoft word" in speech or "open ms word" in speech:
            speak("Opening microsoft word, sir")
            time.sleep(0.5)
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
        elif "open microsoft powerpoint" in speech or "open ms powerpoint" in speech:
            speak("Opening microsoft powerpoint, sir")
            time.sleep(0.5)
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
        elif "open microsoft excel" in speech or "open ms excel" in speech:
            speak("Opening microsoft excel, sir")
            time.sleep(0.5)
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
        elif "open chrome" in speech or "open ggogle chrome" in speech:
            speak("Opening google chrome, sir")
            time.sleep(0.5)
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
        elif "base conversion" in speech:
            # Base conversion among Decimal, Binary, Octal and Hexadecimal number systems.
            speak("Say 1 to convert from decimal to binary.")
            speak("Say 2 to convert from decimal to octal.")
            speak("Say 3 to convert from decimal to hexadecimal.")
            speak("Say 4 to convert from binary to decimal.")
            speak("Say 5 to convert from binary to octal.")
            speak("Say 6 to convert from binary to hexadecimal.")
            speak("Say 7 to convert from octal to decimal.")
            speak("Say 8 to convert from octal to binary.")
            speak("Say 9 to convert from octal to hexadecimal.")
            speak("Say 10 to convert from hexadecimal to decimal.")
            speak("Say 11 to convert from hexadecimal to binary.")
            speak("Say 12 to convert from hexadecimal to octal.")
            speak("Say 0 to exit.\n\n")

            while True:
                speak("Enter your input: ")

                SpeechToText()
                if speech == "1":
                    speak("Say your decimal number: ")
                    SpeechToText()
                    n = int(speech)
                    n1 = n
                    ans = ""
                    while n1 != 0:
                        p = n1 % 2
                        ans = ans + str(p)
                        n1 = n1 // 2

                    ans = ans[::-1]
                    ans = int(ans)
                    speak(f"The binary form of {n} is: {ans}")


                elif speech == "2":
                    speak("Say your decimal number: ")
                    SpeechToText()
                    n = int(speech)
                    n1 = n
                    ans = ""
                    while n1 != 0:
                        p = n1 % 8
                        ans = ans + str(p)
                        n1 = n1 // 8

                    ans = ans[::-1]
                    speak(f"The octal form of {n} is: {ans}")


                elif speech == "3":
                    speak("Say your decimal number: ")
                    SpeechToText()
                    n = int(speech)
                    n1 = n
                    ans = ""
                    while n1 != 0:
                        p = n1 % 16

                        if p <= 9:
                            ans = ans + str(p)
                        else:
                            diction = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
                            for key, value in diction.items():
                                if p == key: ans = ans + value

                        n1 = n1 // 16

                    ans = ans[::-1]
                    speak(f"The hexadecimal form of {n} is: {ans}")


                elif speech == "4":
                    speak("Say your decimal number: ")
                    SpeechToText()
                    n = int(speech)
                    n1 = n
                    ans = 0
                    power = 0
                    while n1 != 0:
                        p = n1 % 10
                        ans = ans + p * (2 ** power)
                        n1 = n1 // 10
                        power = power + 1

                    speak(f"The decimal form of {n} is: {ans}")


                elif speech == "5":
                    speak("Say your decimal number: ")
                    SpeechToText()
                    n = int(speech)
                    n1 = n
                    while len(n1) % 3 != 0: n1 = '0' + n1
                    ans = ""
                    position = len(n1) - 1
                    for i in range(len(n1) // 3):
                        temp = ""
                        for i in range(3):
                            temp = temp + n1[position]
                            position = position - 1
                        temp = temp[::-1]

                        diction = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6',
                                   '111': '7'}
                        for key, value in diction.items():
                            if temp == key: ans = ans + value

                    ans = ans[::-1]
                    speak(f"The octal form of {n} is: {ans}")


                elif speech == "6":
                    speak("Say your binary number: ")
                    SpeechToText()
                    n = int(speech)
                    n1 = n
                    while len(n1) % 4 != 0: n1 = '0' + n1
                    ans = ""
                    position = len(n1) - 1
                    for i in range(len(n1) // 4):
                        temp = ""
                        for i in range(4):
                            temp = temp + n1[position]
                            position = position - 1
                        temp = temp[::-1]

                        diction = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                                   '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A',
                                   '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F', }
                        for key, value in diction.items():
                            if temp == key: ans = ans + value

                    ans = ans[::-1]
                    speak(f"The hexadecimal form of {n} is: {ans}")


                elif speech == "7":
                    speak("Say your octal number: ")
                    SpeechToText()
                    n = int(speech)
                    n1 = n
                    ans = 0
                    power = 0
                    while n1 != 0:
                        p = n1 % 10
                        ans = ans + p * (8 ** power)
                        n1 = n1 // 10
                        power = power + 1

                    speak(f"The decimal form of {n} is: {ans}")


                elif speech == "8":
                    speak("Say your octal number: ")
                    SpeechToText()
                    n = speech
                    n1 = n[::-1]
                    ans = ""
                    position = len(n1) - 1

                    for i in range(len(n1)):
                        diction = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110',
                                   '7': '111'}
                        for key, value in diction.items():
                            if n1[position] == key: ans = ans + value

                        position = position - 1

                    speak(f"The binary form of {n} is: {ans}")


                elif speech == "9":
                    speak("Say your octal number: ")
                    SpeechToText()
                    n = speech
                    n1 = n[::-1]
                    bin = ""
                    position = len(n1) - 1

                    for i in range(len(n1)):
                        diction = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110',
                                   '7': '111'}
                        for key, value in diction.items():
                            if n1[position] == key: bin = bin + value

                        position = position - 1

                    bin1 = bin
                    while len(bin1) % 4 != 0: bin1 = '0' + bin1
                    ans = ""
                    position = len(bin1) - 1
                    for i in range(len(bin1) // 4):
                        temp = ""
                        for i in range(4):
                            temp = temp + bin1[position]
                            position = position - 1
                        temp = temp[::-1]

                        diction = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                                   '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A',
                                   '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F', }
                        for key, value in diction.items():
                            if temp == key: ans = ans + value

                    ans = ans[::-1]
                    speak(f"The hexadecimal form of {n} is: {ans}")


                elif speech == "10":
                    print("Say your hexadecimal number: ")
                    SpeechToText()
                    n = speech
                    position = len(n) - 1
                    ans = 0
                    power = 0
                    while position >= 0:
                        flag = 0

                        diction = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
                        for key, value in diction.items():
                            if n[position] == key:
                                ans = ans + value * (16 ** power)
                                flag = 1
                        if flag == 0: ans = ans + int(n[position]) * (16 ** power)

                        power = power + 1
                        position = position - 1

                    speak(f"The decimal form of {n} is: {ans}")


                elif speech == "11":
                    speak("Say your hexadecimal number: ")
                    SpeechToText()
                    n = speech
                    n1 = n[::-1]
                    ans = ""
                    position = len(n1) - 1

                    for i in range(len(n1)):
                        diction = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                                   '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010',
                                   'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
                        for key, value in diction.items():
                            if n1[position] == key: ans = ans + value

                        position = position - 1

                    speak(f"The binary form of {n} is: {ans}")


                elif speech == "12":
                    speak("Say your hexadecimal number: ")
                    n = input()
                    n1 = n[::-1]
                    bin = ""
                    position = len(n1) - 1

                    for i in range(len(n1)):
                        diction = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                                   '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010',
                                   'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
                        for key, value in diction.items():
                            if n1[position] == key: bin = bin + value

                        position = position - 1

                    bin1 = bin
                    while len(bin1) % 3 != 0: bin1 = '0' + bin1
                    ans = ""
                    position = len(bin1) - 1
                    for i in range(len(bin1) // 3):
                        temp = ""
                        for i in range(3):
                            temp = temp + bin1[position]
                            position = position - 1
                        temp = temp[::-1]

                        diction = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6',
                                   '111': '7'}
                        for key, value in diction.items():
                            if temp == key: ans = ans + value

                    ans = ans[::-1]
                    speak(f"The octal form of {n} is: {ans}")


                else:
                    break


        elif speech == "exit":
            exit()

    def gotoBack(self):
        a = LogIn()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex() + 1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome = WelcomeScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedWidth(1900)
    widget.setFixedHeight(1000)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
