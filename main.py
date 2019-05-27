from Hunted import Bird
from Hunter import Predator
from p5 import *

bird = [Bird() for i in range(1)]
pred = [Predator() for i in range(2)]


def setup():
    size(1270, 680)
    no_stroke()
    fill(255)


def alldead():
    if len(bird) == 0:
        for i, k in enumerate(pred):
            print("preditor " + str(i) + " killed :", k.kill)


def draw():
    background(255)
    alldead()
    for bir in bird:
        bir.run(pred)
    for prayy in pred:
        prayy.run(bird)
        prayy.movebitch(pred)


if __name__ == '__main__':
    run()
