import math
from tkinter import *

root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
drBtn = Button(text="Направление")
spLabel = Label(text="Скорость  1-100")
spEntry = Entry()
spEntry.insert(1, "50")
spBtn = Button(text="Поменять скорость")

cirlce = c.create_oval(100, 100, 500, 500, fill='red')  # 400 - диаметр. (300;300) - центр окружности
ball = c.create_oval(70, 300, 100, 330, fill='green')

drball = 1  # направление
speed = 10

def move(angle, rad, drt):
    if angle >= 360:
        angle = 0
    x = (200 + rad) * math.cos(math.radians(angle))  # 200 - радиус
    y = (200 + rad) * math.sin(math.radians(drball * angle))  # направление (+angle; -angle)
    angle += 1
    if  70 > rad >= -71 and not drt:
        rad += 1
    elif -70 < rad <= 69:
        rad -= 1
    else:
        rad -= 1
        drt = not drt
    print(rad)
    c.coords(ball, 285 + x, 285 + y, 315 + x, 315 + y)  # (300;300) - центр точки. 285;315 - ее границы
    root.after(int(speed), move, angle, rad, drt)  # скорость


def direc(event):  # направление
    global drball
    drball = drball * (-1)


def chspeed(event):
    global speed
    new_sp = spEntry.get()
    try:
        if 1 <= int(new_sp) <= 100:
            speed = 20 - int(new_sp) / 5
            if speed < 1:
                speed = 1
            spEntry.delete(0, END)
            spEntry.insert(1, new_sp)
        else:
            spEntry.delete(0, END)
            spEntry.insert(1, "Неверная скорость")
    except:
        spEntry.delete(0, END)
        spEntry.insert(1, "Неверная скорость")


drBtn.bind('<Button-1>', direc)
spBtn.bind('<Button-1>', chspeed)

c.pack()
drBtn.pack()
spLabel.pack()
spEntry.pack()
spBtn.pack()

root.after(10, move, 0, 0, 0)
root.mainloop()