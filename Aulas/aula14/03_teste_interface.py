import math
import turtle


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

        


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)


def petala(t, n, length, degrees):
    angle = degrees/n
    polyline(t, n, length, angle)
    t.lt(180-(angle*n))
    polyline(t, n, length, angle)


def flor(t, n, length, degrees):
    times = int(360/degrees)
    
    for i in range(times):
        petala(t, n, length, degrees)


bob = turtle.Turtle()

flor(bob,10,20,15)


print(bob)
turtle.mainloop()
