        import webbrowser
        speech = ("Input command: ")
        speech = speech.lower()
        if "open google" in speech:
            speak("Opening google, sir")
            time.sleep(0.5)
            webbrowser.open("google.com")
