from tkinter import Tk,Canvas,PhotoImage,NW
import time
import math

tk=Tk()
canvas=Canvas(width=880,height=500,bg='black')
canvas.grid()
BGPic=PhotoImage(file='Background2.png')
MonkeyPic=PhotoImage(file='Monkey.png')
DartPic=PhotoImage(file='dart.png')
canvas.create_image(0,0,image=BGPic,anchor=NW)
monkey=canvas.create_image(810,147, image=MonkeyPic)
dart=canvas.create_image(180,300, image=DartPic)


canvas.pack()

Theta=math.atan((320-147)/(810-180))
V0=15
Vx=V0*math.cos(Theta)
Vy=-V0*math.sin(Theta)
Vym=0
g=.2
while True:
    canvas.move(monkey,0,Vym)
    canvas.move(dart,Vx,Vy)
    posM = canvas.coords(monkey)
    posD = canvas.coords(dart)
    Vym=Vym+g
    Vy=Vy+g
    if posM[1]>=400 :
        Vym=0
    if posD[0]>=posM[0]-55:
        Vym=0
        Vy=0
        Vx=0
    tk.update()
    time.sleep(0.025)
    pass

tk.mainloop()