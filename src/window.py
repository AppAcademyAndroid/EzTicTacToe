from PyQt5.QtWidgets import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        width = 500

        self.setWindowTitle('EzSudoku')
        self.setFixedWidth(width)
        # self.setStyle('Windows')

        def on_button_clicked():
            alert = QMessageBox()
            alert.setText('Button clicked')
            alert.show()

        self.button = QPushButton('Test', self)
        self.label_1 = QLabel('Hello world!')
        self.label_1.move(0, 0)
        self.label_1.resize(120, 80)

        self.show()
