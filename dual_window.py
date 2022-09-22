import os
import pygame
import numpy as np
import tkinter as tk
from tkinter import *
from color_picker import pick_color

pauseExect = True
toroide = True
running = True
# colors   
bg_color = 0, 0, 0  
cell_color = 255, 255, 255
# --------------------------------


# run = True
root = tk.Tk() 

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))
screen.fill(pygame.Color(255,255,255))
screen.fill(bg_color)

pygame.display.init()

# rows and colls
# 100 x 100 matrix
num_cells_x, num_cells_y = 250, 250

dimention_cell_width = width/num_cells_x
dimention_cell_height = height/num_cells_y

#  Cell state

system_state = np.zeros((num_cells_x, num_cells_y))


# no toroide
def sum_of_neighbors(x, y):
    total = (
        (system_state[(x-1), (y-1)] if x > 0 or y > 0 else 0) +
        (system_state[(x), (y-1)] if y > 0 else 0) +
        (system_state[(x+1), (y-1)] if x < (num_cells_x-1) and y > 0 else 0) +
        (system_state[(x-1), (y)] if x > 0 else 0) +
        # system_state[(x) , (y)] <- the one being analized
        (system_state[(x+1), (y)] if x < (num_cells_x-1) else 0) +
        (system_state[(x-1), (y+1)] if x > 0 and y < (num_cells_y-1) else 0) +
        (system_state[(x), (y+1)] if y < (num_cells_y-1) else 0) +
        (system_state[(x+1), (y+1)] if x < (num_cells_x-1) and y < (num_cells_y-1) else 0)
    )
    return total

# toroide
def sum_of_neighbors_t(x, y):
    total = (
        (system_state[(x-1) % num_cells_x, (y-1) % num_cells_y]) +
        system_state[(x) % num_cells_x, (y-1) % num_cells_y] +
        system_state[(x+1) % num_cells_x, (y-1) % num_cells_y] +
        system_state[(x-1) % num_cells_x, (y) % num_cells_y] +
        # system_state[(x) , (y)] <- the one being analized
        system_state[(x+1) % num_cells_x, (y) % num_cells_y] +
        system_state[(x-1) % num_cells_x, (y+1) % num_cells_y] +
        system_state[(x) % num_cells_x, (y+1) % num_cells_y] +
        system_state[(x+1) % num_cells_x, (y+1) % num_cells_y]
    )
    return total


# # automata palo
# system_state[5, 3] = 1
# system_state[5, 4] = 1
# system_state[5, 5] = 1
# # automata movil
# system_state[21, 21] = 1
# system_state[22, 22] = 1
# system_state[22, 23] = 1
# system_state[21, 23] = 1
# system_state[20, 23] = 1

# system_state[98, 99] = 1
# system_state[97, 99] = 1
# system_state[96, 99] = 1
# system_state[98, 98] = 1
# system_state[97, 97] = 1


system_state[50, 50] = 1
system_state[51, 50] = 1
system_state[51, 48] = 1
system_state[53, 49] = 1
system_state[54, 50] = 1
system_state[55, 50] = 1
system_state[56, 50] = 1

system_state[50+60, 50+100] = 1
system_state[51+60, 50+100] = 1
system_state[51+60, 48+100] = 1
system_state[53+60, 49+100] = 1
system_state[54+60, 50+100] = 1
system_state[55+60, 50+100] = 1
system_state[56+60, 50+100] = 1

def draw(opcion):
    global cell_color, bg_color, bg_color
    if opcion == 'celula':
        cell_color = pick_color(root) 
    if opcion == 'Bg':
        bg_color = pick_color(root)   
def stop():
    global pauseExect
    pauseExect = not pauseExect
    
button1 = Button(root,text = 'Cell color',  command=lambda:draw('celula'))
button1.pack(side=LEFT)
button1 = Button(root,text = 'Bg color',  command=lambda:draw('Bg'))
button1.pack(side=LEFT)
buttonStop = Button(root,text = 'Stop/Play', command = stop)
buttonStop.pack(side=RIGHT)

pygame.display.update()
root.update()

def event_handler(es):
    global running, pauseExect
    for e in es:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                pauseExect = True if not pauseExect else False 
        # Get cursor pos and draw        
        mouse_click = pygame.mouse.get_pressed(3)
        if mouse_click[0] or mouse_click[1] or mouse_click[2]:
            pos_x, pos_y = pygame.mouse.get_pos()
            new_cell_x = int(pos_x/dimention_cell_width)
            new_cell_y = int(pos_y/dimention_cell_height)
            # Draw with r_click and erase with l_click
            new_system[new_cell_x, new_cell_y] = not mouse_click[2]

while running:
    # copy
    new_system = np.copy(system_state)
    # recolor  
    screen.fill(bg_color) 
    event_handler(pygame.event.get())
    
    for y in range(0, num_cells_x):
        for x in range(0, num_cells_y):
            # check for pause
            if not pauseExect: 
                total = sum_of_neighbors_t(x, y) if toroide else sum_of_neighbors(x, y) 
                # Rules <<<<<
                    # death cell with 3 neighbors comes to life
                if system_state[x, y] == 0:
                    new_system[x, y] = 1 if total == 3 else 0
                    # alive cell deads with neighbors > 3 (overpopulation) or neighbors < 2 (lonelyness?)
                elif system_state[x, y] == 1:
                    new_system[x, y] = 1 if total == 3 or total == 2 else 0 
                    
            # each square
            h= (x)*dimention_cell_width
            h1 = (x+1)*dimention_cell_width
            w = (y)*dimention_cell_height
            w1 = (y+1)*dimention_cell_height
            polygon = [
                (h, w),
                (h1, w),
                (h1, w1),
                (h, w1)
            ]

            # polygon drawing 
            if new_system[x, y] == 1:
                pygame.draw.polygon(screen,cell_color, polygon, 0) 
    # state update
    system_state = np.copy(new_system) 
    pygame.display.update()
    root.update()