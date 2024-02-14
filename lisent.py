import speech_recognition as sr
import speak_module
from time import sleep
from speech_recognition import UnknownValueError



# global variables
r = sr.Recognizer()
source = sr.Microphone(0)
keywords = [("tito", 0.7), ("wakeup tito", 0.7)]


def start_main():
    speak_module.speak("tell me how i can help you to day ")
    r=sr.Recognizer()
    with sr.Microphone(0) as source:
        audio=r.listen(source)
    text=r.recognize_google(audio)
    speak_module.speak(text)
    


def start_recognize():
    print("listen ........")
    with source:
       audio= r.listen(source)
    try:
        text = r.recognize_sphinx(audio, keyword_entries=keywords)
        if ("tito" in text or "wakeup tito" ):
            speak_module.speak("yes sir")
            start_main()
        
    except UnknownValueError as e:
     print("Couldn't understand the audio. Please try again.")



start_recognize()

