import turtle, math

landon = turtle.Turtle()
landon.color('orange')
landon.shape('turtle')

for i in range(1000):
    landon.forward(math.cos(2*i)*400)
    if i % 2 == 0:
        landon.right(i)
    else:
        landon.left(i)
turtle.done()
