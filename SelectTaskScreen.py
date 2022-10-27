import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import time
import re
import datetime
import webbrowser
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
        if speech == "open youtube":
            webbrowser.open("youtube.com")
        elif speech == "open google":
            webbrowser.open("google.com")
        elif speech == "open a website":
            speak("Please say the name of the website you want to open")
            SpeechToText()
            webbrowser.open(speech)
        #elif speech == f"search   in wikipedia":
        elif "what's the time" in speech:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")
        elif speech == "exit":
            exit()

    def gotoBack(self):
        a = LogIn()
        widget.addWidget(a)
        widget.setCurrentIndex(widget.currentIndex() + 1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome = SelectTask()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedWidth(1900)
    widget.setFixedHeight(1000)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
