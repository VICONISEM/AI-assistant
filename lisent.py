import speech_recognition as sr
import speak_module
import datetime as dt
from speech_recognition import UnknownValueError



# global variables
r = sr.Recognizer()
source = sr.Microphone(0)
keywords = [("tito", 0.7), ("wakeup tito", 0.7)]
    
def main():
    while True:
        speak_module.speak("how can i help you sir")
        r=sr.Recognizer()
        with sr.Microphone(0) as source:
            audio=r.listen(source)
        text=r.recognize_google(audio)
        speak_module.speak(text)
    


def wakeupTito():
    print("listen ........")
    with source:
       audio= r.listen(source)
    try:
        text = r.recognize_sphinx(audio, keyword_entries=keywords)
        if ("tito" in text or "wakeup tito" ):
            speak_module.speak("yes sir")
            main()
        
    except UnknownValueError as e:
     print("Couldn't understand the audio. Please try again.")



wakeupTito()

