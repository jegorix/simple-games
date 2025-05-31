import tkinter as tk
import random

# game const
WIDTH = 400
HEIGHT = 400
CELL_SIZE = 10
DELAY = 100

# main window
root = tk.Tk()
root.title("Snake | Score: 0")
root.resizable(False, False)

# add game field
canvas = tk.Canvas(
    root, 
    width=WIDTH,
    height=HEIGHT,
    bg="black",
    highlightthickness=0
)
canvas.pack()


# initial state of the game
snake = [(100, 100), (90, 100), (80, 100)]
direction = 'Right'
DIRECTIONS = ["Up", "Down", "Left", "Right"]
food = None
score = 0
game_over = False


# create food
def create_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

food = create_food()

# draw food
def draw_food():
    canvas.create_rectangle(
        food[0], food[1],
        food[0] + CELL_SIZE,
        food[1] + CELL_SIZE,
        fill="red"
        
    )
    
    
# create game main cycle
def game_loop():
    global snake, food, score
    canvas.delete("all")
    draw_food()
    root.after(DELAY, game_loop)

draw_food()
root.after(DELAY, game_loop)



# execute main cycle
root.mainloop()