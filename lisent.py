import speech_recognition as sr
import speech

r=sr.Recognizer()
source=sr.Microphone(0)
with source as mic:
    audio=r.listen(mic)
text=r.recognize_google(audio) 
speech.speech(text)

