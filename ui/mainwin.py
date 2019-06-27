# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget {background: white}\n"
"QVBoxLayout{border: 1px; border-color: black}\n"
"QPushButton{\n"
"font-size: 16pt;\n"
"display: inline-block;\n"
"  margin-bottom: 0;\n"
"  text-align: center;\n"
"  text-transform: uppercase;\n"
"  vertical-align: middle;\n"
"  cursor: pointer;\n"
"  background-image: none;\n"
"  whitespace: nowrap;\n"
"  padding: 6px 12px;\n"
"  font-size: 1.4rem;\n"
"  border-radius: 3px;\n"
"  border: 1px solid transparent;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: none;\n"
"    color: #fff;\n"
"  }\n"
"QPushButton:pressed{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 12pt;\n"
"min-width: 8em;\n"
"padding: 0px\n"
"}\n"
"[accessibleName=\"newData\"] {\n"
"    background: #fa5a5a;\n"
"}\n"
"[accessibleName=\"training\"] {\n"
"    background: #f0d264;\n"
"}\n"
"[accessibleName=\"prognostic\"] {\n"
"    background: #82c8a0;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newData = QtWidgets.QPushButton(self.centralwidget)
        self.newData.setGeometry(QtCore.QRect(120, 180, 560, 50))
        self.newData.setObjectName("newData")
        self.training = QtWidgets.QPushButton(self.centralwidget)
        self.training.setGeometry(QtCore.QRect(120, 280, 560, 50))
        self.training.setObjectName("training")
        self.prognostic = QtWidgets.QPushButton(self.centralwidget)
        self.prognostic.setGeometry(QtCore.QRect(120, 380, 560, 50))
        self.prognostic.setObjectName("prognostic")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BASE"))
        self.newData.setAccessibleName(_translate("MainWindow", "newData"))
        self.newData.setText(_translate("MainWindow", "Оновлення даних"))
        self.training.setAccessibleName(_translate("MainWindow", "training"))
        self.training.setText(_translate("MainWindow", "Тренування мережі"))
        self.prognostic.setAccessibleName(_translate("MainWindow", "prognostic"))
        self.prognostic.setText(_translate("MainWindow", "Виконання прогнозу"))


