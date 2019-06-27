import sys
from PyQt5 import QtWidgets
from ui import mainwin
from updatecontroller import BaseUpdate
from traincontroller import BaseTrain
from prognosticcontroller import BasePrognose

class BaseApp(QtWidgets.QMainWindow, mainwin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newData.clicked.connect(self.newData_clicked)
        self.training.clicked.connect(self.training_clicked)
        self.prognostic.clicked.connect(self.predict_clicked)

    def newData_clicked(self):
        global win
        win = BaseUpdate(self)
        self.hide()

    def training_clicked(self):
        global win
        win = BaseTrain(self)
        self.hide()

    def predict_clicked(self):
        global win
        win = BasePrognose(self)
        self.hide()

    def closeEvent(self, QCloseEvent):
        self.destroy()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BaseApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()