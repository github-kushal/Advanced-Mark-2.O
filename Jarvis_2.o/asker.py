import speech_recognition as sr
import pyttsx3
import os
import sys

# stderr = sys.stderr
# sys.stderr = open(os.devnull, 'w')
# sys.stderr = stderr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
# for voice in voices:
#     print(voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("hello sir i am your virtual assistant")
# engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

speak("hello")
    
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            print("say that again please...")
            return "none"
        return query
    

def clear():
    os.system('cls')


    