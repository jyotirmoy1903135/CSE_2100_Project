import os
import time

speech = input("Input your command ")
if "open chrome" in speech or "open google chrome" in speech:
    print("Opening google chrome, sir")
    time.sleep(0.5)
    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
