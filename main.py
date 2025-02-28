import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QLabel,)

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 40px;')
    window.v_layout.addWidget(label1)
    window.adjustfixedsize()

    window.show()
    app.exec()
