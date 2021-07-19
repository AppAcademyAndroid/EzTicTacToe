import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow


main_board = [[0] * 3] * 3


def print_board(board: [[]]):
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(board[i][j])
            else:
                print(f"{board[i][j]} ", end="")


def on_action(x: int, y: int):
    print(f'action {x}, {y}')


def on_reset():
    print('reset')


def main():
    print_board(main_board)
    app = QApplication(sys.argv)
    window = MainWindow(on_action, on_reset)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
