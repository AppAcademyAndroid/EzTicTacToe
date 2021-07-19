from typing import Callable
from PyQt5.QtWidgets import QPushButton


class CellButton(QPushButton):
    def __init__(self, x: int, y: int, text: str = "", on_click: Callable[[int, int], any] = None):
        super().__init__()
        self.setText(text)
        self.setFixedSize(50, 50)
        self.cell_pos = (x, y)
        self.on_click = on_click
        if on_click is not None:
            self.clicked.connect(self._on_cell_action)

    def _on_cell_action(self):
        self.on_click(self.cell_pos[0], self.cell_pos[1])

