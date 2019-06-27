# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/prognosticwin.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Prognosis(object):
    def setupUi(self, Prognosis):
        Prognosis.setObjectName("Prognosis")
        Prognosis.resize(679, 516)
        Prognosis.setStyleSheet("QWidget {background: white}\n"
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
"background: #82c8a0;\n"
"}\n"
"QLabel{\n"
"color:#82c8a0;\n"
"}\n"
"[accessibleName=\"prognoseButton\"]:hover{\n"
"    text-decoration: none;\n"
"    color: #fff;\n"
"  }\n"
"[accessibleName=\"prognoseButton\"]:pressed{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 12pt;\n"
"min-width: 8em;\n"
"padding: 0px\n"
"}\n"
"")
        self.prognostic = QtWidgets.QPushButton(Prognosis)
        self.prognostic.setGeometry(QtCore.QRect(60, 30, 560, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.prognostic.setFont(font)
        self.prognostic.setObjectName("prognostic")
        self.prognoseButton = QtWidgets.QPushButton(Prognosis)
        self.prognoseButton.setGeometry(QtCore.QRect(60, 460, 560, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.prognoseButton.setFont(font)
        self.prognoseButton.setObjectName("prognoseButton")
        self.tableApps = QtWidgets.QTableWidget(Prognosis)
        self.tableApps.setGeometry(QtCore.QRect(60, 100, 261, 341))
        self.tableApps.setObjectName("tableApps")
        self.tableApps.setColumnCount(0)
        self.tableApps.setRowCount(0)
        self.tableOptions = QtWidgets.QTableWidget(Prognosis)
        self.tableOptions.setGeometry(QtCore.QRect(360, 100, 261, 341))
        self.tableOptions.setObjectName("tableOptions")
        self.tableOptions.setColumnCount(0)
        self.tableOptions.setRowCount(0)

        self.retranslateUi(Prognosis)
        QtCore.QMetaObject.connectSlotsByName(Prognosis)

    def retranslateUi(self, Prognosis):
        _translate = QtCore.QCoreApplication.translate
        Prognosis.setWindowTitle(_translate("Prognosis", "Prognosis"))
        self.prognostic.setAccessibleName(_translate("Prognosis", "prognostic"))
        self.prognostic.setText(_translate("Prognosis", "Виконання прогнозу"))
        self.prognoseButton.setAccessibleName(_translate("Prognosis", "prognoseButton"))
        self.prognoseButton.setText(_translate("Prognosis", "Виконання прогнозу"))


