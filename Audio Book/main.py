# IMPORTING PACKAGES/MODULES
import sys
import pyttsx3

from PyQt6 import QtWidgets
from PyQt6.uic import loadUi

# DECLARING GLOBAL VARIABLES
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Initial voice speed
voices = engine.getProperty('voices')  # Getting voiced from pyttsx3 engine
voice_array = ["Microsoft David (Male - American Accent)", "Microsoft Zara (Female - American Accent)"]


# MAIN WINDOW
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('main.ui', self)

        # EVENTS
        self.play_button.clicked.connect(self.play)  # Play button click event
        self.speed_slider.valueChanged.connect(self.change_speed)  # Speed slider value change event
        self.voices_combo_box.addItems(voice_array)  # Adding voices to combo-box

    # PLAY AUDIO BOOK BUTTON
    def play(self):
        voice_text = str(self.voices_combo_box.currentText())
        if voice_text == "Microsoft David (Male - American Accent)":
            engine.setProperty('voice', voices[0].id)

        elif voice_text == "Microsoft Zara (Female - American Accent)":
            engine.setProperty('voice', voices[1].id)
        text = self.text.toPlainText()
        engine.say(text)
        engine.runAndWait()

    # CHANGING SPEED SLIDER
    def change_speed(self):
        speed = self.speed_slider.value()
        self.speed_number.setText(str(speed))
        engine.setProperty('rate', speed)


# MAIN
if __name__ == '__main__':
    '''=======================>
        CREATING WINDOW
    ==========================>'''
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedHeight(400)
    widget.setFixedWidth(500)
    widget.setWindowTitle("Audio Book")
    widget.show()
    app.exec()
