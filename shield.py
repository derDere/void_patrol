

def circle_intersects_triangle(pos, radius, v1, v2, v3):
    # 1. Check if circle center is inside the triangle
    if point_in_triangle(pos, v1, v2, v3):
        return True

    # 2. Check if any triangle vertex is inside the circle
    if pos.dist(v1) <= radius or pos.dist(v2) <= radius or pos.dist(v3) <= radius:
        return True

    # 3. Check if any triangle edge intersects the circle
    if point_to_segment_distance(pos, v1, v2) <= radius:
        return True
    if point_to_segment_distance(pos, v2, v3) <= radius:
        return True
    if point_to_segment_distance(pos, v3, v1) <= radius:
        return True

    return False


def point_in_triangle(p, a, b, c):
    d1 = sign(p, a, b)
    d2 = sign(p, b, c)
    d3 = sign(p, c, a)

    has_neg = d1 < 0 or d2 < 0 or d3 < 0
    has_pos = d1 > 0 or d2 > 0 or d3 > 0

    return not (has_neg and has_pos)


def sign(p1, p2, p3):
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)


def point_to_segment_distance(p, a, b):
    ab = b.copy().sub(a)
    ap = p.copy().sub(a)

    ab_length_sq = ab.magSq()
    if ab_length_sq == 0:
        return p.dist(a)  # a and b are the same point

    t = constrain(ap.dot(ab) / ab_length_sq, 0, 1)
    closest = a.copy().add(ab.mult(t))
    return p.dist(closest)


def center_of_points(points):
    if not points:
        return PVector(0, 0)
    
    sum_vec = PVector(0, 0)
    for p in points:
        sum_vec.add(p)
    
    count = len(points)
    return sum_vec.div(count)


def is_vector_in_ellipse(o, s, v):
    # Distance from the center, normalized
    dx = (v.x - o.x) / s.x
    dy = (v.y - o.y) / s.y
    
    # Check if inside the ellipse using the standard ellipse equation
    return (dx * dx + dy * dy) <= 1


class Shield:
    
    def __init__(self, color, w, h, origin, pos):
        self.color = color
        self.sizeHalf = PVector(w, h)
        self.sizeHalf.mult(0.5)
        self.offSet = pos
        self.origin = origin
        self.health = 100
        self.blink = 0
        self.visible = False
    
    def check(self, bullets):
        pos = self.origin.pos.copy()
        pos.add(self.offSet)
        for bullet in bullets:
            intersects = is_vector_in_ellipse(pos, self.sizeHalf, bullet.pos)
            if intersects:
                self.blink = 30
                self.health -= bullet.d
                bullet.kill = True
    
    def loop(self, tick):
        if self.blink > 0:
            self.blink -= 1

    def draw(self, tick):
        if (self.blink > 0) or self.visible:
            push()
            noFill()
            
            t = self.color & 0x13FFFFFF # most transparent color
            w = 0x7FFFFFFF # half transparent white
            
            pos = self.origin.pos.copy()
            pos.add(self.offSet)
            
            ms = sin(tick / 5)
            mss = int(map(ms, -1, 1, 15, 20))
            for i in range(1, mss, 5):
                l = map(i, 1, 19, 1, 0)
                c = lerpColor(t, w, l)
                stroke(c)
                strokeWeight(i)
                if i == 1:
                    fill(t)
                else:
                    noFill()
                ellipse(pos.x, pos.y, self.sizeHalf.x * 2, self.sizeHalf.y * 2)
            
            pop()



#
# DEPRICATED: To Slow
#
class ShieldFrame:
    
    def __init__(self, color, *frame):
        self.color = color
        self.frame = frame
        self.center = center_of_points(self.frame)
        self.health = 100
        self.blink = 0
        self.visible = False
    
    def check(self, gun, shieldPos):
        for bullet in gun.bullets:
            intersects = False
            for i in range(1, len(self.frame)):
                p1 = self.frame[i-1].copy()
                p2 = self.frame[i].copy()
                p3 = self.center.copy()
                p1.add(shieldPos)
                p2.add(shieldPos)
                p3.add(shieldPos)
                if circle_intersects_triangle(bullet.pos, bullet.r, p1, p2, p3):
                    intersects = True
                    break
            if intersects:
                self.blink = 30
                self.health -= bullet.d
                bullet.kill = True
    
    def loop(self, tick):
        if self.blink > 0:
            self.blink -= 1

    def draw(self, tick):
        if (self.blink > 0) or self.visible:
            push()
            noFill()
            
            t = self.color & 0x13FFFFFF
            w = 0x7FFFFFFF
            strokeJoin(ROUND)
            
            ms = sin(tick / 5)
            mss = int(map(ms, -1, 1, 15, 20))
            for i in range(1, mss, 5):
                l = map(i, 1, 19, 1, 0)
                c = lerpColor(t, w, l)
                stroke(c)
                strokeWeight(i)
                if i == 1:
                    fill(t)
                else:
                    noFill()
                beginShape()
                for p in self.frame:
                    vertex(p.x, p.y)
                endShape(CLOSE)
            
            pop()



























































# EOF
