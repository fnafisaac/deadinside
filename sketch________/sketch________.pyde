from math import copysign

FLAKES, YMIN, YMAX = 500, -500, 50
RANGE = tuple(range(FLAKES))
#ниже вставь свой код

def setup():
    size(1920, 1080, FX2D)
    noStroke()
    fill(255)
    global flakes
    flakes = tuple(Flake(random(width), random(YMIN, YMAX)) for i in RANGE)
#ниже вставь свой код

def draw():
    background(0)
    for f in flakes: f.show().update()
    changeAllFlakesSpeed()
    this.surface.title = 'FPS: ' + `this.round(frameRate)`
#ниже вставь свой код
    ellipse(400,680,100,100)
    ellipse(400,620,80,80)
    ellipse(400,560,60,60)
    fill (0,0,0)
    ellipse(390,560,10,10)
    ellipse(420,560,10,10)
    stroke (228,122,30)
    strokeWeight(10)
    line(390,570,430,570) 
    stroke (0)
    noStroke()
    fill(255)
#это трогать не нужно
def keyPressed():
    k = chr(keyCode) if key != CODED else keyCode

    if k == 'R' or k == ENTER or k == RETURN:
        for f in flakes: f.reset(random(width), random(YMIN, YMAX))

def changeAllFlakesSpeed():
    if not keyPressed: return

    k = key.upper() if key != CODED else keyCode

    if k == 'W' or k == UP:
        for f in flakes: f.vel.y -= f.maps[2]

    elif k == 'S' or k == DOWN:
        for f in flakes: f.vel.y += f.maps[2]

    elif k == 'A' or k == LEFT:
        for f in flakes: f.vel.x -= f.maps[2]

    elif k == 'D' or k == RIGHT:
        for f in flakes: f.vel.x += f.maps[2]


class Flake:
    Z, INC = 3.0, .01
    def __init__(f, x, y):
        f.vec = __pvector__()
        f.vel = __pvector__()
        f.reset(x, y)
    def __str__(f):
        return 'vec: %s\tvel: %s' % (f.vec, f.vel)
    def reset(f, x, y):
        z = random(f.Z)

        f.maps = (
            map(z, 0, f.Z, .5, 1.5),
            map(z, 0, f.Z, 2, 5),
            map(z, 0, f.Z, .01, .03)
        )

        f.vec.set(x, y)
        f.vel.set(0, f.maps[0])

        return f
    def show(f):
        ellipse(f.vec.x, f.vec.y, f.maps[1], f.maps[1])
        return f
    def update(f):
        f.vec.add(f.vel)
        f.vel.add(copysign(f.INC, -f.vel.x), f.INC)

        if f.vec.y > height:
            f.vec.set(random(width), random(YMIN, -YMAX))
            f.vel.y = f.maps[0]

        if   f.vec.x < 0:     f.vec.x = random(width>>1, width)
        elif f.vec.x > width: f.vec.x = random(100)

        return f
