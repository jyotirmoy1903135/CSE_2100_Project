        import webbrowser
        speech = ("Input command: ")
        if "open youtube" in speech:
            speak("Opening youtube, sir")
            time.sleep(0.5)
            webbrowser.open("youtube.com")
