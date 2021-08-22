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
vocal = False

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
