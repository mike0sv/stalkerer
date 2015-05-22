import tkinter
from PIL import ImageTk, Image
import os, time
import pygame

girls = {}
for fold in os.listdir('./data'):
    if os.path.isdir('./data/' + fold):
        girls[fold] = []

for girl in girls:
    for file in os.listdir('./data/' + girl):
        if not os.path.isdir('./data/' + girl + '/' + file):
            girls[girl].append('./data/' + girl + '/' + file)
    if len(girls[girl]) == 0:
        girls[girl].append(None)


girl = 0
photo = 0
size_x, size_y = 800, 600
done = False

pygame.init()
window = pygame.display.set_mode((size_x, size_y))

img = pygame.image.load(girls[girls.keys()[girl]][photo]).convert()
upd = False
window.blit(img, (0, 0))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                girl = (girl - 1) % len(girls)
                photo = 0
                upd = True
            elif event.key == pygame.K_w:
                girl = (girl + 1) % len(girls)
                photo = 0
                upd = True
            elif event.key == pygame.K_a:
                photo = (photo + 1) % len(girls[girls.keys()[girl]])
                upd = True
            elif event.key == pygame.K_d:
                photo = (photo + 1) % len(girls[girls.keys()[girl]])
                upd = True

        if upd:
            print girl, photo, girls.keys()[girl]
            try:
                upd = False
                img = pygame.image.load(girls[girls.keys()[girl]][photo]).convert()
                window.blit(img, (0, 0))
            except Exception as e:
                print e


    pygame.display.update()

#img = tkinter.PhotoImage(file=girls[girls.keys()[girl]][photo])
