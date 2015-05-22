import tkinter
from PIL import ImageTk, Image
import os


girls = {}
for fold in os.listdir('./data'):
    if os.path.isdir('./data/' + fold):
        girls[fold] = []

for girl in girls:
    for file in os.listdir('./data/' + girl):
        if not os.path.isdir('./data/' + girl + '/' + file):
            girls[girl].append('./data/' + girl + '/' + file)


girl = 0
photo = 0


tk = tkinter.Tk()
can = tkinter.Canvas(tk)
can.pack()
img = Image.open(girls[girls.keys()[girl]][photo])
img = ImageTk.PhotoImage(img)
#img = tkinter.PhotoImage(file=girls[girls.keys()[girl]][photo])
can.create_image((100, 100), img)
