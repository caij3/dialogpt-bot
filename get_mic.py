import speech_recognition as sr
import sounddevice as sd

#print(sd.check_output_settings())
if __name__ == '__main__':
    for mic_id, mic_name in enumerate(sr.Microphone.list_microphone_names()):
        print(f'{mic_id}: {mic_name}')