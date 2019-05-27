from Hunted import Bird
from Hunter import Predator
from p5 import *
global z
z=0

bird = [Bird() for i in range(4)]
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
    global z
    z+=1
    background(255) 
    if z <  700:
    #    alldead()
        for bir in bird:
            bir.run(pred)
        for prayy in pred:
            prayy.run(bird)
            prayy.movebitch(pred)
    else:
        z=0
        a=500
        b=0
        for i,prayy in enumerate(pred):
            if prayy.min < a:
                a=pray.kill
                b=i
    



if __name__ == '__main__':
    run()
