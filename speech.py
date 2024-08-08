import speech_recognition as sr
import cmds, stock_actions

STC = sr.Recognizer()
global wake_cmd
wake_cmd = False

def get_audio():
    with sr.Microphone() as source:
        audio = STC.listen(source)
        return audio
    
while True:
    if STC.recognize_vosk(get_audio()) == "hey Phoenix":
        wake_cmd = True
        stock_actions.say_help()
    if wake_cmd == True:
        cmds.cmds()
        