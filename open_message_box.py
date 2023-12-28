from PySide6.QtWidgets import *
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    """Basic window"""
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 200))
        self.my_button = QPushButton('show messagebox')
        self.my_button.clicked.connect(self.open_messagebox)
        self.msgbox = QMessageBox(self)
        self.msgbox.setWindowTitle('Hi, I am a messagebox')
        self.msgbox.setText('Hello from messagebox')
        # QMessageBox.Question | QMessageBox.Warning | QMessageBox.Critical
        self.msgbox.setIcon(QMessageBox.Critical)
        self.my_button.clicked.connect(self.open_messagebox)
        self.setCentralWidget(self.my_button)

    def open_messagebox(self):
        self.msgbox.exec()


def main():
    app = QApplication()
    ui = MainWindow()
    ui.show()
    app.exec()


if __name__ == '__main__':
    main()












# QMessageBox.Warning
# QMessageBox.Critical
# QMessageBox.Question