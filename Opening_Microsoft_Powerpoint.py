import os
import time

speech = input("Input your command ")
if "open microsoft powerpoint" in speech or "open ms powerpoint" in speech:
    print("Opening microsoft powerpoint, sir")
    time.sleep(0.5)
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
