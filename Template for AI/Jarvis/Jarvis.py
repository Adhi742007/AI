from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Jarvis : Wait For Few Seconds More")
from Main import MainTaskExecution
import os


def MainExecution():
    Speak("Hello World")
    Speak("I'm Jarvis, I'm Ready To Assist.")
    print("  ")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:

            pass

        elif 'open phone' in Data:# Specific COmmand
            os.startfile("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\App\\App.py")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()

