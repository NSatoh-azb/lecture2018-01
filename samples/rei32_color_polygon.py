import turtlesvg as ttl
import math

t = ttl.MyTurtle()

def color_polygon(n, e=200, m=15):
    if m > 0:
        # R：0～1, G：0～0.5，B：1（固定）
        t.fillcolor(m/15, m/30, 1)
        t.begin_fill()
        for i in range(n):
            t.fd(e)
            t.rt(360/n)
        t.end_fill()
        t.penup()
        t.fd(e/2)

        # 次の辺の長さは余弦定理
        a = math.radians(360/n)
        c = math.cos(a)
        next_e = e * (2 + 2*c)**0.5 /2
        t.rt(360/n/2)
        t.pendown()

        color_polygon(n, next_e, m-1)

t.pu()
t.goto(-100, 200)
t.pd()

color_polygon(5)
