from Hunted import Bird
from neurlnet import Neuralnet
from Hunter import Predator
from p5 import *
from copy import deepcopy
import numpy as np
global z
global bird
global pred
global nodead
nodead = True
z=0

net = Neuralnet()


bird = [Bird() for i in range(2)]
pred = [Predator(net) for i in range(4)]

def setup():
    size(1270, 680)
    no_stroke()
    fill(255)


def alldead():
    global nodead
    if len(bird) == 0:
        nodead = False
        for i, k in enumerate(pred):
            print("preditor " + str(i) + " killed :", k.kill)


def baby(pred):
        a = []

        for pre in pred:
            a.append(pre.rank())
        minim = min(a)
        print(a)
        i = a.index(min(a))
        one=deepcopy(pred[i])
        one.forone()
        net = deepcopy(pred[i].net)
        print(i)
        pred = [Predator(net) for i in range(4)]
        pred.append(one)
        return pred



def draw():
    global nodead
    nodead = True
    global bird
    global pred
    global z
    z+=1
    alldead()
    background(255) 
    if z <  700 and nodead:
        
        for bir in bird:
            bir.run(pred)
        for pre in pred:
            pre.run(bird)
            pre.time()
    #        pre.movebitch(pred)
    else:
        z=0
        bird = [Bird() for i in range(2)]
        pred=baby(pred)






if __name__ == '__main__':
    run()
