import pyttsx3

def speech(text):
    tts_engine=pyttsx3.init()
    voices=tts_engine.getProperty("voices")
    tts_engine.setProperty('voice',voices[1].id)
    tts_engine.setProperty('rate',120)
    tts_engine.say(text)
    tts_engine.runAndWait()
    
