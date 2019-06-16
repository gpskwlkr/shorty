from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from layouts.ok import okayWindow

class resultWindow(QWidget):
    def __init__(self, url):
        super().__init__()

        # Default geometry configuration

        self.setWindowTitle('Result')
        self.setFixedSize(300, 100)
        self.layout = QGridLayout()

        # Centering result window

        self.mainGeometry = self.frameGeometry()
        centralPosition = QDesktopWidget().availableGeometry().center()
        self.mainGeometry.moveCenter(centralPosition)
        self.move(self.mainGeometry.topLeft())
        self.setWindowModality(True)

        # UI configuration

        self.label = QLabel(url)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)

        self.button = QPushButton("Copy to clipboard", self)
        self.button.clicked.connect(self.copy)

        # System-wide clipboard

        self.qclip = QApplication.clipboard()
        self.qclip.clear(mode=self.qclip.Clipboard)


        # Layout configuration

        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 1, 0)

        self.setLayout(self.layout)
        self.show()

    def copy(self):
        self.qclip.setText(self.label.text(), mode=self.qclip.Clipboard)
        ok = okayWindow()
        button = QPushButton('Close')
        button.setToolTip('Close window')
        button.setIcon(QIcon('graphics/tick.png'))
        button.clicked.connect(ok.close)

        ok.layout.addWidget(button)
        ok.exec_()