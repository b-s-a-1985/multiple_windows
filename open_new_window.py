from PySide6.QtWidgets import *
from PySide6.QtCore import QSize


class NewWindow(QWidget):
    """Second window"""
    def __init__(self):
        super().__init__()
        self.label = QLabel('This is a new window')
        self.setFixedSize(300, 100)
        self.close_button = QPushButton('Close this window')
        self.close_button.clicked.connect(self.close_window)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.close_button)
        self.setLayout(self.v_layout)

    def close_window(self):
        self.hide()     # destroy this window


class MyWindow(QMainWindow):
    """First window"""
    new_window = ''

    def __init__(self):
        super().__init__()
        self.setWindowTitle('This is the first window')
        self.setFixedSize(QSize(350, 150))
        self.my_button = QPushButton('Open new window')
        self.my_button.clicked.connect(self.open_new_window)
        self.setCentralWidget(self.my_button)

    def open_new_window(self):
        self.new_window = NewWindow()
        self.new_window.show()


def main():
    app = QApplication()
    ui = MyWindow()
    ui.show()
    app.exec()


if __name__ == '__main__':
    main()

