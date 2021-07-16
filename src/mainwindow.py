from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, ):
        super().__init__()

        self.setWindowTitle('EzSudoku')
        self.setFixedSize(520, 400)

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
        about_action = QAction('&About', self)

        reset_action.triggered.connect(self._menu_action)
        about_action.triggered.connect(self._menu_action)

        menu_bar.addAction(reset_action)
        menu_bar.addAction(about_action)

    def _create_grid_view(self):
        widget = QWidget(self)
        grid_layout = QGridLayout()
        widget.setLayout(grid_layout)
        self.setCentralWidget(widget)

        button: QPushButton
        for i in range(3):
            for j in range(3):
                button = QPushButton(str(3 * i + j))
                grid_layout.addWidget(button, i, j)

    def _menu_action(self, checked):
        action = self.sender().text()
        if action == "&Reset":
            print('reset')
        elif action == "&About":
            print('about')

    def _button_action(self):
        print('test')
