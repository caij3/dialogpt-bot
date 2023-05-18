import edge_tts
import os
import sounddevice as sd
import soundfile as sf
import playsound
from gtts import gTTS

DEVICE_ID = sd.default.device
VOICE = "en-IE-EmilyNeural"
FILENAME = "sound.mp3"

# Play audio using Microsoft text-to-speech voices
async def speak(text,device_id=DEVICE_ID):
    try:
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(FILENAME)
        data,fs = sf.read(FILENAME,dtype='float32')
        sd.play(data,fs,device=device_id)
        sd.wait()
        #playsound.playsound(filename)
        os.remove(FILENAME)
    except Exception as e:
        print(e)

# Plays the audio file using Google text-to-speech
def speak_google(text):
    try:
        tts = gTTS(text=text,lang="en")
        tts.save(FILENAME)
        playsound.playsound(FILENAME)
        os.remove(FILENAME)
    except Exception as e:
        print(e)