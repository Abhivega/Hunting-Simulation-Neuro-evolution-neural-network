from Hunted import Bird
from neurlnet import Neuralnet
from Hunter import Predator
from p5 import *
from copy import deepcopy
import numpy as np
global z
global bird
global pred
z=0

net = Neuralnet()


bird = [Bird() for i in range(2)]
pred = [Predator(net) for i in range(4)]

def setup():
    size(1270, 680)
    no_stroke()
    fill(255)


def alldead():
    if len(bird) == 0:
        for i, k in enumerate(pred):
            print("preditor " + str(i) + " killed :", k.kill)


def baby(pred):
        a = []

        for pre in pred:
            a.append(pre.mini)
        minim = min(a)
        i = a.index(min(a))
        one=deepcopy(pred[i])
        one.forone()
        net = deepcopy(pred[i].net)
        print(i)
        pred = [Predator(net) for i in range(4)]
        pred.append(one)
        return pred



def draw():
    global bird
    global pred
    global z
    z+=1
    background(255) 
    if z <  700:
    #    alldead()
        for bir in bird:
            bir.run(pred)
        for pre in pred:
            pre.run(bird)
            pre.movebitch(pred)
    else:
        z=0
        bird = [Bird() for i in range(2)]
        pred=baby(pred)






if __name__ == '__main__':
    run()
