x = 10
y = 10
def setup():
    size(500,500)
    rectMode(CENTER)
def draw():
    global x,y
    if keyPressed:
        x = x + 5
    fill(255)
    textSize(10)
    textAlign(CENTER,CENTER)
    text(key,x,175)
