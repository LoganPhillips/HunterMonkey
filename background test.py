from tkinter import Tk,Canvas,PhotoImage,NW
from PIL import Image,ImageTk
root=Tk()

canvas=Canvas(width=880,height=500,bg='black')
canvas.pack()

photo=PhotoImage(file='Background2.png')
DartPic=Image.open('dart.png')
canvas.create_image(0,0,image=photo,anchor=NW)
#dart=canvas.create_image(400,300, image=DartPic)

root.mainloop()