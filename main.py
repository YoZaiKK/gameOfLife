import numpy as np
import pygame
# pygame init hah
pygame.init()

toroide = True

# display config
width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

# colors
bg_color = 25, 25, 25  # bg_color
cell_color = 128, 128, 128  # cell
white_color = 255, 255, 255 

screen.fill(bg_color)

# rows and colls
# 25x25 matrix
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


# inf loop
while True:
    
    new_system = np.copy(system_state)
    
    for y in range(0, num_cells_x):
        for x in range(0, num_cells_y):

            # sum of neighbors
            if toroide:
                total = sum_of_neighbors(x, y)
            else:
                total = sum_of_neighbors_t(x, y)
                
            # Rules <<<<<
                # death cell with 3 neighbors comes to life
            if system_state[x,y] == 0 and total == 3:
                new_system[x,y] = 1
                # alive cell deads with neighbors > 3 (overpopulation) or neighbors < 2 (lonelyness?)
            if system_state[x,y] == 1 and (total > 3 or total < 2):
                new_system[x,y] = 0
            
            polygon = [
                ((x)*dimention_cell_width, (y)*dimention_cell_height),
                ((x+1)*dimention_cell_width, (y)*dimention_cell_height),
                ((x+1)*dimention_cell_width, (y+1)*dimention_cell_height),
                ((x)*dimention_cell_width, (y+1)*dimention_cell_height),
            ]
            
            # polygon drawing
            if new_system[x,y] == 0:
                pygame.draw.polygon(screen, cell_color, polygon, 1)
            else:
                pygame.draw.polygon(screen, white_color, polygon, 0)
                
    # state update
    system_state = np.copy(new_system)
    
    # display
    pygame.display.flip()
