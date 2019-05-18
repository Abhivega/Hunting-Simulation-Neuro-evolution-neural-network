from p5 import *
import random as rn

class Predator(object):
    
    def __init__(self):
        # our object has two Vectors: location and velocity
        self.position = Vector(rn.randint(0,700),
                               rn.randint(0,500))

        self.velocity = Vector(random_uniform(low=-2, high=2),
                               random_uniform(low=-2, high=2))
        self.acceleration=Vector(0,0)
        self.top_speed=6
        self.kill=0

    def update(self):
        
        self.velocity.limit(self.top_speed)
        self.position+=self.velocity
        self.velocity+=self.acceleration
        self.acceleration=Vector(0,0)

    def show(self):
        stroke(0)
        x=remap(self.kill,(0,15),(0,255))
        y=remap(self.kill,(0,15),(255,0))
        fill(x,y,0)
        circle(self.position, 15)
    

    def checkobs(self):
        if self.position.y  > 500 :
            self.velocity.y =- self.velocity.y
            self.position=Vector(self.position.x,500)
            self.acceleration= Vector(0,0)
            
        elif self.position.y < 20 :
             self.velocity.y =- self.velocity.y
             self.position=Vector(self.position.x,20)
             self.acceleration= Vector(0,0)
             
        elif (self.position.x > 700) :
             self.velocity.x =- self.velocity.x
             self.position=Vector(700, self.position.y)
             self.acceleration= Vector(0,0)
             
             
        elif  self.position.x < 20:
            self.velocity.x =- self.velocity.x
            self.position=Vector(20,self.position.y)
            self.acceleration= Vector(0,0)
            
    def movebitch(self,ppray):
        for pray in ppray: 
             run =remap(self.kill,(0,15),(8,20))
             self.top_speed= run


         
            
    def hund(self,bird):
         k=[]
         if len(bird) == 0:
              return
         for i,bir in enumerate (bird):
 #            bir.chase=False
             k.append(dist(self.position,bir.position))
         kmin=int(min(k))
         i=k.index(min(k))
         if kmin < 250 and kmin > 15:
                  m=remap(kmin,(15,250),(4,10))
                  bird[i].chase = True
                  diff =  bird[i].position - self.position 
                  acceleration= diff + self.velocity
                  acceleration.normalize()
                  self.acceleration = acceleration*m
                  
         if kmin < 10 :
                   bird.pop()
                   self.headcount()
#        return self.acceleration
    def headcount(self):
         self.kill += 1
         return (self.kill)
         
    def run(self,bird): 
         
         self.update()
         self.hund(bird)
         self.checkobs()
         
         self.show() 

         
         
                
               
               
