import math
from tkinter import *
from colors import COLORS
import random

root = Tk()
c = Canvas(root, width=1200, height=1200, bg="white")
cirlce = c.create_oval(590, 590, 600, 600, fill='red')



global angle
global dist
global x1
global y1

x1 = 595
y1 = 595

dist = 595
angle = 0


def dot (x1,y1, color):
    grup = c.create_oval(x1-5,y1-5, x1+5,y1+5, fill=color, outline='black')


def dot_power(clr):
    global angle
    global dist
    global x1
    global y1
    dot(
        ((x1 - dist) * math.cos(math.radians(angle)) - (y1 - dist) * math.sin(math.radians(angle))) + dist,
        ((x1  - dist) * math.sin(math.radians(angle)) + (y1 - dist) * math.cos(math.radians(angle))) + dist,
        clr)

    # dot(
    #     ((x1 - dist) * math.cos(math.radians(angle/3)) - (y1 - dist) * math.sin(math.radians(angle/3))) + dist,
    #     ((x1  - dist) * math.sin(math.radians(angle/3)) + (y1 - dist) * math.cos(math.radians(angle/3))) + dist,
    #     clr)
    #
    # dot(
    #     ((x1+10 - dist) * math.cos(math.radians(angle)) - (y1+10 - dist) * math.sin(math.radians(angle))) + dist,
    #     ((x1+10  - dist) * math.sin(math.radians(angle)) + (y1+10 - dist) * math.cos(math.radians(angle))) + dist,
    #     clr)
    #
    # dot(
    #     ((x1+15 - dist) * math.cos(math.radians(angle)) - (y1+15 - dist) * math.sin(math.radians(angle))) + dist,
    #     ((x1+15  - dist) * math.sin(math.radians(angle)) + (y1+15 - dist) * math.cos(math.radians(angle))) + dist,
    #     clr)

    dot(
        ((x1 - dist*2) * math.cos(math.radians(angle)) - (y1 - dist*2) * math.sin(math.radians(angle))) + dist,
        ((x1  - dist*2) * math.sin(math.radians(angle)) + (y1 - dist*2) * math.cos(math.radians(angle))) + dist,
        clr)

    angle += 10
    # dist += 1
    x1 += 1
    y1 += 1

def dot_spawn(clr):
    root.after(50, dot_power,  clr)

    if dist < 10000:
        root.after(50, dot_spawn, random.choice(COLORS))

c.pack()

root.after(150, dot_spawn, random.choice(COLORS))
root.mainloop()