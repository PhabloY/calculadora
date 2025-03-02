import sys
from PySide6.QtWidgets import (QApplication)
from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH


if __name__ == '__main__':
    # cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    window.addToVLayout(display)

    # executa tudo
    window.adjustfixedsize()
    window.show()
    app.exec()
