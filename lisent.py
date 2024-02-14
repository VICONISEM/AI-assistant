import speech_recognition as sr
import speak_module
from time import sleep
from speech_recognition import UnknownValueError



# global variables
r = sr.Recognizer()
source = sr.Microphone(0)
keywords = [("tito", 1), ("wakeup tito", 1)]


def start_reco():
    speak_module.speak("tell me how i can help you to day ")
    r=sr.Recognizer()
    with sr.Microphone(0) as source:
        audio=r.listen(source)
    text=r.recognize_google(audio)
    speak_module.speak(text)
    
    
    
def callback(recognizer, audio):
    try:
        text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        if ("tito" in text or "wakeup tito" ):
            speak_module.speak("yes sir")
            start_reco()
            
    except UnknownValueError as e:
        print("Couldn't understand the audio. Please try again.")



def start_recognize():
    print("listen........")
    r.listen_in_background(source, callback)
    sleep(10)


start_recognize()

