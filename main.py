import math
import pygame
import numpy as np
from tkinter import *
from color_picker import pick_color
import matplotlib.pyplot as plt

pauseExect = True
toroide = True
# run = True
running = True
# colors
bg_color = 0, 0, 0
cell_color = 255, 255, 255

cell_counting = 0
cell_array_x = [0.0]
cell_array_x_log = [0.0]
cell_generation = 0
cell_gen_y = [0.0]
# --------------------------------


# # Buttons and functions
# ---Functions


def draw(opcion):
    global cell_color, bg_color, bg_color
    if opcion == 'celula':
        cell_color = pick_color(root)
    if opcion == 'Bg':
        bg_color = pick_color(root)


def stop():
    global pauseExect
    pauseExect = not pauseExect


def toro():
    global toroide, etiqToro
    toroide = not toroide
    etiqToro.config(text="Si" if toroide else "No")


def plot(plt, cell_array_x, cell_gen_y, cell_array_x_log):
    plt.plot(cell_gen_y, cell_array_x, ":", color='r', label='normal')
    plt.plot(cell_gen_y, cell_array_x_log, ":", color='g', label='log_10')
    plt.xlabel('generacion')
    plt.ylabel('poblacion')
    plt.title('Grafica de poblacion')
    plt.legend()
    plt.show()


root = Tk()
# root.geometry("200x100")
root.wm_title("Opciones")
cell_counting_tk = 0.0
# Et de numero de celulas vivas
etiqGeneracionText = Label(root, text='Iteracion: ')
etiqGeneracion = Label(root, text=cell_counting_tk, foreground="yellow",
                       background="black", borderwidth=5, anchor="w", width=15)
etiqGeneracionText.grid(row=0, column=0)
etiqGeneracion.grid(row=0, column=1)
# Et de generaciones
etiqPoblacionText = Label(root, text='Poblacion: ')
etiqPoblacion = Label(root, text=cell_counting_tk, foreground="yellow",
                      background="black", borderwidth=5, anchor="w", width=15)
etiqPoblacionText.grid(row=1, column=0)
etiqPoblacion.grid(row=1, column=1)
# btn para el color de la celula
buttonCellColor = Button(root, text='Cell color',
                         command=lambda: draw('celula'))
buttonCellColor.grid(row=2, column=0, sticky='nesw')

# btn para el color del bg
buttonBgColor = Button(root, text='Bg color',  command=lambda: draw('Bg'))
buttonBgColor.grid(row=2, column=1, sticky='nesw')

# btn para detener y continuar animacion
buttonStop = Button(root, text='Stop / Go', command=stop,
                    bg='black', fg='yellow', relief='raised')
buttonStop.grid(row=3, columnspan=2, column=0, sticky='nesw')

# btn para lanzar el plot
buttonPlot = Button(root, text='Ver grafica', command=lambda: plot(
    plt, cell_array_x, cell_gen_y, cell_array_x_log
))
buttonPlot.grid(row=4, columnspan=2, column=0, sticky='nesw')

# btn para cambiar de toroide a no toroide
buttonToro = Button(root, text='Toroide', command=toro)
buttonToro.grid(row=5, column=0, sticky='nesw')

# Et de numero de celulas vivas
etiqToro = Label(root, text="Si" if toroide else "No", foreground="yellow",
                 background="black", borderwidth=5, anchor="w", width=15)
etiqToro.grid(row=5, column=1)

# root update
root.update()

# # Valores iniciales y de configuracion del pygame
width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))
screen.fill(pygame.Color(255, 255, 255))
screen.fill(bg_color)

pygame.display.init()
pygame.display.update()

# rows and colls
# 100 x 100 matrix
num_cells_x, num_cells_y = 250, 250
# tamanio de pixeles
dimention_cell_width = width/num_cells_x
dimention_cell_height = height/num_cells_y

#  Cell state matrix
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
        (system_state[(x+1), (y+1)] if x <
         (num_cells_x-1) and y < (num_cells_y-1) else 0)
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
    cell_counting = 0
    # copy
    new_system = np.copy(system_state)
    # recolor
    screen.fill(bg_color)
    event_handler(pygame.event.get())

    for y in range(0, num_cells_x):
        for x in range(0, num_cells_y):
            # check for pause
            if not pauseExect:
                total = sum_of_neighbors_t(
                    x, y) if toroide else sum_of_neighbors(x, y)
                # Rules <<<<<
                # death cell with 3 neighbors comes to life
                if system_state[x, y] == 0:
                    new_system[x, y] = 1 if total == 3 else 0
                    # alive cell deads with neighbors > 3 (overpopulation) or neighbors < 2 (lonelyness?)
                elif system_state[x, y] == 1:
                    new_system[x, y] = 1 if total == 3 or total == 2 else 0

            # each square
            h = (x)*dimention_cell_width
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
                cell_counting += 1
                pygame.draw.polygon(screen, cell_color, polygon, 0)
    # Solo actualizamos los datos del matplot y del tk si no esta en pausa
    if not pauseExect:
        etiqPoblacion.config(text=cell_counting)
        etiqGeneracion.config(text=cell_generation)
        cell_array_x.append(cell_counting)
        cell_array_x_log.append(math.log10(cell_counting))
        cell_gen_y.append(cell_generation)
        cell_generation += 1

    # state update
    system_state = np.copy(new_system)
    pygame.display.update()
    root.update()
