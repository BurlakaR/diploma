from collect.bridge import Bridge


class Broker:
    def __init__(self):
        self.bridge = Bridge()
        self.queueRequest = 'Request'
        self.queueData = 'Data'
        self.host = 'amqp://vgglftoj:ql5_URu2IzU2V03EpjTPq8gukdFeu241@raven.rmq.cloudamqp.com/vgglftoj'

    def sendRequest(self, request):
        self.bridge.send(self.queueRequest, request, self.host)

    def receiveData(self):
        mes = self.bridge.receive(self.queueData, self.host)
        return mes
