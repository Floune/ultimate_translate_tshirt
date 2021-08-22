import sys
import os
import speech_recognition as sr
import pyaudio
from deep_translator import GoogleTranslator
from gtts import gTTS

micro = sr.Microphone()
r = sr.Recognizer()
fromlang = "fr"
tolang = "en"
audio_language = "fr-FR"
vocal = False
filename = "tts.mp3"
CRED = '\033[91m'
CEND = '\033[0m'


languages = {
    "espagnol": "es",
    "allemand": "de",
    "portugais": "pt",
    "japonais": "ja",
    "arabe": "ar",
    "français": "fr",
    "russe": "ru",
    "serbe": "sr",
}
