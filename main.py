import turtle
from turtle import Screen, Turtle


pointer = Turtle()
turtle.colormode(255)
pointer.speed('fastest')
pointer.hideturtle()

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

x_initial = -200
y = -200
z = 0
for vertical_dots in range(10):
    x = x_initial
    pointer.teleport(x,y)
    pointer.dot(20, color_list[z])
    for horizontal_dots in range(10):
        pointer.teleport(x, y)
        pointer.dot(20, color_list[z])
        x += 50
        z += 1
        if z >= len(color_list):
            z = 0
    y += 50
    z += 1












my_screen = Screen()
my_screen.exitonclick()