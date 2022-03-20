x=0 
y=0
def setup():
    size(600,600)
def draw():
    global x,y
    line(200,0,200,600)
    line(400,0,400,600)
    line(0,200,600,200)
    line(0,400,600,400)
    #for y in range(0,600,200):
       # for x in range(0,600,200):
          #  rect(x,y,200,200)
        
def mouseClicked():   
    x = mouseX
    y = mouseY
    
    if x > 0 and x < 200 and y > 0 and y < 200:
        if mouseButton == RIGHT:
            ellipse(100,100,200,200)
        if mouseButton == LEFT:
            line(0,200,200,0)
            line(200,200,0,0)
    if x > 200 and x < 400 and y > 0 and y < 200:
        if mouseButton == LEFT:
            line(200,200,400,0)
            line(400,200,200,0)
    if x > 400 and x < 600 and y > 0 and y < 200:
        line(400,200,600,0)
        line(600,200,400,0)
    if x > 0 and x < 200 and y > 200 and y < 400:
        line(0,200,200,400)
        line(200,200,0,400)
    if x > 200 and x < 400 and y > 200 and y < 400:
        line(200,200,400,400)
        line(400,200,200,400)
    if x > 400 and x < 600 and y > 200 and y < 400:
        line(400,200,600,400)
        line(600,200,400,400)
    if x > 0 and x < 200 and y > 400 and y < 600:
        line(0,400,200,600)
        line(200,400,0,600)
    if x > 200 and x < 400 and y > 400 and y < 600:           
        line(200,400,400,600)
        line(400,400,200,600)
    if x > 400 and x < 600 and y > 400 and y < 600:                          
        line(400,400,600,600)
        line(600,400,400,600)
           
        
        
