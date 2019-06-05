from Hunted import Bird
from neurlnet import Neuralnet
from Hunter import Predator
from p5 import *
from copy import deepcopy
import numpy as np

global bird
global pred
global nodead
global saveme
nodead = True
global count
count = 0

net = Neuralnet(flag=True)


bird = [Bird() for i in range(10)]
pred = [Predator(net, net) for i in range(2)]


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


def key_pressed(event):
    global saveme
    if event.key == 'S':
        np.savez("save.npz", saveme.w1, saveme.w2, saveme.w3)
        print("saved")


def baby(pred):
    global saveme
    a = []
    y=[]
    for pre in pred:
        y.append(pre.kill)
        a.append(pre.rank())
    first = sorted(a)[0]
    second = sorted(a)[1]
    i = a.index(first)
    j = a.index(second)
    print(a, i, j)
    saveme = deepcopy(pred[i].net)
    one = deepcopy(pred[i])
    one.forone()
    net = deepcopy(pred[i].net)
    net2 = deepcopy(pred[j].net)
    pred = [Predator(net, net2) for i in range(2)]
    pred.append(one)
    return pred


def draw():
    global nodead
    nodead = True
    global bird
    global pred
    global count
    count += 1
    alldead()
    background(255)
    if count < 700 and nodead:

        for bir in bird:
            bir.run(pred)
        for pre in pred:
            pre.run(bird)
            pre.time()
    #        pre.movebitch(pred)
    else:
        count = 0
        bird = [Bird() for i in range(10)]
        pred = baby(pred)


if __name__ == '__main__':
    run()
