import turtle

t=turtle.Turtle()
window=turtle.Screen()
window.bgcolor('yellow')
t.shape('turtle')
t.speed(0.75)
t.color('green')

d=0
x=2
for i in range(100):
    for i in range(18):
        t.right(10)
        t.forward(d)
    d-=x

window.exitonclick()
