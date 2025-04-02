from random import randint
from guns import Weapon
from shield import Shield
from ship import draw_shape, draw_shape_open


enemyGunBullets = []


class EnemyTypeBase:
    
    def get_gun_points(self):
        return [(0,0)]
    
    def set_gun(self, gun):
        gun.type.enemy_gun_1()
    
    def get_shield(self, ship):
        s = Shield(0xFF000000, 10, 10, ship, PVector(0,0))
        s.health = 20
        return s 
    
    def draw(self, tick, pos):
        push()
        translate(pos.x, pos.y)
        fill(200)
        stroke(255)
        circle(0, 0, 30)
        pop()


class EnemyTypeInvader1(EnemyTypeBase):
    
    def get_gun_points(self):
        return [(0,0)]
    
    def set_gun(self, gun):
        gun.type.enemy_gun_1()
    
    def get_shield(self, ship):
        s = Shield(0xFFFF00FF, 80, 70, ship, PVector(0,0))
        s.health = 20
        return s 
    
    def draw(self, tick, pos):
        push()
        translate(pos.x, pos.y)
        #scale(2, 2)
        strokeWeight(1)
        
        #bottom backside tentacles
        push()
        fill(0xFF324B21)
        translate(7, -5)
        draw_shape_open( (2,18), (5, 35), (9,25), (10,17) )
        translate(3, 4)
        draw_shape_open( (-18,10), (-30,20), (-31,26),  (-26,32),  (-26,25),  (-24,22),  (-10,16) )
        pop()
        
        # bottom eye elli
        fill(0xFF324B21)
        #ellipse(-20, 5, 20, 20)
        ellipse(-24, 5, 14, 17)
        
        # body elli
        fill(0xFF70924E)
        stroke(0xFF324B21)
        ellipse(0, 0,50,40)
        
        #top eye elli
        noStroke()
        ellipse(-24, 5, 12, 15)
        
        stroke(0xFF324B21)
        strokeJoin(ROUND)
        
        # top spikes
        draw_shape_open( (-20,-11), (-14,-20), (-12,-21), (-13,-16) )
        draw_shape_open( (-7,-18), (0,-25), (0,-18) )
        draw_shape_open( (5,-18), (15,-21), (11,-16) )
        draw_shape_open( (20,-12), (25,-12), (21,-7) )
        draw_shape_open( (24,-2), (29, 0), (23,6) )
        
        # bottom front tentacles
        draw_shape_open( (-18,10), (-30,20), (-31,26),  (-26,32),  (-26,25),  (-24,22),  (-10,16) )
        draw_shape_open( (20,9), (27,17), (28,23),  (23,29),  (23,22),  (21,19),  (13,16) )
        draw_shape_open( (-10,14), (-14,21), (-14,28), (-12,31), (-8,33), (-5,31), (-8,31), (-10,27), (-9,23), (-3,17) )
        draw_shape_open( (2,18), (5, 35), (9,25), (10,17) )
        
        # dots
        noStroke()
        fill(0xFF92AF77)
        ellipse(5, 9, 9, 11)
        ellipse(-15, 9, 5, 4)
        
        # Eye Shadows
        push()
        fill(0xFF4C6D33)
        stroke(0xFF4C6D33)
        translate(2,2)
        ellipse(-28, 5, 6, 8)
        ellipse(-16, -5, 8, 10)
        ellipse(13, -2, 8, 10)
        ellipse(-1, -8, 11, 13)
        ellipse(-8, 5, 7, 7)
        pop()
        
        # Eyes
        fill(0xFFE1582D)
        stroke(0xFF66200D)
        ellipse(-28, 5, 6, 8)
        ellipse(-16, -5, 8, 10)
        ellipse(13, -2, 8, 10)
        ellipse(-1, -8, 11, 13)
        ellipse(-8, 5, 7, 7)
        
        # Eyes
        fill(0xFFEFB377)
        noStroke()
        ellipse(-29, 4, 3, 4)
        ellipse(-17, -6, 4, 5)
        ellipse(12, -3, 4, 5)
        ellipse(-3, -10, 5, 6)
        ellipse(-9, 4, 3, 4)
        
        pop()


class Enemy:
    
    def __init__(self):
        global enemyGunBullets
        self.pos = PVector(width + 200, randint(20, height-20))
        self.dir = PVector(-2.5, 0)
        self.kill = False
        self.gun = Weapon(self)
        self.gun.bullets = enemyGunBullets
        self.type = EnemyTypeBase()
        self.shield = self.type.get_shield(self)
        self.type.set_gun(self.gun)
    
    def set_type(self, newType):
        self.type = newType
        self.shield = self.type.get_shield(self)
        self.type.set_gun(self.gun)
    
    def get_gun_point(self, pointIndex):
        points = self.type.get_gun_points()
        pointIndex %= len(points)
        x, y = points[pointIndex]
        p = PVector(x, y)
        p.add(self.pos)
        return p
    
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
        self.type.draw(tick, self.pos)
        self.shield.draw(tick)
        self.gun.draw(tick)




































































# EOF
