import sys
import speech_recognition as sr
import pyaudio
from deep_translator import GoogleTranslator

micro = sr.Microphone()
fromlang = "fr"
tolang = "en"
r = sr.Recognizer()

languages = {
    "espagnol": "es",
    "allemand": "de",
    "portugais": "pt",
    "chinois": "fz",
    "japonais": "ja",
    "arabe": "ar",
    "français": "fr",
}

def configureTarget(newlang):
    global tolang
    if newlang in languages:
        tolang = languages[newlang]
        print("nouvelle langue de traduction: " + newlang)

def configureSource(newlang):
    global fromlang
    if newlang in languages:
        fromlang = languages[newlang]
        print("nouvelle langue d'input': " + newlang)


def megaTrans(text):
    translated = GoogleTranslator(source=fromlang, target=tolang).translate(text=text)
    print(translated)


def tshirt():

    while True:
        try:
            with micro as source:
                audio_data = r.listen(source)
                result = r.recognize_google(audio_data, language="fr-FR")

            if result.split()[0] == "destination":
                configureTarget(result.split()[1])

            if result.split()[0] == "source":
                configureSource(result.split()[1])

            if result == "extinction":
                
                sys.exit()

            else:
                megaTrans(result)
        
        except sr.UnknownValueError:
            print("incompréhensible")

tshirt()


