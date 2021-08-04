import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow

app: QApplication
window: MainWindow
main_board = [[0] * 3 for _ in range(3)]


# Not played = 0
# Player X = 1
# Player O = 2
def evaluate_board(board: [[]], player: int) -> int:
    for i in range(3):
        first_cell = board[i][0]
        if first_cell != 0 and first_cell == board[i][1] and first_cell == board[i][2]:
            return 10 if first_cell == player else -10

    for i in range(3):
        first_cell = board[0][i]
        if first_cell != 0 and first_cell == board[1][i] and first_cell == board[2][i]:
            return 10 if first_cell == player else -10

    middle_cell = board[1][1]
    if middle_cell != 0 and ((middle_cell == board[0][0] and middle_cell == board[2][2]) or (middle_cell == board[0][2] and middle_cell == board[2][0])):
        return 10 if middle_cell == player else -10

    return 0


def has_moves_left(board: [[]]) -> bool:
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return True
    return False


def print_board(board: [[]]):
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(board[i][j])
            else:
                print(f"{board[i][j]} ", end="")


def min_max(board: [[]], depth: int, is_max: bool) -> int:
    player = 1 if is_max else 2
    score = evaluate_board(board, player)

    if score != 0:
        return score

    best_score = -1000 if is_max else 1000
    min_max_result: int

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = player
                min_max_result = min_max(board, depth + 1, not is_max)
                best_score = max(best_score, min_max_result) if is_max else min(best_score, min_max_result)
                board[i][j] = 0

    return best_score


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
