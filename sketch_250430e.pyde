x=0
def setup():
    size(800,800)
def draw():
    global x
    translate(400,400)
    rotate(x)
    ellipse(0,0,80,60)
    if mouseButton ==LEFT:
        x=x+2
    if mouseButton == RIGHT:
        x=x-2
        
        
        
