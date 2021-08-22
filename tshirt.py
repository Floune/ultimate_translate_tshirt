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
    "russe": "ru",
    "serbe": "sr",
}


def displayConfiguration():
    print("----Configuration----")
    print("langue de sortie: " + tolang)
    print("-- Langues disponibles --")
    for lang in languages:
        print(lang)

def configureTarget(newlang):
    global tolang
    if newlang in languages:
        tolang = languages[newlang]
        print("nouvelle langue de traduction: " + newlang)

def megaTrans(text):
    translated = GoogleTranslator(source=fromlang, target=tolang).translate(text=text)
    print(translated)


def tshirt():

    while True:
        try:
            with micro as source:
                audio_data = r.listen(source)
                print("...")
                result = r.recognize_google(audio_data, language="fr-FR")

            if result == "configuration":
                displayConfiguration()

            elif result.split()[0] == "destination":
                configureTarget(result.split()[1])

            elif result == "je me retire de la vie politique":                
                sys.exit()

            else:
                megaTrans(result)
        
        except sr.UnknownValueError:
            pass

tshirt()


