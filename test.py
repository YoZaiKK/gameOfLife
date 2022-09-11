import os
import pygame
import tkinter as tk
from tkinter import *
run = True
root = tk.Tk() 
screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(255,255,255))
pygame.display.init()
pygame.display.update()

def draw():
    pygame.draw.circle(screen, (0,0,0), (250,250), 125)
    pygame.display.update() 
button1 = Button(root,text = 'Draw',  command=draw)
button1.pack(side=LEFT)
buttonStop = Button(root,text = 'Stop')
buttonStop.pack(side=RIGHT)
root.update()

while run:
    pygame.display.update()
    root.update()
