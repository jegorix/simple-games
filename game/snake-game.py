import pygame
import random
import time

pygame.init()

window_size = (800, 600)
pygame.display.set_caption("Project")
screen = pygame.display.set_mode(window_size)
background_color = (0, 0, 0)
running = True
paused = False

# background_image = pygame.image.load('images/back.jpeg')
# background_image = pygame.transform.scale(background_image, window_size)
# screen.blit(background_image, (0, 0))
circle_radius = 20
circle_color = (255, 0, 0)
x_pos = window_size[0] // 2
y_pos = window_size[1] - circle_radius
speed = 1

rect_height = 50
rect_width = 50
rect_color = (0, 0, 255)
rect_x = random.randint(0, window_size[0] - rect_width)
rect_y = -rect_height
rect_speed = 0.5


score = 0


font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 48)

game_over_time = None

def draw_button(text, x, y, width, height):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (200, 200, 200), button_rect, border_radius=10)
    text_render = button_font.render(text, True, (0, 0, 0))
    text_x = x + (width - text_render.get_width()) / 2
    text_y = y + (height - text_render.get_height()) / 2
    screen.blit(text_render, (text_x, text_y))
    return button_rect


def start_menu():
    screen.fill(background_color)
    title_text = button_font.render("WELCOME TO THE GAME", True, (255, 255, 255))
    screen.blit(title_text, ((window_size[0] - title_text.get_width()) / 2, 200))
    start_button = draw_button("START", (window_size[0] - 200) // 2, window_size[1] // 2,
                                200, 100)

    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                waiting = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    waiting = False


start_menu()


def game_over_menu():
    screen.fill(background_color)

    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (window_size[0] // 2 - game_over_text.get_width() // 2, 50))

    play_again_button = draw_button("PLAY AGAIN", (window_size[0] - 200) / 2, 200,
                                    200, 100)
    exit_button = draw_button("EXIT", (window_size[0] - 200) // 2, 400,
                              200, 100)

    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                waiting = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                  waiting = False
                  return True

                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    waiting = False



while running:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if paused:
        pause_text = game_over_font.render("PAUSE", True, (255, 255, 255))
        screen.blit(pause_text, ((window_size[0] - pause_text.get_width()) // 2,
                                 (window_size[1] - pause_text.get_height()) // 2))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text,(window_size[0] // 2 - score_text.get_width() // 2, 400))

        pygame.display.update()
        continue

    if game_over_time:
        pygame.time.wait(1500)
        if game_over_menu():
            score = 0
            rect_y = -rect_height
            rect_x = random.randint(0, window_size[0] - rect_width)
            game_over_time = None
            x_pos = window_size[0] // 2
            y_pos = window_size[1] - circle_radius

        else:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y_pos - circle_radius > 0:
        y_pos -= speed

    if keys[pygame.K_s] and y_pos + circle_radius < window_size[1]:
        y_pos += speed

    if keys[pygame.K_a] and x_pos - circle_radius > 0:
        x_pos -= speed

    if keys[pygame.K_d] and x_pos + circle_radius < window_size[0]:
        x_pos += speed

    if keys[pygame.K_k]:
        score += 1



    rect_y += rect_speed
    if rect_y > window_size[1]:
        rect_y = -rect_height
        rect_x = random.randint(0, window_size[0] - rect_width)
        score = 0


    if(x_pos - circle_radius < rect_x + rect_width and
    x_pos + circle_radius > rect_x and
    y_pos - circle_radius < rect_y + rect_height and
    y_pos + circle_radius > rect_y):
        rect_y = -rect_height
        rect_x = random.randint(0, window_size[0] - rect_width)
        score += 1



    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.circle(screen, circle_color, (x_pos, y_pos), circle_radius)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if score >= 10 and game_over_time is None:
        game_over_time = time.time()



    pygame.display.update()
