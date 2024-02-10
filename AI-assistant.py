import pyttsx3

def speech(text):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',120)
    engine.say(text)
    engine.runAndWait()

speech("hello world")