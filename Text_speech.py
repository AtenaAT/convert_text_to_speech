#convering text from my_text.txt to speech!
#AT

from gtts import gTTS
import os

file = open("my_text.txt", "r").read()

speech = gTTS(text=file, lang='en')
speech.save("voice.mp3") #save the voice
os.system("voice.mp3")
