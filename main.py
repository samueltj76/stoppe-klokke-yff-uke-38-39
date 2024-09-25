# python pyqt5

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout, QHBoxLayout) # komponenter fra pyqt5 
from PyQt5.QtCore import QTimer, QTime, Qt 

class Stopwatch(QWidget): #klasse Qwidget som bruke til å lage GUI-elementer
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0) #dette gjør at timeren starter på 0 timer 0 minnuter 0 sekunder og 0 millisekunder når stoppekloken starter
        self.time_label = QLabel("00:00:00.00", self) #viser den nåverende tiden
        self.start_button = QPushButton("Start", self) #startknapp for å få timeren til å gå opp
        self.stop_button = QPushButton("Stop", self)   #stopknapp som stopper timeren
        self.reset_button = QPushButton("Reset", self) #resetknapp som reseter tiden tilbake til 00.00.00.00
        self.timer = QTimer(self) #
        self.initUI()

    def initUI(self):
        self.setWindowTitle("stoppe klokke")

        vbox = QVBoxLayout() #en layout som plaserer Qtime og start,stop og reset kappene knappene 
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()#setter start stop og reset knappene ved siden av hverandre

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        #setter stilen til knappene Qpushbuttons og Qlabel, søtrelse på knappene og label, bakgrunn farge og border radius
        #setstylesheet brukes til å legge inn css i pyqt5
        self.setStyleSheet(""" 
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton{
                font-size: 50px; 
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)
        # funksjoner for å få kanppene til å funke
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10) #starter timeren med 

    def stop(self): #stopper timeren
        self.timer.stop()

    def reset(self): #resetter timeren til 00.00.00
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    stopwatch = Stopwatch() #oppretter et stoppekloke vindu
    stopwatch.show() #viser stoppekloke viduet
    sys.exit(app.exec_()) #åpner i pyqt5 og sørger for at prugrammet kjøret fra til det blir lukket



