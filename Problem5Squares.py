import turtle
def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()
wn= turtle.Screen()

alex = turtle.Turtle()
alex.pencolor('purple')
alex.pensize(3)

for i in range(5):
    drawSquare(alex,20 + 20*i)

wn.mainloop()

# Kelly Beltran
# 02-26-24
# Probelm 5: Five purple squares are drawn within one another going from smaller to larger