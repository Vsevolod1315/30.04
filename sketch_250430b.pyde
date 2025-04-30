x=0
def setup():
    size(800,800)
def draw():
   global x
   ellipse(400,x,50,50)
   if mouseButton == LEFT:
       x=x+2
       
   
       

    
