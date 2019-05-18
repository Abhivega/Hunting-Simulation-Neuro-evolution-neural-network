from tala import Bird
from pray import Pray
from p5 import *
bird=[Bird() for i in range(15)]
pray=[Pray() for i in range(2)]

def setup():
    size(700, 500)
    no_stroke()
    fill(255)
    
def alldead():
    if len(bird) == 0:
       for i,k in enumerate( pray):
          print("preditor " +str(i)+" killed :", k.kill)

    
def draw():
    background(255)
    alldead()
    for bir in bird:
         bir.run(pray)
    for prayy in pray:
         prayy.run(bird)   
         prayy.movebitch(pray)
          
if __name__ == '__main__':
    run()
