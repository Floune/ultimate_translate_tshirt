from conf import *
from utils import *


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
                speak(res) if vocal == True else print(res)
        
        except sr.UnknownValueError:
            pass

tshirt()


