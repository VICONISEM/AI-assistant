import datetime as dt
from speak_module import speak
import calendar
import pyttsx3

def speak(text:str):
    tts_engine=pyttsx3.init()
    voices=tts_engine.getProperty("voices")
    tts_engine.setProperty('voice',voices[0].id)
    tts_engine.setProperty('rate',120)
    parts=text.split("@pause")
    for part in parts:
        tts_engine.say(part)
        tts_engine.runAndWait()

    

if __name__ == "__main__":
    today=dt.date.today()
    name_of_day=calendar.day_name[today.weekday()]
    H=dt.datetime.now().hour
    M=dt.datetime.now().minute
    str=f"good moring sir @p today is {name_of_day} @p {today}"
    
    speak()