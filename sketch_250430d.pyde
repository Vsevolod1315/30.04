def setup():
    size(800,800)
def draw():
    background(0)
    if  mouseButton ==LEFT:
       ellipse(350,350,90,20)
       ellipse(450,350,90,20)
       rect(330,400,70,20)
       rect(370,400,70,20)
       rect(400,400,20,75)
    if mouseButton ==RIGHT:
       ellipse(400,400,200,200)
    if mouseButton ==CENTER:
        ellipse(400,400,40,80)
