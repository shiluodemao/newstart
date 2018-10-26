import turtle
def triangle(turtle,distance):
    for i in range(3):
       turtle.forward(distance)
       turtle.left(120)
def tri_in_tri(turtle,distance,j):
   
   if j==0:
      turtle.begin_fill()
      turtle.fillcolor('green')
      triangle(turtle,distance)
      turtle.end_fill()
      
   else:
      for i in range(3):
         turtle.begin_fill()
         turtle.fillcolor('green')
         triangle(turtle,distance)
         turtle.end_fill()
         turtle.forward(distance/2)
         turtle.right(120)
         tri_in_tri(turtle,distance/2,j-1)
         turtle.left(120)
         turtle.forward(distance/2)
         turtle.left(120)
         
   
      
    
      
   
def draw_triangles():
   window=turtle.Screen()
   window.bgcolor('yellow')
   brad=turtle.Turtle()
   brad.color('red')
   brad.speed('100')
   triangle(brad,204.8)
   
   brad.forward(102.4)
   brad.left(60)
   tri_in_tri(brad,102.4,4)
   
   window.exitonclick()
   
draw_triangles()
   
    