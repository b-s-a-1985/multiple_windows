# PySide6 Tutorial - QDialog, QMessageBox , Move to Second Window:
# https://youtu.be/KuOZAwXedjw?si=0KhbqW5Djpvg60H-
from PySide6.QtWidgets import *
from PySide6.QtCore import QSize


class CustomDialog(QDialog):
    """Second window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('This is the new dialog')
        self.setFixedSize(QSize(350, 150))
        self.buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.my_button = QDialogButtonBox(self.buttons)
        self.my_button.accepted.connect(self.accept)
        self.my_button.rejected.connect(self.reject)
        self.my_layout = QVBoxLayout()
        self.message = QLabel('This is a new dialog')
        self.message.setStyleSheet('font-size:30px;color:blue')
        self.my_layout.addWidget(self.message)
        self.my_layout.addWidget(self.my_button)
        self.setLayout(self.my_layout)

    def accept(self):
        print('You clicked on OK button')
        self.hide()     # collapse CustomDialog

    def reject(self):
        print('You clicked on Cancel button')
        self.hide()     # collapse CustomDialog


class MainWindow(QMainWindow):
    """First window"""
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 200))
        self.my_button = QPushButton('show dialog')
        self.my_button.clicked.connect(self.open_dialog)
        self.setCentralWidget(self.my_button)

    def open_dialog(self):
        dialog = CustomDialog()
        dialog.exec()


def main():
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
