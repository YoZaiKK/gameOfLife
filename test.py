import os
import pygame
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
 
x = []
y = []

run = True
root = tk.Tk()
screen = pygame.display.set_mode((500, 500))
screen.fill(pygame.Color(255, 255, 255))
pygame.display.init()
pygame.display.update()


def draw():
    pygame.draw.circle(screen, (0, 0, 0), (250, 250), 125)
    pygame.display.update()


def stop():
    pygame.quit()
    
def plot(plt, x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Lab DLS')
    plt.show()


button1 = Button(root, text='Draw',  command=draw)
button1.pack(side=LEFT)
buttonStop = Button(root, text='Stop', command=stop)
buttonStop.pack(side=RIGHT)
buttonPlot = Button(root, text='Plot', command=lambda:plot(plt, x, y))
buttonPlot.pack()
root.update()

example = 0

while run: 
    x.append(example*2) 
    y.append(example) 
    root.update()
    example += 1
