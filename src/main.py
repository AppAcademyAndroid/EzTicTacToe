import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow

app: QApplication
window: MainWindow
main_board = [[0] * 3 for _ in range(3)]


# -1 = game in progress
# 0 = tie
# 1 = X won
# 2 = Y won
def game_status(board: [[]]) -> int:
    for i in range(3):
        if board[i][0] == 0:
            continue
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
    for i in range(3):
        if board[0][i] == 0:
            continue
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]
    mid = board[1][1]
    if mid != 0 and ((mid == board[0][0] and mid == board[2][2]) or (mid == board[0][2] and mid == board[2][0])):
        return board[1][1]
    return 0


def print_board(board: [[]]):
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(board[i][j])
            else:
                print(f"{board[i][j]} ", end="")


def on_action(x: int, y: int):
    global main_board

    print(f"click on cell ({x}, {y})")

    if main_board[x][y] == 0:
        main_board[x][y] = 1
        window.mark_cell('X', x, y)
    else:
        print("cell already marked")


def on_reset():
    print_board(main_board)
    print("reset")
    window.reset_board()
    for i in range(3):
        for j in range(3):
            main_board[i][j] = 0


def main():
    global app
    global window

    app = QApplication(sys.argv)
    window = MainWindow(on_action, on_reset)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
