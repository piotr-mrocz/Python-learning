import turtle



turtle.setup(800, 500)
turtle.pensize(12)

# yellow ring
turtle.pencolor("yellow")
turtle.circle(80)


# green ring
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

turtle.pencolor("green")
turtle.circle(80)


# red ring
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

turtle.pencolor("red")
turtle.circle(80)


# purple ring
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

turtle.pencolor("purple")
turtle.circle(80)


# blue ring
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()

turtle.pencolor("blue")
turtle.circle(80)