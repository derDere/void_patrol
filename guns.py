

class Bullet:
    
    def __init__(self, c, r, s, x, y, h, d):
        self.c1 = color(c) # Color 1
        self.c2 = lerpColor(self.c1, color(255), 0.4) # Color 2
        self.c3 = lerpColor(self.c1, color(255), 0.8) # Color 3
        self.r = float(r) # Radius
        self.pos = PVector(x, y)
        self.dir = PVector.fromAngle(h)
        self.dir.normalize()
        self.dir.mult(s)
        self.kill = False # Remove
        self.d = d # Damage
    
    def loop(self, tick):
        self.pos.add(self.dir)
        
        if (self.pos.x > (width + self.r)) or (self.pos.x < -self.r) or (self.pos.y > (height + self.r)) or (self.pos.y < -self.r):
            self.kill = True
    
    def draw(self, tick):
        push()
        noStroke();
        translate(self.pos.x, self.pos.y)
        
        fill(self.c1)
        circle(0, 0, self.r)
        
        fill(self.c2)
        circle(0, 0, self.r * 0.66)
        
        fill(self.c3)
        circle(0, 0, self.r * 0.3)
        
        pop()


class WeaponType:
    def __init__(self):
        self.color = 0x3F007FFF
        self.indexes = [0] # indexes of gun points the more indexes the more shots fired
        self.angles = [0] # angles of fire. the more angles the more shots fired
        self.radius = 30 # size of the bullets
        self.speed = 15 # speed of the bullet
        self.coolDown = 10 # weapon cooldown (works together with the weapon headUp)
        self.damage = 5 # bullet damage
    
    def __str__(self):
        #return f"I{len(self.indexes)}A{len(self.indexes)}R{self.radius}S{self.speed}C{self.coolDown}"
        return "%iA%i-%irS%i (%iCD)" % (len(self.indexes), len(self.angles), self.radius, self.speed, self.coolDown)
    
    def enemy_gun_1(self):
        self.color = 0x3FFF0000
        self.indexes = [0]
        self.angles = [PI]
        self.radius = 30
        self.speed = 10
        self.coolDown = 50
        self.damage = 1


class Weapon:
    
    def __init__(self, ship):
        self.ship = ship # parent ship
        self.bullets = [] # flying bullets
        self.heatUp = 0 # weapon heat (manages cooldown)
        self.type = WeaponType() # weapon type
    
    def loop(self, tick):
        toRemove = []
        for bullet in self.bullets:
            bullet.loop(tick)
            if bullet.kill:
                toRemove.append(bullet)
        for bullet in toRemove:
            self.bullets.remove(bullet)
        if self.heatUp > 0:
            self.heatUp -= 1
    
    def draw(self, tick):
        for bullet in self.bullets:
            bullet.draw(tick)
    
    def shoot(self):
        if self.heatUp <= 0:
            for gpi in self.type.indexes:
                gpos = self.ship.get_gun_point(gpi)
                for a in self.type.angles:
                    bullet = Bullet(self.type.color, self.type.radius, self.type.speed, gpos.x, gpos.y, a, self.type.damage)
                    self.bullets.append(bullet)
            self.heatUp = self.type.coolDown
            
























































# EOF
