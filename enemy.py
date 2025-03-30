from random import randint
from guns import Weapon
from shield import Shield


class Enemy:
    
    def __init__(self):
        self.pos = PVector(width + 200, randint(0, height))
        self.dir = PVector(-2.5, 0)
        self.kill = False
        self.gun = Weapon(self)
        self.gun.type.enemy_gun_1()
        #self.shield = ShieldFrame(
        #                     0xFF7FF00FF,
        #                     PVector( 0, -50),
        #                     PVector( 50, 0),
        #                     PVector( 0, 50),
        #                     PVector( -50, 0),
        #                   )
        self.shield = Shield(0xFF7FF00FF, 70, 70, self, PVector(0,0))
        self.shield.health = 20
    
    def get_gun_point(self, pointIndex):
        return self.pos.copy()
        #points = [ (110, 0), (40, -42.5), (40, 42.5), (30, -100), (30, 100) ]
        #pointIndex %= len(points)
        #x, y = points[pointIndex]
        #p = PVector(x, y)
        #p.rotate(self.rotation)
        #p.add(PVector(self.x, self.y))
        #return p.x, p.y
    
    def loop(self, tick):
        self.pos.add(self.dir)
        self.gun.shoot()
        self.gun.loop(tick)
        self.shield.loop(tick)
        if self.pos.x < -100:
            self.kill = True
        if self.shield.health <= 0:
            self.kill = True
    
    def draw(self, tick):
        push()
        translate(self.pos.x, self.pos.y)
        fill(200)
        stroke(255)
        circle(0, 0, 30)
        pop()
        self.shield.draw(tick)
        self.gun.draw(tick)
