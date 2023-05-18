# DialoGPT Bot
This is a general purpose voice chatbot created using DialoGPT, combined with the use of WhisperAI and Microsoft text-to-speech.

# Installation
To install, you can clone the repository using: git clone https://github.com/caij3/dialogpt-bot 
<br>
If git is not installed, you can download the ZIP file and unzip it.
<br>
You can install dependencies using: pip install -r requirements.txt
<br>

Note: For Whisper AI speech recognition, you must install ffmpeg. A guide for installation can be found here: https://phoenixnap.com/kb/ffmpeg-windows

If you are receiving an error, follow the **Troubleshooting** section found at the end of this README

# How to use
To use this program, run the main.py python file. You can use the command: python main.py
<br>
Once run, wait until you see the **Listening** prompt before speaking. The chatbot will then respond.

# How it works
The program receives input from the microphone and converts it to text. This can be done using two options: either through Whisper AI's speech recognition or Google's speech recognition. It then passes the input through Microsoft's DialoGPT large language model. After receiving a response from DialoGPT, the response is converted to an audio file and spoken with using Microsoft's text-to-speech.

# Troubleshooting
**Error:** AttributeError: Could not find PyAudio; check installation...can't use speech Recognition
<br>
Solution: Either PyAudio is not installed or you have an incorrect version of playsound.
<br>

To install PyAudio, use pip install PyAudio
<br>
If PyAudio is already installed and you are still receiving this error, try a different version of playsound. To do this, use:
<br>
pip uninstall playsound
<br>
pip install playsound==1.2.2

