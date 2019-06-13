import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    
    
    windows_screen = turtle.Screen()
    windows_screen.bgcolor("blue")
    windows_screen.exitonclick()


def testing_to_draw():
    testing = turtle.Turtle()
    testing.forward(200)
    testing.right(90)
    testing.forward(200)
    testing.right(135)
    testing.forward(270)
    testing.circle(100)


    windows_screen = turtle.Screen()
    windows_screen.bgcolor("blue")
    windows_screen.exitonclick()
    


testing_to_draw()