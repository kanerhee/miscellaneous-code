import turtle
s=turtle.Screen()       #new window


# Creates a yellow rectangle with a blue border
t=turtle.Turtle()       #new turtle
t.up()                      #pen up
t.setposition(100,100)
t.down()                    

t.pencolor('blue')           #set pen color
t.width(20)                  #set pen width
t.setheading(180)           #set pen direction
t.fillcolor('yellow')       #set fill color
t.begin_fill()

t.forward(200)              #top side
t.left(90)

t.forward(150)              #left side
t.left(90)

t.up()                   #move to top right corner
t.setposition(100,100)
t.right(90)
t.down()

t.forward(150)              #right side
t.right(90)

t.forward(200)              #bottom side
t.up()

t.end_fill()                 #end fill








# Creates a green triangle with a red border
# Smaller border
# Centered dimensions


s=turtle.Turtle()


s.up()                      #sets pen below the rectagnle
s.setposition(50,-100)
t.down()

s.pencolor('red')
s.width(20)
s.setheading(180)           #pen direction
s.fillcolor('green')
s.begin_fill()

s.forward(100)
s.left(120)

s.forward(100)
s.left(120)

s.forward(100)
s.left(120)

s.up()
s.end_fill()






s.exitonclick()              #prevents window from freezing
