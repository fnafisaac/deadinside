size_t = 100
mode = "dec"
def setup():
    size(1000,1000)
    rectMode(CENTER)
def draw():
    background(0)
    global size_t,mode
    if size_t >= 400:
        mode = "dec"
    if mode == "dec":    
        size_t -= 10
    if size_t <= 100:
        mode = "s"    
    if mode == "s":
        size_t += 10
    rect(500,500,size_t,size_t)
    if mousePressed:
        if mouseButton == RIGHT:
            fill(0)
def mouseClicked():
    if mouseButton == LEFT:
        fill(random(255), random(255), random(255))
    

        
        
        
