import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget): 
    def __init__(self):
        super().__init__()

        # Default geometry configuration

        self.title = 'Shorty'
        self.width = 500
        self.height = 200
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.layout = QVBoxLayout()

        # Centering application

        self.mainGeometry = self.frameGeometry()
        centralPosition = QDesktopWidget().availableGeometry().center()
        self.mainGeometry.moveCenter(centralPosition)
        self.move(self.mainGeometry.topLeft())

        # UI initialization

        self.button = QPushButton('Short', self)
        # self.button.clicked.connect(self.onClick)
        self.button.setMaximumHeight(50)
        self.button.setToolTip('Shorten')
        self.button.setStyleSheet('border-style: solid; border-width: 2px; border-radius: 10px; border-color: #22323B; font-size: 16px;')

        self.label = QLabel('URL')

        self.label.setAlignment(Qt.AlignTop)
        self.layout.setAlignment(Qt.AlignTop)
        
        self.layout.addWidget(self.createServicesGroup())
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.createURLTextBox())
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
        
        self.show()

    def createServicesGroup(self):
        groupBox = QGroupBox("Preffered service")

        bitly = QRadioButton("bit.ly")
        googl = QRadioButton("goo.gl")
        local = QRadioButton("localhost (if you have a server running)")

        bitly.setChecked(True)

        vbox = QHBoxLayout()
        vbox.addWidget(bitly)
        vbox.addWidget(googl)
        vbox.addWidget(local)
        vbox.addStretch()
        groupBox.setMaximumHeight(100)
        groupBox.setAlignment(Qt.AlignTop)
        groupBox.setLayout(vbox)

        return groupBox

    def createURLTextBox(self):
        textbox = QLineEdit(self)
        textbox.setStyleSheet('background-color:#243640;')
        return textbox

app = QApplication(sys.argv)
app.setStyleSheet('* { background-color: #19252B; color:white; }')
window = Window()
sys.exit(app.exec())