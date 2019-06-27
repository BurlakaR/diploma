import numpy
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QRadioButton, QButtonGroup

import pyqtgraph as pg
from ui import prognosticwin
from win import Win
from localBD.bdcontroller import BdController
from dataprepare import DataPreparator
from PyQt5 import QtCore


class BasePrognose(Win, prognosticwin.Ui_Prognosis):
    def __init__(self, mainwindow):
        super().__init__(mainwindow=mainwindow)
        self.db = BdController()
        self.preparator = DataPreparator()

        self.listOptions = []
        self.listApps = []

        apps, options = self.preparator.forPrognosticWindow(self.db.read_market(), self.db.read_options())

        self.tableApps.setColumnCount(1)
        self.tableApps.setRowCount(len(apps))
        self.tableApps.setHorizontalHeaderLabels(['Applications'])
        self.tableApps.setColumnWidth(0, 250)
        for i in range(len(apps)):
            for j in range(1):
                chkBoxItem = QTableWidgetItem()
                chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                chkBoxItem.setText(apps[i])
                self.tableApps.setItem(i, j, chkBoxItem)
        self.tableApps.itemClicked.connect(self.handleItemClickedApps)

        self.tableOptions.setColumnCount(1)
        self.tableOptions.setRowCount(len(options))
        self.tableOptions.setHorizontalHeaderLabels(['Options'])
        self.tableOptions.setColumnWidth(0, 250)
        for i in range(len(options)):
            for j in range(1):
                chkBoxItem = QTableWidgetItem()
                chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                chkBoxItem.setText(options[i])
                self.tableOptions.setItem(i, j, chkBoxItem)
        self.tableOptions.itemClicked.connect(self.handleItemClickedOptions)

        self.prognoseButton.clicked.connect(self.make_prognose)

    def make_prognose(self):
        timesteps = 7
        data = self.db.read_market()

        for app in self.listApps:
            mainset = []
            for opt in self.listOptions:
                set = self.preparator.prepare_prognose(data, app, opt, timesteps)
                set = numpy.array(set)
                set = set.reshape(1, timesteps, 1)
                y = []
                x = []

                model = self.db.read_model(opt)
                for i in range(100):
                    set = model.predict(set)
                    x.append(i)
                    y.append(set[0][len(set)-1][0])
                mainset.append(y)

                pg.setConfigOption('background', 'w')
                pg.setConfigOption('foreground', 'k')
                pw = pg.plot(x, y, pen='g')

            model = self.db.read_model('main')
            ms = []
            for i in range(len(mainset[0])):
                mms = []
                for j in range(len(mainset)):
                    mms.append(mainset[j][i])
                ms.append(mms)
            s1 = len(ms)
            s2 = len(ms[0])
            ms = numpy.array(ms)
            ms = ms.reshape(s1, s2)
            y = model.predict(ms)
            yp = []
            for y1 in y:
                yp.append(self.preparator.transform_y_dense(y1))
            x = range(0, len(yp))
            pg.setConfigOption('background', 'w')
            pg.setConfigOption('foreground', 'k')
            pw = pg.plot(x, yp, pen='g')
            print(yp[0])




    def handleItemClickedOptions(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            self.listOptions.append(item.text())
        else:
            try:
                self.listOptions.remove(item.text())
            except:
                pass

    def handleItemClickedApps(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            self.listApps.append(item.text())
        else:
            try:
                self.listApps.remove(item.text())
            except:
                pass