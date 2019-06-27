import time
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


class NeurowebNode:
    def __init__(self, denseLayers, denseLayersNum):
        self.denseLayers = denseLayers
        self.denseLayersNum = denseLayersNum
        self.model = Sequential()
        self.children=[]
        self.time = 0

    def configweb(self, input_s, output_s):
        self.model.add(
            Dense(self.denseLayersNum[0], input_shape=(input_s,), activation='relu', kernel_initializer='random_normal'))

        for i in range(self.denseLayers-1):
            self.model.add(Dense(self.denseLayersNum[i+1], activation='relu', kernel_initializer='random_normal'))
        self.model.add(Dense(output_s, activation='sigmoid', kernel_initializer='random_normal'))
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return self.model

    def demotrain(self, sets, answers, epochs):
        s1 = len(sets)
        s2 = len(sets[0])
        s3 = len(answers[0])
        m = self.configweb(len(sets[0]), len(answers[0]))
        time_callback = TimeHistory()
        sets = numpy.array(sets)
        sets = sets.reshape(s1, s2)
        answers = numpy.array(answers)
        answers = answers.reshape(s1, s3)
        print(self)
        history = m.fit(sets, answers, epochs=epochs, batch_size=10, callbacks=[time_callback])
        self.time = time_callback.time
        loss = history.history['loss']
        loss = loss[len(loss)-1]
        return loss

    def createchildren(self):
        denseLN=self.denseLayersNum.copy()
        denseLN.append(1)

        self.children.append(
            NeurowebNode(self.denseLayers + 1, denseLN))



        denseLN = self.denseLayersNum.copy()
        denseLN[self.denseLayers-1] += 1
        self.children.append(
            NeurowebNode(self.denseLayers, denseLN))



    def __str__(self) -> str:
        st = ''
        st += str(self.denseLayers) + ' dense layers:'
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