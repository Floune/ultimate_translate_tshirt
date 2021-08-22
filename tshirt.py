import sys
import os
import speech_recognition as sr
import pyaudio
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO
from playsound import playsound

micro = sr.Microphone()
fromlang = "fr"
tolang = "en"
r = sr.Recognizer()
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


def displayConfiguration():
    print("----Configuration----")
    print("langue de sortie: " + tolang)
    print("mode vocal activé") if vocal else print("mode vocal désactivé")
    print("--Langues disponibles--")
    for lang in languages:
        print(lang)

def configureTarget(newlang):
    global tolang
    if newlang in languages:
        tolang = languages[newlang]
        print("nouvelle langue de traduction: " + newlang)

def megaTrans(whatDidYouSay):
    translated = GoogleTranslator(source=fromlang, target=tolang).translate(text=whatDidYouSay)
    print(translated)
    return translated


def speak(wannaHear, info=False):
    language = tolang if info == False else "fr"
    tts = gTTS(text=wannaHear, lang=language)
    filename = "tts.mp3"
    tts.save(filename)
    os.system("mpg123 " + filename)


def recognize():
    with micro as source:
        audio_data = r.listen(source)
        print("...")
        return r.recognize_google(audio_data, language="fr-FR")


def tshirt():
    global vocal
    while True:
        try:
            result = recognize()
            if result == "configuration":
                displayConfiguration()

            elif result == "parle":
                vocal = True
                speak("d'accord", True)
            
            elif result == "ne parle plus":
                vocal = False
                speak("je me tais", True)

            elif result.split()[0] == "destination":
                configureTarget(result.split()[1])

            elif result == "je me retire de la vie politique":                
                sys.exit()

            else:
                res = megaTrans(result)
                if vocal == True:
                    speak(res)
        
        except sr.UnknownValueError:
            pass

tshirt()


