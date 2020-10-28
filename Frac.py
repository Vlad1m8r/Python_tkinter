import math
from tkinter import *
import random

#################################################
class Line():

    def __init__(self, x, y,  dir):
        self.x = x
        self.y = y
        self.dir = dir

    def draw_line(self):
        if self.dir:
            c.create_line(self.x, self.y - 10, self.x, self.y + 10)
            self.ends = [(self.x, self.y - 10), (self.x, self.y + 10)]
        else:
            c.create_line(self.x - 10, self.y, self.x + 10, self.y)
            self.ends = [(self.x - 10, self.y), (self.x + 10, self.y)]


    def get_ends(self):
        return [self.ends[0], self.ends[1]]
#################################################

global use_line
global ends
global use_ends

use_line = []
use_ends = set()
ends = []

root = Tk()
c = Canvas(root, width=1200, height=1200, bg="white")

lines = []
new_lines = []

lines.append(Line(600, 600, 1))
lines[0].draw_line()

use_ends |= set(lines[0].get_ends())
use_line = list(lines)

def start():
    global use_line
    global ends
    global use_ends


    for l in use_line:
        if l.dir:
            if ((l.x, l.y + 10) in use_ends):
                new_lines.append(Line(l.x, l.y + 10, not(l.dir)))
                new_lines[-1].draw_line()
                ends.extend(new_lines[-1].get_ends())
            if  ((l.x, l.y - 10) in use_ends):
                new_lines.append(Line(l.x, l.y - 10, not(l.dir)))
                new_lines[-1].draw_line()
                ends.extend(new_lines[-1].get_ends())
        else:
            if  ((l.x + 10, l.y) in use_ends):
                new_lines.append(Line(l.x + 10, l.y, not (l.dir)))
                new_lines[-1].draw_line()
                ends.extend(new_lines[-1].get_ends())
            if  ((l.x - 10, l.y) in use_ends):
                new_lines.append(Line(l.x - 10, l.y, not (l.dir)))
                new_lines[-1].draw_line()
                ends.extend(new_lines[-1].get_ends())

    use_ends.clear()
    for e in ends:
        if ends.count(e) != 2:
            use_ends.add(e)
    ends.clear()

    use_line.clear()
    use_line = new_lines.copy()
    new_lines.clear()

    root.after(50, start)

c.pack()
root.after(50, start)
root.mainloop()