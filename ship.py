from shield import Shield


MAX_ROTATION = PI * 0.05

            
def draw_shape(*points):
    beginShape()
    for x, y in points:
        vertex(x, y)
    endShape(CLOSE)

            
def draw_shape_open(*points):
    beginShape()
    for x, y in points:
        vertex(x, y)
    endShape()


class Ship():
    
    def __init__(self):
        self.pos = PVector(-200, height / 2)
        self.exaustAni = float(5)
        self.rotation = float(0)
        self.targetRotation = float(0)
        self.speed = 10
        self.lastX = self.pos.x
        self.shield = Shield(0xFF007FFF, 160, 200, self, PVector(20,0))
    
    def get_gun_point(self, pointIndex):
        points = [ (110, 0), (40, -42.5), (40, 42.5), (30, -100), (30, 100) ]
        pointIndex %= len(points)
        x, y = points[pointIndex]
        p = PVector(x, y)
        p.rotate(self.rotation)
        p.add(self.pos)
        return p
        
    
    def loop(self, tick):
        # movement
        mousePos = PVector(mouseX, mouseY)
        if self.pos.dist(mousePos) < self.speed:
            self.pos = mousePos.copy() 
            self.targetRotation = 0
        else:
            posDelta = mousePos.copy()
            posDelta.sub(self.pos)
            self.targetRotation = posDelta.heading()
            posDelta.normalize()
            posDelta.mult(self.speed)
            self.pos.add(posDelta)
        
        # Flip if going Back
        if (mouseX < self.pos.x):
            self.targetRotation += PI
        
        # Fix Value
        if self.targetRotation < 0:
            self.targetRotation += (PI + PI)
        if self.targetRotation > 2*PI:
            self.targetRotation -= (PI + PI)
        
        # Min Max
        if self.targetRotation < MAX_ROTATION or self.targetRotation > ((2*PI)-MAX_ROTATION):
            pass # We are within the good Range
        elif self.targetRotation < PI:
            self.targetRotation = MAX_ROTATION
        else:
            self.targetRotation = ((2*PI)-MAX_ROTATION)
            
        # Rotate towards targetRotation
        targetRotaV = PVector.fromAngle(self.targetRotation)
        rotaV = PVector.fromAngle(self.rotation)
        rotaV.lerp(targetRotaV, 0.1)
        self.rotation = rotaV.heading()
        
        # trust ani
        self.exaustAni = (self.pos.x - self.lastX) * 10
        if self.exaustAni < 0:
            self.exaustAni = 0
        if self.exaustAni > 80:
            self.exaustAni = 80
        self.lastX = self.pos.x
        
        self.shield.loop(tick)
    
    def draw(self, tick):
        push()
        translate(self.pos.x, self.pos.y)
        rotate(self.rotation)
        
        # exaust
        noStroke();
        fill(0x37FF0000)
        ellipse(-40, 0, 100 + self.exaustAni, 40)
        fill(0x6FFF7F00)
        ellipse(-40, 0, 70 + self.exaustAni, 30)
        fill(0xDFFFFF00)
        ellipse(-40, 0, 40 + self.exaustAni, 20)
        fill(0xFFFFFFFF)
        ellipse(-40, 0, 10 + self.exaustAni, 10)
        
        # metal
        stroke(200)
        fill(120)
        
        # rockets
        ellipse(10, -50, 50, 10)
        ellipse(10, -35, 50, 10)
        ellipse(10,  35, 50, 10)
        ellipse(10,  50, 50, 10)
        
        # thruster top
        draw_shape( (-25, -30), (-45, -40), (-45, -15), (-25, -15) )
        
        # thruster bot
        draw_shape( (-25, 30), (-45, 40), (-45, 15), (-25, 15) )
        
        # big wing top
        draw_shape( (20, -20), (20, -100), (15, -100), (0, -60), (-20, -30), (-20, -10) )
        
        # big wing bottom
        draw_shape( (20, 20), (20, 100), (15, 100), (0, 60), (-20, 30), (-20, 10) )
        
        # middle wing top
        draw_shape( (0, -30), (100, -10), (-20, -10) )
        
        # middle wing bottom
        draw_shape( (0, 30), (100, 10), (-20, 10) )
        
        # center cabine
        draw_shape( (-10, -20), (50, 0), (-10, 20), (-30, 0) )
        
        # frame top top
        draw_shape( (-10, -30), (-30, -20), (-30, -5), (-10, -5) )
        
        # frame top bot
        draw_shape( (-10, 30), (-30, 20), (-30, 5), (-10, 5) )
        
        # fin
        ellipse(-30, 0, 30, 5)
        
        # window
        fill(255, 200, 0)
        draw_shape( (25, -5), (40, 0), (25, 5), (20, 0) )
        
        pop()
        
        self.shield.draw(tick)



















































#
#  OLD Shield Shape
#
        #self.shield = ShieldFrame(
        #                     0xFF007FFF,
        #                     PVector( -55, -45),
        #                     PVector( -10, -70),
        #                     PVector( 10, -110),
        #                     PVector( 30, -110),
        #                     PVector( 30, -70),
        #                     PVector( 45, -60),
        #                     PVector( 45, -33),
        #                     PVector( 113, -18),
        #                     PVector( 113, 18),
        #                     PVector( 45, 33),
        #                     PVector( 45, 60),
        #                     PVector( 30, 70),
        #                     PVector( 30, 110),
        #                     PVector( 10, 110),
        #                     PVector( -10, 70),
        #                     PVector( -55, 45),
        #                   )

















# EOF
