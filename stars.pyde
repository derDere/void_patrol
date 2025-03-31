from sky import Sky
from ship import Ship
from guns import Weapon
from enemy import Enemy, EnemyTypeInvader1


DEBUG = True
STAR_COUNT = 1000


tick = -1
sky = None
ship = None
gun = None
enemies = []


def setup():
    global sky, ship, gun
    frameRate(240)
    size(1800, 1200)
    sky = Sky(STAR_COUNT)
    ship = Ship()
    gun = Weapon(ship)


def draw():
    global sky, ship, gun, tick
    tick += 1
    #background(0)
    
    ship.loop(tick)
    gun.loop(tick)
    
    sky.draw(tick)
    gun.draw(tick)
    ship.draw(tick)
    
    removeEnemies = []
    for enemy in enemies:
        enemy.shield.check(gun)
        enemy.loop(tick)
        enemy.draw(tick)
        ship.shield.check(enemy.gun)
        if enemy.kill:
            removeEnemies.append(enemy)
    for enemy in removeEnemies:
        enemies.remove(enemy)
    if (tick % 100) == 0:
        e = Enemy()
        e.set_type(EnemyTypeInvader1())
        enemies.append(e)
    
    if mousePressed:
        gun.shoot()
    
    push()
    textAlign(LEFT, TOP)
    textSize(20)
    text('Shield: ', 10, 10)
    
    noStroke();
    fill(0xFF002347)
    rect(75, 10, 400, 15)
    fill(0xFF007FFF)
    rect(75, 10, max(map(ship.shield.health, 0, 100, 0, 400), 0), 15)
    pop()
    
    if not DEBUG:
        push()
        translate(0, 50)
        textSize(20)
        text('WT: %s' % gun.type, 20, 30)
        text('TR: %i' % (ship.targetRotation / (2*PI) * 360), 20, 60)
        text('AR: %i' % (ship.rotation / (2*PI) * 360), 20, 90)
        text('BC: %i' % len(gun.bullets), 20, 120)
        text('T: %i' % tick, 20, 150)
        pop()
        
        
        
