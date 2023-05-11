# DialoGPT Bot
This is a chatbot created using DialoGPT

# Installation
To install, you can clone the repository using: git clone https://github.com/caij3/dialogpt-bot 
<br>
If git is not installed, you can download the ZIP file and unzip it.
<br>
You can install dependencies using: pip install -r requirements.txt
<br>

If you are receiving an error, follow the **Troubleshooting** section found at the end of this README

# How to use
To use this program, run the main.py python file. You can use the command: python main.py
<br>
Once run, wait until you see the **Listening** prompt before speaking. The chatbot will then respond.

# How it works
The program receives input from the microphone and converts it to text using Google's speech recognition API. It then passes the input through Microsoft's DialoGPT language model. Lastly, Google's Text-to-Speech is used to talk.

# Troubleshooting
**Error:** AttributeError: Could not find PyAudio; check installation...can't use speech Recognition
Solution: Either PyAudio is not installed or you have an incorrect version of playsound.
<br>
To install PyAudio, use pip install PyAudio
<br>
If PyAudio is already installed and you are still receiving this error, try a different version of playsound. To do this, use:
<br>

pip uninstall playsound
<br>

pip install playsound==1.2.2