from ui import updatewin
from win import Win
from collect.datacollector import DataCollector
from localBD.bdcontroller import BdController
from dataprepare import DataPreparator
import PyQt5.QtWidgets as QtGui


class BaseUpdate(Win, updatewin.Ui_Update):
    def __init__(self, mainwindow):
        super().__init__(mainwindow=mainwindow)
        self.updateButton.clicked.connect(self.update)
        self.bdcontroller = BdController()
        self.datapreparator = DataPreparator()

        if self.bdcontroller.data_exists():
            market, trends = self.bdcontroller.read_data()
            df = self.datapreparator.forUpdateWindow(market)

            self.tableApps.setColumnCount(len(df.columns))
            self.tableApps.setRowCount(len(df.index))
            self.tableApps.setHorizontalHeaderLabels(df.columns)
            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    self.tableApps.setItem(i, j, QtGui.QTableWidgetItem(str(df.iloc[i, j])))

    def update(self):
        datacollector = DataCollector()
        market, trends = datacollector.update(self.calendarStart.selectedDate(), self.calendarFinish.selectedDate())
        self.bdcontroller.save(market, trends)
        self.mainwindow.show()
        self.close()
