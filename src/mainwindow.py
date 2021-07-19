from typing import Callable
from PyQt5.QtWidgets import *
from cellbutton import CellButton


class MainWindow(QMainWindow):
    def __init__(self, on_cell_click: Callable[[int, int], any] = None, on_reset_click: Callable = None):
        super().__init__()

        self.setWindowTitle('EzSudoku')
        self.setFixedSize(250, 250)
        self.on_cell_click = on_cell_click
        self.on_reset_click = on_reset_click

        self._create_menu_bar()
        self._create_grid_view()
        self._center_on_screen()

    def _center_on_screen(self):
        center = QDesktopWidget().availableGeometry().center()
        rect = self.frameGeometry()
        rect.moveCenter(center)
        self.move(rect.topLeft())

    def _create_menu_bar(self):
        menu_bar = self.menuBar()

        reset_action = QAction('&Reset', self)
        # about_action = QAction('&About', self)

        reset_action.triggered.connect(self._menu_action)
        # about_action.triggered.connect(self._menu_action)

        menu_bar.addAction(reset_action)
        # menu_bar.addAction(about_action)

    def _create_grid_view(self):
        widget = QWidget(self)
        grid_layout = QGridLayout()
        widget.setLayout(grid_layout)
        self.setCentralWidget(widget)
        self.buttons = list([])
        button: QPushButton
        button_action: QAction
        for i in range(3):
            for j in range(3):
                button = CellButton(i, j, on_click=self.on_cell_click)
                self.buttons.append(button)
                grid_layout.addWidget(button, i, j)
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_label = QLabel("Game in progress...")
        self.status_bar.addPermanentWidget(self.status_label)

    def _menu_action(self, checked):
        action = self.sender().text()
        if action == "&Reset" and self.on_reset_click is not None:
            self.on_reset_click()
        elif action == "&About":
            print('about')

    def mark_cell(self, mark: str, x: int, y: int):
        pos = (x * 3) + y
        self.buttons[pos].setText(mark)

    def reset_board(self):
        for button in self.buttons:
            button.setText("")
