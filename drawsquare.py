import turtle
def draw_square():
   window=turtle.Screen()
   window.bgcolor('green')
   brad=turtle.Turtle() 
   brad.shape('turtle')
   brad.color('black')
   brad.speed=20000
   katie=turtle.Turtle()
   katie.speed=200
   katie.color('red')
   ash=turtle.Turtle()
   for i in range(36):
       for j in range(3):
           brad.forward(100)
           brad.left(120)
       brad.left(10) 
       for k in range(4):
          katie.forward(50)
          katie.right(90)
       katie.right(10)
       ash.circle(50-i)
       ash.left(10)
   window.exitonclick()
   

draw_square()
   