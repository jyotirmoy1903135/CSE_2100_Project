import os
import time

speech = input("Input your command ")
if "open microsoft excel" in speech or "open ms excel" in speech:
    print("Opening microsoft excel, sir")
    time.sleep(0.5)
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
