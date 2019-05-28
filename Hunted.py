from p5 import *
import random as rn
import numpy as np


class Bird():
    def __init__(self):
        self.position = Vector(rn.randint(20, 1100),
                               rn.randint(20, 550))

        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.top_speed = 8
        self.chase = False

    def show1(self):
        stroke(0)
        fill(255, 0, 0)
        circle(self.position, 6)

    def show(self):
        stroke(0)
        fill(0)
        circle(self.position, 6)

    def update(self):
        self.velocity += self.acceleration
        self.velocity.limit(self.top_speed)
        self.position += self.velocity
        self.acceleration = Vector.from_angle(rn.uniform(-np.pi, np.pi))

    def checkobs(self):
        if self.position.y > 650:
            self.velocity.y = - self.velocity.y
            self.position = Vector(self.position.x, 650)
            self.acceleration = Vector(0, 0)

        elif self.position.y < 20:
            self.velocity.y = - self.velocity.y
            self.position = Vector(self.position.x, 20)
            self.acceleration = Vector(0, 0)

        elif (self.position.x > 1250):
            self.velocity.x = - self.velocity.x
            self.position = Vector(1250, self.position.y)
            self.acceleration = Vector(0, 0)

        elif self.position.x < 20:
            self.velocity.x = - self.velocity.x
            self.position = Vector(20, self.position.y)
            self.acceleration = Vector(0, 0)

    def flee(self, Pray):
        for pray in Pray:
            k = dist(self.position, pray.position)
            if k < 50:
                m = remap(k, (0, 50), (2, 5))
                diff = -(pray.position - self.position)
                acceleration = diff + self.velocity
                acceleration.normalize()
                self.acceleration = acceleration * m

    def run(self, pray):

        self.flee(pray)
        self.checkobs()
        self.update()
        if self.chase:
            self.show1()
        else:
            self.show()
        self.chase = False
