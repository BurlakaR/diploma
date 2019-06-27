import time

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


class NeurowebNodeLSTM:
    def __init__(self, lstmLayers, lstmLayersNum, denseLayers, denseLayersNum, timesteps):
        self.lstmLayers = lstmLayers
        self.lstmLayersNum = lstmLayersNum
        self.denseLayers = denseLayers
        self.denseLayersNum = denseLayersNum
        self.timesteps = timesteps
        self.model = Sequential()
        self.children=[]
        self.time = 0

    def configweb(self):
        self.model.add(
            LSTM(self.lstmLayersNum[0], input_shape=(self.timesteps, 1), return_sequences=True))
        for i in range(self.lstmLayers-1):
            self.model.add(LSTM(self.lstmLayersNum[i + 1], return_sequences=True))
        for i in range(self.denseLayers):
            self.model.add(Dense(self.denseLayersNum[i]))
        self.model.add(Dense(1))
        self.model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['accuracy'])
        return self.model

    def demotrain(self, sets, answers, epochs):
        m = self.configweb()
        time_callback = TimeHistory()
        print(self)
        history = m.fit(sets, answers, epochs=epochs, callbacks=[time_callback])
        self.time = time_callback.time
        loss = history.history['loss']
        loss = loss[len(loss)-1]
        return loss

    def createchildren(self):
        lstmLN = self.lstmLayersNum.copy()
        lstmLN.insert(0, 1)
        denseLN=self.denseLayersNum.copy()
        denseLN.append(1)

        self.children.append(NeurowebNodeLSTM(self.lstmLayers + 1, lstmLN, self.denseLayers, self.denseLayersNum, self.timesteps))
        self.children.append(
            NeurowebNodeLSTM(self.lstmLayers, self.lstmLayersNum, self.denseLayers + 1, denseLN, self.timesteps))

        lstmLN = self.lstmLayersNum.copy()
        lstmLN[self.lstmLayers-1]+=1
        self.children.append(
            NeurowebNodeLSTM(self.lstmLayers, lstmLN, self.denseLayers, self.denseLayersNum, self.timesteps))

        denseLN = self.denseLayersNum.copy()
        denseLN[0] += 1
        self.children.append(
            NeurowebNodeLSTM(self.lstmLayers, self.lstmLayersNum, self.denseLayers, denseLN, self.timesteps))



    def __str__(self) -> str:
        st = ''
        st+= str(self.lstmLayers) + ' lstm layers:'
        for i in self.lstmLayersNum:
            st+=str(i)+'-'
        st += '| '+str(self.denseLayers) + ' dense layers:'
        for i in self.denseLayersNum:
            st+=str(i)+'-'
        return st

class TimeHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.time = time.time()

    def on_epoch_begin(self, batch, logs={}):
        self.epoch_time_start = time.time()

    def on_train_end(self, logs={}):
        self.time = time.time() - self.time