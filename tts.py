from gtts import gTTS
import os
import speech_recognition as sr
import playsound

# Name of the audio file generated
FILE = "voice.mp3"

# Plays the audio file
def speak(text):
    try:
        tts = gTTS(text=text,lang="en")
        filename = "sound.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove("sound.mp3")
    except Exception as e:
        print(e)

# Listens to audio
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
            print(said)
            return said
        except Exception as e:
            print(e)