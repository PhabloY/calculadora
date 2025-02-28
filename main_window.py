from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget,
                               QVBoxLayout, QLabel,)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        # Configurando o layout básico
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle('Calculadora')

    def adjustfixedsize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def multiplication(self, valor, multiplicador):
        self.valor = valor
        self.multiplicador = multiplicador
        multiplicacao = self.valor * self.multiplicador
        return multiplicacao
