from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class okayDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Default geometry configuration

        self.setWindowTitle('Success')
        self.setFixedSize(200, 100)
        self.layout = QGridLayout()

        # Centering ok window

        self.mainGeometry = self.frameGeometry()
        centralPosition = QDesktopWidget().availableGeometry().center()
        self.mainGeometry.moveCenter(centralPosition)
        self.move(self.mainGeometry.topLeft())

        self.setLayout(self.layout)
        self.show()