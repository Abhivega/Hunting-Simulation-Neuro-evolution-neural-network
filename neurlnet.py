import numpy as np


class Neuralnet(object):

    def __init__(self):
        self.w1 = np.random.uniform(low=-1,high=1,size=(3, 10))


        self.w2 = np.random.uniform(low=-1,high=1,size=(10, 10))


        self.w3 = np.random.uniform(low=-1, high=1, size=(10, 2))


        self.inp = np.ones((3,))
        self.layer1 = np.ones((10,))
        self.layer2 = np.ones((10,))
        self.out = np.ones((2,))

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def compute(self, inpu):
        self.inp = inpu

        for i in range(len(self.layer1)):
            temp = 0
            for j in range(len(self.inp)):
                temp += np.multiply(self.inp[j], self.w1[j, i])
            #temp+=self.b1[0]
            self.layer1[i] = temp
        for i in range(len(self.layer2)):
            temp = 0
            for j in range(len(self.layer1)):
                temp += np.multiply(self.layer1[j], self.w2[j, i])
            #temp+=self.b1[0]
            self.layer2[i] = temp

        for i in range(len(self.out)):
            temp = 0
            for j in range(len(self.layer2)):
                temp += np.multiply(self.layer2[j], self.w3[j, i])
            #temp += self.b2[0]
            self.out[i] = temp
        temp=np.copy(self.out)
        return(temp)

    def mutate(self):
        for i in range(3):
            for j in range(10):
                if np.random.rand() < 0.05:
                    self.w1[i,j]=np.random.uniform(low=-1,high=1)

        for i in range(10):
            for j in range(10):
                if np.random.rand() < 0.05:
                    self.w2[i, j] = np.random.uniform(low=-1, high=1)
                    
        for i in range(10):
            for j in range(2):
                if np.random.rand() < 0.05:
                    self.w3[i, j] = np.random.uniform(low=-1, high=1)


