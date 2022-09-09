import numpy as np
import pygame
import time
# pygame init hah
pygame.init()

toroide = True
pauseExect = False

# display config
width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

# colors
bg_color = 25, 25, 25  # bg_color
cell_color = 0, 0, 0  # cell
white_color = 255, 255, 255

screen.fill(bg_color)

# rows and colls
# 100 x 100 matrix
num_cells_x, num_cells_y = 50, 50

dimention_cell_width = width/num_cells_x
dimention_cell_height = height/num_cells_y

#  Cell state

system_state = np.zeros((num_cells_x, num_cells_y))


# not toroide
def sum_of_neighbors(x, y):
    total = (
        system_state[(x-1), (y-1)] +
        system_state[(x), (y-1)] +
        system_state[(x+1), (y-1)] +
        system_state[(x-1), (y)] +
        # system_state[(x) , (y)] <- the one being analized
        system_state[(x+1), (y)] +
        system_state[(x-1), (y+1)] +
        system_state[(x), (+-1)] +
        system_state[(x+1), (y+1)]
    )
    return total


# toroide
def sum_of_neighbors_t(x, y):
    total = (
        system_state[(x-1) % num_cells_x, (y-1) % num_cells_y] +
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


# automata palo
system_state[5, 3] = 1
system_state[5, 4] = 1
system_state[5, 5] = 1
# automata movil
system_state[21, 21] = 1
system_state[22, 22] = 1
system_state[22, 23] = 1
system_state[21, 23] = 1
system_state[20, 23] = 1

# inf loop
while True:
    # copy
    new_system = np.copy(system_state)
    # recolor and wait between iterations
    screen.fill(bg_color)
    time.sleep(0.1)

    # event handler
    events = pygame.event.get()

    for e in events:
        if e.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        mouse_click = pygame.mouse.get_pressed(3)
        if mouse_click[0] or mouse_click[1] or mouse_click[2]:
            pos_x, pos_y = pygame.mouse.get_pos()
            new_cell_x = int(np.floor(pos_x/dimention_cell_width))
            new_cell_y = int(np.floor(pos_y/dimention_cell_height))
            new_system[new_cell_x,new_cell_y] = not mouse_click[2]

    for y in range(0, num_cells_x):
        for x in range(0, num_cells_y):
            # chech for pause
            if not pauseExect:
                # sum of neighbors
                if toroide:
                    total = sum_of_neighbors_t(x, y)
                else:
                    total = sum_of_neighbors(x, y)
                # Rules <<<<<
                    # death cell with 3 neighbors comes to life
                if system_state[x, y] == 0 and total == 3:
                    new_system[x, y] = 1
                    # alive cell deads with neighbors > 3 (overpopulation) or neighbors < 2 (lonelyness?)
                if system_state[x, y] == 1 and (total > 3 or total < 2):
                    new_system[x, y] = 0

            polygon = [
                ((x)*dimention_cell_width, (y)*dimention_cell_height),
                ((x+1)*dimention_cell_width, (y)*dimention_cell_height),
                ((x+1)*dimention_cell_width, (y+1)*dimention_cell_height),
                ((x)*dimention_cell_width, (y+1)*dimention_cell_height),
            ]

            # polygon drawing
            if new_system[x, y] == 0:
                pygame.draw.polygon(screen, cell_color, polygon, 1)
            else:
                pygame.draw.polygon(screen, white_color, polygon, 0)

    # state update
    system_state = np.copy(new_system)

    # display
    pygame.display.flip()
