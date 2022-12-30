# import package
import turtle

# method to draw ellipse
def draw(rad,rad1):
	
 # rad --> radius of arc
 for i in range(100):
	
	# two arcs
  turtle.goto(0,-22)
  turtle.circle(rad,rad1)
  turtle.circle(rad//2,rad1)
  turtle.circle(-rad,-rad1+30)
  turtle.circle(-rad//2,-rad1+30)
  rad+=3
  
  

# Main section
# tilt the shape to negative 45
turtle.seth(-60)

# calling draw method
draw(90,90)
