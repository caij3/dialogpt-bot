from gtts import gTTS
import os
import speech_recognition as sr
import playsound

FILE = "voice.mp3"

def speak(text):
    try:
        tts = gTTS(text=text,lang="en")
        filename = "sound.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove("sound.mp3")
    except Exception as e:
        print(e)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            if not said:
                return ""
            #speak(said)
            print(said)
            return said
        except Exception as e:
            print(e)