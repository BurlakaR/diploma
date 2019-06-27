from collect.broker import Broker

class DataCollector:
    def __init__(self):
        self.broker = Broker()

    def update(self, date1, date2):
        request = date1.toString('yyyy-MM-dd')+'T00:00;'+date2.toString('yyyy-MM-dd')+'T00:00'
        self.broker.sendRequest(request=request)
        data=self.broker.receiveData()
        return data[0], data[1]