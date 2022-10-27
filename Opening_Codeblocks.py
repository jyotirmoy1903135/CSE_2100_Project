import os
import time

speech = input("Input your command ")
if "open codeblocks" in speech or "open code blocks" in speech:
    print("Opening codeblocks, sir.")
    time.sleep(0.5)
    os.startfile(
        r"C:\Users\ASUS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\CodeBlocks\CodeBlocks.lnk")
