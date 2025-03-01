import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QLabel,)
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 40px;')
    window.addWidgetToVLayout(label1)
    window.adjustfixedsize()
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    window.adjustfixedsize()

    window.show()
    app.exec()
