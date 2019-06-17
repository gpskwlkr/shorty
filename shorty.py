import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from urlCreators.hideURL import hide
from urlCreators.tinyURL import tinyurl
from urlCreators.localhost import local
from urlCreators.myHeroku import heroku
from layouts.result import resultWindow

class Window(QWidget): 

    def __init__(self):
        super().__init__()

        self.radioFunctions = {'hideuri.com' : hide.getShortUrl, 'tinyURL.com' : tinyurl.getShortUrl, \
            'localhost' : local.getShortUrl, 'My Heroku' : heroku.getShortUrl}

        self.services = {0 : QRadioButton("hideuri.com"), \
                        1 : QRadioButton("tinyURL.com"), 
                        2 : QRadioButton("localhost"),
                        3 : QRadioButton("My Heroku")}

        self.services[0].setChecked(True)
        self.services[2].setToolTip('For nerds')

        # Default geometry configuration

        self.setWindowTitle('Shorty')
        self.setFixedSize(550, 200)
        self.layout = QVBoxLayout()

        # Centering application

        self.mainGeometry = self.frameGeometry()
        centralPosition = QDesktopWidget().availableGeometry().center()
        self.mainGeometry.moveCenter(centralPosition)
        self.move(self.mainGeometry.topLeft())

        # UI initialization

        self.button = QPushButton('Shorten', self)
        self.button.clicked.connect(self.onClick)
        self.button.setMaximumHeight(50)
        self.button.setToolTip('Shorten')
        self.button.setStyleSheet('border-style: solid; border-width: 2px; border-radius: 8px; border-color: #22323B; font-size: 15px;')

        self.label = QLabel('URL')
        self.label.setStyleSheet('margin-top:10px;')

        self.textbox = QLineEdit(self)
        self.textbox.setStyleSheet('background-color:#243640; border:none; margin-bottom: 10px;')
        
        self.label.setAlignment(Qt.AlignTop)
        self.layout.setAlignment(Qt.AlignTop)
        
        self.layout.addWidget(self.createServicesGroup())
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
        
        self.show()

    def createServicesGroup(self):
        groupBox = QGroupBox("Preffered service")
        vbox = QHBoxLayout()

        for i in self.services.keys():
            vbox.addWidget(self.services[i])

        vbox.addStretch()
        groupBox.setMaximumHeight(100)
        groupBox.setAlignment(Qt.AlignTop)
        groupBox.setLayout(vbox)

        return groupBox

    def onClick(self):
        for service in self.services.values():
            if service.isChecked():
                url = self.radioFunctions[service.text()](self.textbox.text())
        res = resultWindow(url)
        res.exec_()


app = QApplication(sys.argv)
app.setStyleSheet('* { background-color: #19252B; color:white; }')
window = Window()
sys.exit(app.exec())