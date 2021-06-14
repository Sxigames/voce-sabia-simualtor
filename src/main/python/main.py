from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSystemTrayIcon
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor, QIcon
import sys
import pypresence
appctxt = ApplicationContext()


presence = pypresence.Presence("816430658020311091")



class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        tray = QSystemTrayIcon()
        icone = QIcon(appctxt.get_resource("molo.png"))
        tray.setIcon(icone)
        tray.activated.connect(lambda: self.show())
        tray.activated.connect(lambda: tray.hide())
        uic.loadUi(appctxt.get_resource("telaprincipal.ui"), self)
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setColor(QColor(0, 0, 0, 60))
        sombra.setXOffset(0)
        sombra.setYOffset(0)
        sombra.setBlurRadius(20)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGraphicsEffect(sombra)
        self.setWindowTitle("Você Sabia Simulator")
        self.Selecionar.setEnabled(False)
        self.Fechar.clicked.connect(lambda: self.close())
        self.Minimizar.clicked.connect(lambda: tray.show())
        self.Minimizar.clicked.connect(lambda: tray.showMessage("Minimzado", "minimazdo para a gaveta"))
        self.Minimizar.clicked.connect(lambda: self.hide())
        self.show()



    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    presence.connect()
    presence.update(state="Puxando a vinheta", large_image='danielmolo', large_text="Daniel Molo",
                    small_image='lucasmarques', small_text='Lucas Marques',
                    buttons=[{"label": "Puxar A vinheta", "url": "https://youtu.be/ZOflhzJGNIM/"},
                             {"label": "Esperar", "url": "https://youtu.be/wbSLqaRzKW0"}])
    ex = Janela()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)

