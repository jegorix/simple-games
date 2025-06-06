import tkinter as tk
import pygame
import random
import sys
import os



# game const
WIDTH = 400
HEIGHT = 400
CELL_SIZE = 10
DELAY = 100
pygame.mixer.init()
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
sounds = {
    'apple': '/Users/macbook/PycharmProjects/snake-interface-1/snake/static/audio/apple.mp3',
    'collision': '/Users/macbook/PycharmProjects/snake-interface-1/snake/static/audio/crash.mp3',
    'game_over': '/Users/macbook/PycharmProjects/snake-interface-1/snake/static/audio/game_over.mp3',
    'game_start': '/Users/macbook/PycharmProjects/snake-interface-1/snake/static/audio/game_start.mp3',
}

audio_files = [
    'apple.mp3',
    'crash.mp3',
    'game_over.mp3',
    'game_start.mp3',
]
audio_paths = [os.path.join(BASE_DIR, "static", "audio", filename) for filename in audio_files]

# add audio effects
def play_sound(sound_file):    
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()



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




# create snake at random position
def create_snake():
    max_x = (WIDTH // CELL_SIZE) - 3
    max_y = (HEIGHT // CELL_SIZE) - 1
    
    x = random.randint(0, max_x) * CELL_SIZE
    y = random.randint(0, max_y) * CELL_SIZE
    
    return [(x,y), (x - CELL_SIZE, y), (x - CELL_SIZE * 2, y)]




# initial state of the game
snake = create_snake()
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
        
# game restart
def restart_game():
    global snake, direction, food, score, game_over
    
    snake = create_snake()
    direction = 'Right'
    food = create_food()
    score = 0
    game_over = False
    
    canvas.delete("all")
    draw_food()
    draw_snake()
    update_title()
    
    play_sound(sound_file=sounds['game_start'])
    root.after(DELAY, game_loop)
         
        
        
        
        
        

   
# keystroke handling
def on_key_press(event):
    global direction, game_over
    key = event.keysym
    if key in DIRECTIONS:
        if(key == 'Up' and direction != 'Down' or
           key == 'Down' and direction != 'Up' or
           key == 'Left' and direction != 'Right' or
           key == 'Right' and direction != 'Left'):
            direction = key
    elif key == 'space' and game_over:
        restart_game()
               
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
        play_sound(sounds['apple'])
        return True
    return False 
    
    
# wall collision</KeyPress>
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
        play_sound(sounds['collision'])
        # play_sound(sounds['game_over'])
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