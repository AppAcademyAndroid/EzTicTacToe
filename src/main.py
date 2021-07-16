import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow


def test(test_list: []):
    print(test_list)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
