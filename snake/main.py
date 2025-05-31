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
    
    
    
# draw snake func
def draw_snake():
    for segment in snake:
        canvas.create_rectangle(
            segment[0], segment[1],
            segment[0] + CELL_SIZE, segment[1] + CELL_SIZE,
            fill="green",
            outline="darkgreen",     
        )

   
# keystroke handling
def on_key_press(event):
    global direction
    key = event.keysym
    if key in DIRECTIONS:
        if(key == 'Up' and direction != 'Down' or
           key == 'Down' and direction != 'Up' or
           key == 'Left' and direction != 'Right' or
           key == 'Right' and direction != 'Left'):
            direction = key
root.bind("<KeyPress>", on_key_press)



# move snake forward
def move_snake():
    head_x, head_y = snake[0]
    
    if direction == 'Up':
        new_head = (head_x, head_y - CELL_SIZE)
    elif direction == 'Down':
        new_head = (head_x, head_y + CELL_SIZE)
    elif direction == 'Left':
        new_head = (head_x - CELL_SIZE, head_y)
    elif direction == 'Right':
        new_head = (head_x + CELL_SIZE, head_y)
        
    snake.insert(0, new_head)
    
    if not check_food_colision():
        snake.pop()
        
        
# update score
def update_title():
    root.title(f"Snake | Score: {score}")
    
# check eating food
def check_food_colision():
    global score, food
    if snake[0] == food:
        score += 1
        food = create_food()
        return True
    return False 
    
    
# wall collision
def check_wall_collision():
    head_x, head_y = snake[0]
    return(
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT
    )
    
# self collision
def check_self_collision():
    return snake[0] in snake[1:]
    
    
# game finish
def end_game():
    global game_over
    game_over = True
    canvas.create_text(
        WIDTH // 2, HEIGHT // 2,
        text=f"Game over! Score: {score}",
        fill="white",
        font=("Arial", 24)
    )   
    
    
    
# create game main cycle
def game_loop():
    global snake, food, score
    move_snake()
    
    if game_over:
        return
    
    if check_wall_collision() or check_self_collision():
        end_game()
        return
    
    canvas.delete("all")
    draw_food()
    draw_snake()
    update_title()
    root.after(DELAY, game_loop)

draw_food()
draw_snake()
root.after(DELAY, game_loop)



# execute main cycle
root.mainloop()