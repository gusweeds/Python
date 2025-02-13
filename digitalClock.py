
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digitial Clock")
        self.setGeometry(600, 400, 300, 100)

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.time_label.setStyleSheet("font-size: 150px;"     
                                      "color: hsl(203, 82%, 56%);")
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DIGITAL.ttf")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)
            if font_family:
                my_Font = QFont(font_family[0], 150)
                self.time_label.setFont(my_Font)
            else:
                print("Font family list is empty.")
        else:
            print("Failed to load font.")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
       
                                      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())



