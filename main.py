import speech_recognition as sr
import datetime as dt
from speech_recognition import UnknownValueError
import calendar
import pyttsx3



# global variables
r = sr.Recognizer()
source = sr.Microphone(0)
keywords = [("tito", 0.7), ("wakeup tito", 0.7)]

def speak(text:str):
    tts_engine=pyttsx3.init()
    voices=tts_engine.getProperty("voices")
    tts_engine.setProperty('voice',voices[0].id)
    tts_engine.setProperty('rate',120)
    parts=text.split("@p")
    for part in parts:
        tts_engine.say(part)
        tts_engine.runAndWait()


        
def time_date():
    date=dt.date.today()
    name_of_day=calendar.day_name[today.weekday()]
    H=dt.datetime.now().hour
    M=dt.datetime.now().minute
    if H >=0 and H <= 12: 
        str=f"good moring sir @p today is {name_of_day} @p {today} time is {H} @p ,{M}"
    else :
        str=f"good afternon sir @p today is {name_of_day} @p {today} @p time is {H} ,{M}"
    return str
        
    


    
    
def main():
    while 1 :
        speak("how can i help you sir")
        r=sr.Recognizer()
        with sr.Microphone(0) as source:
            audio=r.listen(source)
        text=r.recognize_google(audio)
        speak(text)
    




def wakeupTito():
    print("listen ........")
    with source:
       audio= r.listen(source)
    try:
        text = r.recognize_sphinx(audio, keyword_entries=keywords)
        if ("tito" in text or "wakeup tito" ):
            speak(time_date())
            main()
        
    except UnknownValueError as e:
     print("Couldn't understand the audio. Please try again.")






wakeupTito()
