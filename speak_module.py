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

    
