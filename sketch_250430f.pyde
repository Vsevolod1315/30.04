x=0
def setup():
    size(800,800)
def draw():
    global x
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(400,400,x,x)
    if mouseButton ==LEFT :
        x=x+2
    if mouseButton == RIGHT :
        x=x-2
        
        
