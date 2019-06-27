# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/trainwin.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Train(object):
    def setupUi(self, Train):
        Train.setObjectName("Train")
        Train.resize(728, 498)
        Train.setStyleSheet("QWidget {background: white}\n"
"QVBoxLayout{border: 1px; border-color: black}\n"
"QPushButton{\n"
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
" background: #f0d264;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:#f0d264;\n"
"}")
        self.training = QtWidgets.QPushButton(Train)
        self.training.setGeometry(QtCore.QRect(80, 30, 560, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.training.setFont(font)
        self.training.setObjectName("training")
        self.label = QtWidgets.QLabel(Train)
        self.label.setGeometry(QtCore.QRect(130, 330, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.mistake = QtWidgets.QDoubleSpinBox(Train)
        self.mistake.setGeometry(QtCore.QRect(230, 330, 62, 22))
        self.mistake.setObjectName("mistake")
        self.label_2 = QtWidgets.QLabel(Train)
        self.label_2.setGeometry(QtCore.QRect(390, 330, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Train)
        self.label_3.setGeometry(QtCore.QRect(300, 330, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(Train)
        self.spinBox.setGeometry(QtCore.QRect(530, 330, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(Train)
        self.label_4.setGeometry(QtCore.QRect(580, 330, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.fullButton = QtWidgets.QPushButton(Train)
        self.fullButton.setGeometry(QtCore.QRect(540, 380, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.fullButton.setFont(font)
        self.fullButton.setStyleSheet("QPushButton{\n"
"     border-radius: 50%;\n"
"font-size:15px;\n"
"color:black;\n"
"  }\n"
":hover{\n"
"    text-decoration: none;\n"
"    color: #fff;\n"
"  }\n"
":pressed{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"font: 12pt;\n"
"padding: 0px\n"
"}")
        self.fullButton.setAutoRepeatDelay(300)
        self.fullButton.setObjectName("fullButton")
        self.deepButton = QtWidgets.QPushButton(Train)
        self.deepButton.setGeometry(QtCore.QRect(390, 380, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.deepButton.setFont(font)
        self.deepButton.setStyleSheet("QPushButton{\n"
"     border-radius: 50%;\n"
"font-size:15px;\n"
"color:black;\n"
"  }\n"
":hover{\n"
"    text-decoration: none;\n"
"    color: #fff;\n"
"  }\n"
":pressed{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"font: 12pt;\n"
"padding: 0px\n"
"}")
        self.deepButton.setAutoRepeatDelay(300)
        self.deepButton.setObjectName("deepButton")
        self.fastButton = QtWidgets.QPushButton(Train)
        self.fastButton.setGeometry(QtCore.QRect(80, 380, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.fastButton.setFont(font)
        self.fastButton.setStyleSheet("QPushButton{\n"
"     border-radius: 50%;\n"
"font-size:15px;\n"
"color:black;\n"
"  }\n"
":hover{\n"
"    text-decoration: none;\n"
"    color: #fff;\n"
"  }\n"
":pressed{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"font: 12pt;\n"
"padding: 0px\n"
"}")
        self.fastButton.setAutoRepeatDelay(300)
        self.fastButton.setObjectName("fastButton")
        self.doubleButton = QtWidgets.QPushButton(Train)
        self.doubleButton.setGeometry(QtCore.QRect(230, 380, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.doubleButton.setFont(font)
        self.doubleButton.setStyleSheet("QPushButton{\n"
"     border-radius: 50%;\n"
"font-size:15px;\n"
"color:black;\n"
"  }\n"
":hover{\n"
"    text-decoration: none;\n"
"    color: #fff;\n"
"  }\n"
":pressed{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: beige;\n"
"font: 12pt;\n"
"padding: 0px\n"
"}")
        self.doubleButton.setAutoRepeatDelay(300)
        self.doubleButton.setObjectName("doubleButton")
        self.tableOptions = QtWidgets.QTableWidget(Train)
        self.tableOptions.setGeometry(QtCore.QRect(80, 90, 561, 221))
        self.tableOptions.setObjectName("tableOptions")
        self.tableOptions.setColumnCount(0)
        self.tableOptions.setRowCount(0)

        self.retranslateUi(Train)
        QtCore.QMetaObject.connectSlotsByName(Train)

    def retranslateUi(self, Train):
        _translate = QtCore.QCoreApplication.translate
        Train.setWindowTitle(_translate("Train", "Train"))
        self.training.setAccessibleName(_translate("Train", "training"))
        self.training.setText(_translate("Train", "Тренування мережі"))
        self.label.setText(_translate("Train", "Похибка:"))
        self.label_2.setText(_translate("Train", "Час на спробу:"))
        self.label_3.setText(_translate("Train", "%"))
        self.label_4.setText(_translate("Train", "c"))
        self.fullButton.setAccessibleName(_translate("Train", "fullButton"))
        self.fullButton.setText(_translate("Train", "Повне"))
        self.deepButton.setAccessibleName(_translate("Train", "deepButton"))
        self.deepButton.setText(_translate("Train", "Глибоке"))
        self.fastButton.setAccessibleName(_translate("Train", "fastButton"))
        self.fastButton.setText(_translate("Train", "Швидке"))
        self.doubleButton.setAccessibleName(_translate("Train", "doubleButton"))
        self.doubleButton.setText(_translate("Train", "Подвійне"))


