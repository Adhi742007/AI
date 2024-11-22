from Brain.AIBrain import ReplyBrain
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import threading
import sys
import speech_recognition as sr
from googletrans import Translator
import pyttsx3

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 250, 231, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -190, 641, 1021))
        self.label_2.setSizeIncrement(QtCore.QSize(50, 59))
        self.label_2.setBaseSize(QtCore.QSize(50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\GUI materials\\monophy.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, -210, 501, 851))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(690, 60, 341, 571))
        self.plainTextEdit.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-bottom-color: rgb(71, 71, 71);\n"
"border-radius:10px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(705, 616, 311, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(706, 46, 311, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 4, 591, 231))
        self.label_6.setStyleSheet("font: 63 18pt \"Yu Gothic UI Semibold\";")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\GUI materials\\CUBIC (1).png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(924, -54, 1781, 911))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\GUI materials\\CUBIC (4).png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-40, 600, 721, 131))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(370, 640, 721, 131))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 660, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 660, 93, 28))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: rgb(99, 143, 102);\n"
"    border-radius:5px ;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    font: 63 10pt \"Bahnschrift SemiBold SemiConden\";\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    background-color:rgba(255, 107, 107, 255);\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: rgb(121, 121, 121);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(160, 660, 93, 28))
        self.pushButton2.setStyleSheet("QPushButton#pushButton2{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius:5px ;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    font: 63 10pt \"Bahnschrift SemiBold SemiConden\";\n"
"}\n"
"QPushButton#pushButton2:pressed{\n"
"    background-color:rgba(255, 107, 107, 255);\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton2:hover{\n"
"    background-color: rgb(121, 121, 121);\n"
"}")
        self.pushButton2.setObjectName("pushButton2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(464, 630, 131, 21))
        self.label_10.setStyleSheet("font: 63 10pt \"Bahnschrift SemiBold SemiConden\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(463, 633, 81, 20))
        self.label_11.setObjectName("label_11")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(610, 660, 93, 28))
        self.pushButton3.setStyleSheet("QPushButton#pushButton3{\n"
"background-color: rgb(11, 176, 0);\n"
"    border-radius:5px ;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    font: 63 10pt \"Bahnschrift SemiBold SemiConden\";\n"
"}\n"
"QPushButton#pushButton3:pressed{\n"
"    background-color:rgba(255, 107, 107, 255);\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton3:hover{\n"
"    background-color: rgb(121, 121, 121);\n"
"}")
        self.pushButton3.setObjectName("pushButton3")
        self.label_3.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.plainTextEdit.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.comboBox.raise_()
        self.pushButton.raise_()
        self.pushButton2.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.pushButton3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.addItem("")
        self.comboBox.addItem("RESUME")
        self.comboBox.addItem("PHONE")
        self.comboBox.addItem("CARBON")
        self.comboBox.addItem("ECO TRIP PLANNER")
        self.pushButton.clicked.connect(self.start)
        self.pushButton2.clicked.connect(self.stop)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "______________________________________________________________________________"))
        self.label_5.setText(_translate("MainWindow", "______________________________________________________________________________"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton2.setText(_translate("MainWindow", "STOP"))
        self.label_10.setText(_translate("MainWindow", "Applications"))
        self.label_11.setText(_translate("MainWindow", "____________________________________"))
        self.pushButton3.setText(_translate("MainWindow", "OPEN"))

    def Listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            T = ('''
Listening...''')
            print("/")
            QtCore.QMetaObject.invokeMethod(self.plainTextEdit, 'appendPlainText',QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, T))
            r.pause_threshold = 0.5
            audio = r.listen(source,0,8) # Listening Mode.....
        try:
            R = ('''
Recognizing...''')
            QtCore.QMetaObject.invokeMethod(self.plainTextEdit, 'appendPlainText',QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, R))
            print("..")
            query = r.recognize_google(audio,language="en")
        except:
            return ""
        query = str(query).lower()
        return query

    def TranslationHinToEng(self,Text):
        line = str(Text)
        translate = Translator()
        result = translate.translate(line)
        data = result.text
        return data

    def MicExecution(self):
        query = self.Listen()
        data = self.TranslationHinToEng(query)
        return data

    def start(self):
        movie = QtGui.QMovie("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\GUI materials\\monophy.gif")
        self.label_2.setMovie(movie)
        movie.start()
        # Start the speech processing thread
        speech_thread = threading.Thread(target=self.process_speech)
        speech_thread.start()

    def stop(self):
        QtCore.QCoreApplication.quit()

    def clicker(self):
        a = self.comboBox.currentText()
        if 'PHONE' in a:
            # Pause the AI program
            self.paused = True
            # Launch the phone.py program
            phone_script_path = "C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\App\\phone.py"
            self.phone_process = QtCore.QProcess()
            self.phone_process.finished.connect(self.resume_ai)
            self.phone_process.start("python", [phone_script_path])
        elif 'RESUME' in a:
            # Start the AI program
            self.paused = False
            self.start_jarvis()
        elif 'ECO TRIP PLANNER' in a:
            os.startfile("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\App\\eco.py")
        elif 'CARBON' in a:
            os.startfile("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\App\\carbon.py")

    def resume_ai(self):
        # Resume the AI program
        self.paused = False
        self.start_jarvis()

    def process_speech(self):

        while True:

            Data = self.MicExecution()
            Data1 = str(Data).replace(".", "")
            Reply = ReplyBrain(Data1)
            TrueReply = f"\nYou : {Data} \n\nCubic : {Reply}"
            engine = pyttsx3.init("sapi5")
            voices = engine.getProperty('voices')
            engine.setProperty('voices', voices[1].id)
            engine.setProperty('rate', 170)
            # Update the text box with the reply
            QtCore.QMetaObject.invokeMethod(self.plainTextEdit, 'appendPlainText', QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, TrueReply))
            engine.say(f"{Reply}")
            engine.runAndWait()

    def start_jarvis(self):
        speech_thread = threading.Thread(target=self.process_speech)
        speech_thread.start()


class Gui_Start(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.pushButton3.clicked.connect(self.jarvis_ui.clicker)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Gui_Start()
    MainWindow.show()
    sys.exit(app.exec_())
