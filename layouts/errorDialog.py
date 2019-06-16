from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class errorDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Default geometry configuration

        self.setWindowTitle('Error')
        self.setFixedSize(400, 100)
        self.layout = QGridLayout()

        # Centering ok window

        self.mainGeometry = self.frameGeometry()
        centralPosition = QDesktopWidget().availableGeometry().center()
        self.mainGeometry.moveCenter(centralPosition)
        self.move(self.mainGeometry.topLeft())

        self.label = QLabel('An error has occured, check your settings')
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)


        self.setLayout(self.layout)
        self.show()