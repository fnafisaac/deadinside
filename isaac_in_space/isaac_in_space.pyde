a=0
bg=0
bg2=0
c=0
d=0
people=0
e=0
f=0
g=0
h=0
j=0
k=0
x=260
y=400
x2=0
y2=0
x3=260
y3=400
vertical=0
def setup():
    global people, bg, barrier , y,bg2
    size(800,800)
    url = "https://static.wikia.nocookie.net/bindingofisaac/images/7/78/Isaac_Fate.png"
    people = loadImage(url, "png")
    url2= "https://cdn.dribbble.com/users/2208405/screenshots/10344568/media/c8d261e7fbe2739731b99a731801d90a.png"
    bg= loadImage(url2, "png")
    bg2= loadImage(url2, "png")
    url3= "https://static.wikia.nocookie.net/bindingofisaacre_gamepedia/images/a/ab/Pickup_Joker_icon.png/revision/latest/scale-to-width-down/35?cb=20141111090955"
    barrier = loadImage(url3,"png")
def draw():
    global x, y, bg, vertical, barrier,people, x2
    background(0)
    image(bg,x2,0)
    image(bg2,x2+bg.width, 0)
    image(people, width/2, y, 100,30)
    image(barrier,400,400,112,144 )
    vertical += 1
    y += vertical
    x2 -= 1  
def keyPressed():
    global x,vertical
    if key == ' ':
        vertical = -15
                    
