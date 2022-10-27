import os
import time

speech = input("Input your command ")
if "open microsoft word" in speech or "open ms word" in speech:
    print("Opening microsoft word, sir.")
    time.sleep(0.5)
    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
