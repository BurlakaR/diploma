import numpy
from PyQt5.QtWidgets import QTableWidgetItem

from ui import trainwin
from win import Win
from localBD.bdcontroller import BdController
from neurocreator import NeuroWebCreator
from dataprepare import DataPreparator
from PyQt5 import QtCore


class BaseTrain(Win, trainwin.Ui_Train):
    def __init__(self, mainwindow):
        super().__init__(mainwindow=mainwindow)

        self.bd = BdController()
        self.preparator = DataPreparator()
        self.neurocreator = NeuroWebCreator()

        if self.bd.data_exists():
            market, trends = self.bd.read_data()
            opts, num = self.preparator.forTrainWindow(market, trends)

            self.bd.save_options(opts, num)

            self.tableOptions.setColumnCount(1)
            self.tableOptions.setRowCount(len(opts))
            self.tableOptions.setHorizontalHeaderLabels(['Options'])
            self.tableOptions.setColumnWidth(0, 500)
            for i in range(len(opts)):
                for j in range(1):
                    chkBoxItem = QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    chkBoxItem.setText(opts[i])
                    self.tableOptions.setItem(i, j, chkBoxItem)
            self.tableOptions.itemClicked.connect(self.handleItemClicked)
            self.listChecked = []

        self.mistake.setMaximum(100)
        self.mistake.setValue(2.5)
        self.spinBox.setMaximum(300)
        self.spinBox.setValue(300)
        self.fastButton.clicked.connect(self.fast)
        self.doubleButton.clicked.connect(self.double)
        self.deepButton.clicked.connect(self.deep)
        self.fullButton.clicked.connect(self.full)

    def handleItemClicked(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            self.listChecked.append(item.text())
        else:
            try:
                self.listChecked.remove(item.text())
            except:
                pass

    def fast(self):
        self.train(0.25)

    def double(self):
        self.train(0.5)

    def deep(self):
        self.train(0.75)

    def full(self):
        self.train(1)

    def train(self, k):
        self.timesteps = 7
        time = self.spinBox.value()
        for item in self.listChecked:
            data = []
            sets = numpy.empty((0, self.timesteps, 1))
            answers = numpy.empty((0, self.timesteps, 1))
            d = self.bd.option_numeric_data(item)
            for _d in d:
                data.append(_d)
            for dataset in data:
                _sets, _answers = self.preparator.prepareForLSTM(dataset, self.timesteps)
                try:
                    sets = numpy.concatenate((sets, _sets))
                except:
                    sets = _sets
                try:
                    answers = numpy.concatenate((answers, _answers))
                except:
                    answers = _answers
            mistake = self.mistake.value()*sets.max()/100
            model = self.neurocreator.createWebLSTM(sets, answers, self.timesteps, k, mistake, time)
            self.bd.save_model(model, item)
        for_dense = []
        self.bd.updateOptionsModels(self.listChecked)
        for item in self.listChecked:
            if not self.bd.app_or_option(item):
                for_dense.append(item)

        sets, answers = self.preparator.prepareForDense(self.bd.read_market(), for_dense)
        model = self.neurocreator.createWebDense(sets, answers, k, 0.2, time)
        self.bd.save_model(model, "main")

        self.mainwindow.show()
        self.close()


