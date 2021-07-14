import sys
from window import Window
from PyQt5.QtWidgets import QApplication


def main():
    print('hello')
    app = QApplication([])
    window = Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
