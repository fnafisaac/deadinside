bg=0
time = 0
def setup():
    size(1000,1000)
def draw():
    global bg,time
    time = time + 1
    background(255)
    fill(255)
    rectMode(CENTER)
    rect(500,500,100,50)
    fill(0)
    textSize(10)
    textAlign(CENTER,CENTER)
    text(bg,500,500) 
    text(time,500,10)
    if time == 200 and bg < 30:
        fill(0)
        textSize(30)
        textAlign(CENTER,CENTER)
        text("You lose",500,300)
        noLoop() 
    if time == 200 and bg >= 30:
        fill(0)
        textSize(30)
        textAlign(CENTER,CENTER)
        text("You won",500,300)
        noLoop() 
def mouseClicked():
    global bg,time
    if mouseX > 450 and mouseX < 550 and mouseY > 475 and mouseY < 525:
        bg = bg + 1
        
