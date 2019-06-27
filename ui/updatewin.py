# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/updatewin.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Update(object):
    def setupUi(self, Update):
        Update.setObjectName("Update")
        Update.resize(854, 741)
        Update.setStyleSheet("QWidget {background: white}\n"
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
" background: #fa5a5a;\n"
"}\n"
"[accessibleName=\"updateButton\"]{\n"
"     border-radius: 85%;\n"
"  }\n"
"[accessibleName=\"updateButton\"]:hover{\n"
"    text-decoration: none;\n"
"    color: #fff;\n"
"  }\n"
"[accessibleName=\"updateButton\"]:pressed{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 85%;\n"
"border-color: beige;\n"
"font: 12pt;\n"
"min-width: 8em;\n"
"padding: 0px\n"
"}\n"
"\n"
"QLabel{\n"
"color:#fa5a5a;\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QToolButton {\n"
"      \n"
"      color: white;\n"
"      font-size: 12px;\n"
"      background-color:#fa5a5a;\n"
"  }\n"
"  QCalendarWidget QMenu {\n"
"      \n"
"      color: white;\n"
"      font-size: 12px;\n"
"      background-color: rgb(100, 100, 100);\n"
"border:1px solid black;\n"
"  }\n"
"  QCalendarWidget QSpinBox { \n"
"\n"
"      font-size:12px; \n"
"      color: white; \n"
"      background-color:#fa5a5a;\n"
"      selection-background-color: rgb(136, 136, 136);\n"
"      selection-color: rgb(255, 255, 255);\n"
"  }\n"
"  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:30px; }\n"
"  QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:30px;}\n"
"   \n"
"  /* header row */\n"
"  QCalendarWidget QWidget { alternate-background-color: rgb(255, 255, 255); }\n"
"   \n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"      font-size:12px;  \n"
"      color: rgb(180, 180, 180);  \n"
"      background-color: black;  \n"
"      selection-background-color: rgb(64, 64, 64); \n"
"      selection-color: rgb(0, 255, 0); \n"
"  }\n"
"   \n"
"  /* days in other months */\n"
"  /* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"background-color: #fa5a5a; \n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(64, 64, 64); \n"
"}")
        self.newData = QtWidgets.QPushButton(Update)
        self.newData.setGeometry(QtCore.QRect(50, 20, 751, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.newData.setFont(font)
        self.newData.setObjectName("newData")
        self.updateButton = QtWidgets.QPushButton(Update)
        self.updateButton.setGeometry(QtCore.QRect(600, 540, 171, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.updateButton.setFont(font)
        self.updateButton.setAutoRepeatDelay(300)
        self.updateButton.setObjectName("updateButton")
        self.calendarStart = QtWidgets.QCalendarWidget(Update)
        self.calendarStart.setGeometry(QtCore.QRect(550, 140, 251, 161))
        self.calendarStart.setObjectName("calendarStart")
        self.label = QtWidgets.QLabel(Update)
        self.label.setGeometry(QtCore.QRect(610, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Update)
        self.label_2.setGeometry(QtCore.QRect(620, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.openGLWidget = QtWidgets.QOpenGLWidget(Update)
        self.openGLWidget.setGeometry(QtCore.QRect(549, 139, 253, 164))
        self.openGLWidget.setObjectName("openGLWidget")
        self.calendarFinish = QtWidgets.QCalendarWidget(Update)
        self.calendarFinish.setGeometry(QtCore.QRect(551, 351, 251, 161))
        self.calendarFinish.setObjectName("calendarFinish")
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(Update)
        self.openGLWidget_2.setGeometry(QtCore.QRect(550, 350, 253, 164))
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.tableApps = QtWidgets.QTableWidget(Update)
        self.tableApps.setGeometry(QtCore.QRect(50, 100, 471, 611))
        self.tableApps.setObjectName("tableApps")
        self.tableApps.setColumnCount(0)
        self.tableApps.setRowCount(0)
        self.openGLWidget_2.raise_()
        self.openGLWidget.raise_()
        self.newData.raise_()
        self.updateButton.raise_()
        self.calendarStart.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.calendarFinish.raise_()
        self.tableApps.raise_()

        self.retranslateUi(Update)
        QtCore.QMetaObject.connectSlotsByName(Update)

    def retranslateUi(self, Update):
        _translate = QtCore.QCoreApplication.translate
        Update.setWindowTitle(_translate("Update", "Data updating"))
        self.newData.setAccessibleName(_translate("Update", "newData"))
        self.newData.setText(_translate("Update", "Оновлення даних"))
        self.updateButton.setAccessibleName(_translate("Update", "updateButton"))
        self.updateButton.setText(_translate("Update", "ОНОВИТИ"))
        self.label.setText(_translate("Update", "Початкова дата"))
        self.label_2.setText(_translate("Update", "Кінцева дата"))


