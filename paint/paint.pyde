AAA=0
def setup():
    size(1000,1000)
def draw():
    global AAA
    strokeWeight(0)
    rect(0,0,200,100)
    rect(210,0,200,50)
    rect(210,60,200,50)
    rect(420,0,200,100)
    fill(0)
    textSize(20)
    text(u"Изменение цвета",10,50)
    text(u"Увеличить размер",220,25)
    text(u"Уменьшить размер",215,95)
    text(u"100 точек",470,50)
    fill(255)
    if mousePressed:
        strokeWeight(AAA)
        line(mouseX, mouseY, pmouseX, pmouseY)
def mouseClicked():
    global AAA
    if mouseX >= 0 and mouseX <= 200 and mouseY >= 0 and mouseY <= 100:
        stroke(random(255),random(255),random(255))
    if mouseX >= 210 and mouseX <= 410 and mouseY >= 0 and mouseY <= 50:
        AAA += 5
    if mouseX >= 210 and mouseX <= 410 and mouseY >= 60 and mouseY <= 100:
        AAA -= 5
    if mouseX >= 420 and mouseX <= 620 and mouseY >= 0 and mouseY <= 100:
        for step in range(100):
            point(random(1000),random(1000))
    if AAA == 5:
        AAA = 10
        
        
    
    
