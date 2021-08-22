from conf import *

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

