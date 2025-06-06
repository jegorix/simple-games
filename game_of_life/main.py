import pygame
import random

ROWS, COLS = 20, 20

def create_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = [1 if random.random() < 0.3 else 0 for _ in range(cols)]
        grid.append(row)
    return grid
            


def show_grid(field):
    print()
    for min_field in field:
        print(min_field)





def count_live_neighbors(grid, row, col):
    alive = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j]:
                        alive += 1
    return alive


def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors_alive = count_live_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if neighbors_alive in (2,3):
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            else:
                if neighbors_alive == 3:
                    new_grid[i][j] = 1
    return new_grid

game_grid = create_grid(ROWS, COLS)
show_grid(game_grid)
game_grid = next_generation(game_grid)
show_grid(game_grid)