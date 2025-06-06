import pygame
import random

ROWS, COLS = 20, 20
CELL_SIZE = 20

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

def draw_grid(screen, grid, cell_size):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            color = (255, 0, 0) if grid[i][j] else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, (50, 50, 50), (j * cell_size, i * cell_size, cell_size, cell_size), 1)
            
def set_value(grid, mouse_pos):
    x,y = mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE
    grid[y][x] = 1
    
def calculate_population(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
    return count
            
    
    

    
    
            
            
            
def main():
    pygame.init()
    screen = pygame.display.set_mode((ROWS*CELL_SIZE, COLS*CELL_SIZE))
    pygame.display.set_caption("Game Of Life")
    running = True
    grid = create_grid(ROWS, COLS)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                set_value(grid, mouse_pos)
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    grid = create_grid(ROWS, COLS)
                
        print(f"Population: {calculate_population(grid)}")
        
        draw_grid(screen, grid, CELL_SIZE)
        grid = next_generation(grid)
        pygame.time.delay(400)
        pygame.display.flip()
                

main()