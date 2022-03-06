y = 0
kill = 255
def setup():
    size(1000,1000)
def draw():
    global y, kill
    x = 0
    for i in range(101):
        fill(kill)
        rect(x,y,10,10)
        x += 10  
        if kill == 255:
            kill = 0
        else:
            print('else')
            kill = 255
    y += 10
    if kill == 255:
        kill = 255
    else:
        kill = 0

    

        
    
        
        
