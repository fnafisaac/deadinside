a=0
bd=0
c=0
d=0
e=0
f=0
g=0
h=0
j=0
k=0
x=400
y=400
def setup():
    global i, bd
    size(800,800)
    url = "https://static.wikia.nocookie.net/bindingofisaac/images/7/78/Isaac_Fate.png/revision/latest?cb=20150321003218"
    i = loadImage(url, "png")
    url2= "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/items/264280/87f668f25bfa64fbb754be7300da0bc93ce11396.jpg"
    bd= loadImage(url2, "jpg")
def draw():
    global x, y, bd
    background(0)
    image(bd,0,0,800,800)
    image(i, x, y)
    y=y+5
def keyPressed():
    global x,y
    if key == ' ':
        y=y-20
    
        
