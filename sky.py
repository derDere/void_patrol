from random import randint


class Star():
    def __init__(self):
        self.pos = PVector(randint(1, width-2), randint(1, height-2))
        self.r = float(randint(1, 3))
        self.dir = PVector(-self.r / 5, 0)
        self.c1 = float(randint(64, 255))
        self.c2 = min((self.c1 + float(randint(-32, 32))), 255)
        self.c3 = min((self.c1 + float(randint(-32, 32))), 255)
    
    def loop(self, tick):
        self.pos.add(self.dir)
        if self.pos.x <= -3:
            self.pos.add(PVector(width + 6, 0))


class Sky:
    
    def __init__(self, star_count):
        self.star_count = star_count
        self.stars = []
        for i in range(self.star_count):
            s = Star()
            self.stars.append(s)
    
    def draw(self, tick):
        background(0)
        push()
        noStroke()
        for star in self.stars:
            star.loop(tick)
            fill(star.c1, star.c2, star.c3)
            circle(star.pos.x, star.pos.y, star.r)
        pop()
