from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class okayWindow(QDialog):
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
        self.setWindowModality(True)

        # self.button = QPushButton('Close')
        # self.button.setToolTip('Close window')
        # self.button.setIcon(QIcon('graphics/tick.png'))
        # self.button.clicked.connect(self.close)

        # self.layout.addWidget(self.button, 0, 0)
        self.setLayout(self.layout)
        self.show()