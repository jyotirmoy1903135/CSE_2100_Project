import datetime

def wishMe():
    hour = int(datetime.datetime.now().hour)
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

    print(Wish_according_to_time)

wishMe()
