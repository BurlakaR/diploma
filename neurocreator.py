from neuronetNodeLSTM import NeurowebNodeLSTM
from neuronetNode import NeurowebNode


class NeuroWebCreator():
    def createWebLSTM(self, sets, answers, timesteps, k, mistake, time):
        self.k = k
        self.mis = mistake
        print(mistake)
        self.t = time

        self.topOfNeuro = []

        lstm = [1]
        dense = [1]
        self.topOfNeuro.append([0, NeurowebNodeLSTM(1, lstm, 1, dense, timesteps)])
        self.topOfNeuro[0][1].demotrain(sets, answers, int(30000 / len(sets)))
        return self.nextlevel(sets, answers)

    def createWebDense(self, sets, answers, k, mistake, time):
        self.k = k
        self.mis = mistake
        print(mistake)
        self.t = time

        self.topOfNeuro = []

        dense = [1]
        self.topOfNeuro.append([0, NeurowebNode(1, dense)])
        self.topOfNeuro[0][1].demotrain(sets, answers, int(30000 / len(sets)))
        return self.nextlevel(sets, answers)

    def nextlevel(self, sets, answers):
        topOfN = []
        for node in self.topOfNeuro:
            if node[1].time < self.t:
                node[1].createchildren()
                for child in node[1].children:
                    topOfN.append([child.demotrain(sets, answers, int(30000 / len(sets))), child])
        self.topOfNeuro = topOfN
        if len(self.topOfNeuro) < 1:
            return 0
        self.topOfNeuro.sort()
        num = int(len(self.topOfNeuro) * self.k)
        if num < 1:
            num = 1
        self.topOfNeuro = self.topOfNeuro[0:num]
        if self.topOfNeuro[0][0] > self.mis:
            return self.nextlevel(sets, answers)
        else:
            print(self.topOfNeuro[0][1])
            return self.topOfNeuro[0][1].model
