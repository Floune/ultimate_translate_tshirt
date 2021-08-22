from conf import *

def displayHelp():
    print("\n")
    print("INFORMATIONS")
    print("\t- langue: " + tolang)
    print("\t- mode vocal: activé") if vocal else print("\t- mode vocal: désactivé")
    print("COMMANDES DISPONIBLES")
    print("\t- parle")
    print("\t- ne parle plus")
    print("\t- destination <langue> ( voir langues disponibles)")
    print("\t- manuel")
    print("\t- je me retire de la vie politique")
    print("Langues disponibles")
    for lang in languages:
        print("\t- " + lang)

def configureTarget(newlang):
    global tolang
    if newlang in languages:
        tolang = languages[newlang]
        print("nouvelle langue de traduction: " + newlang)

def megaTrans(whatDidYouSay):
    return GoogleTranslator(source=fromlang, target=tolang).translate(text=whatDidYouSay)


def speak(wannaHear, info=False):
    language = tolang if info == False else "fr"
    filename = "tts.mp3"
    gTTS(text=wannaHear, lang=language).save(filename)
    os.system("mpg123 " + filename)


def recognize():
    with micro as source:
        audio_data = r.listen(source)
        print("...")
        return r.recognize_google(audio_data, language="fr-FR")

