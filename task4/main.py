import math
from tkinter import *
from colors import COLORS
import random

root = Tk()
c = Canvas(root, width=1200, height=1200, bg="white")

x1 = 620
y1 = 550

x2 = 700
y2 = 400

x3 = 780
y3 = 550

x4 = 700
y4 = 700

global angle
global size_x
global size_y

angle = 0
size_x = 0
size_y = 0

def listok (x1,y1, x2,y2, x3,y3, x4,y4, color):
    grup = c.create_polygon(x1,y1, x2,y2, x3,y3, x4,y4,
                fill=color, outline='black')


def poyav_list( clr, count=0):
    global angle
    global size_x
    global size_y
    listok(((x1 + size_x - x4) * math.cos(math.radians(angle)) - (y1 + size_y - y4) * math.sin(math.radians(angle))) + x4,
           ((x1 + size_x - x4) * math.sin(math.radians(angle)) + (y1 + size_y - y4) * math.cos(math.radians(angle))) + y4,

           ((x2 - x4) * math.cos(math.radians(angle)) - (y2 + size_y - y4) * math.sin(math.radians(angle))) + x4,
           ((x2 - x4) * math.sin(math.radians(angle)) + (y2 + size_y - y4) * math.cos(math.radians(angle))) + y4,

           ((x3 - size_x - x4) * math.cos(math.radians(angle)) - (y3 + size_y - y4) * math.sin(math.radians(angle))) + x4,
           ((x3 - size_x - x4) * math.sin(math.radians(angle)) + (y3 + size_y - y4) * math.cos(math.radians(angle))) + y4,

           (x4),
           (y4),
           clr)
    angle += 137.5
    size_x += 2
    size_y += 5
    count += 1
    if count < 3:
        root.after(150, poyav_list, clr, count)

def grow_up(clr):
    global angle
    global size_x
    global size_y
    root.after(350, poyav_list,  clr)

    if size_x < 75:
        root.after(350, grow_up, random.choice(COLORS))

c.pack()

root.after(150, grow_up, random.choice(COLORS))
root.mainloop()