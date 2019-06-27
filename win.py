from PyQt5 import QtWidgets

class Win(QtWidgets.QDialog):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow=mainwindow
        self.setupUi(self)
        self.show()

    def closeEvent(self, QCloseEvent):
        self.mainwindow.show()
        self.destroy()