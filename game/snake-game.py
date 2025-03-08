import pygame
import random
import time

pygame.init()

window_size = (800, 600)
pygame.display.set_caption("Project")
screen = pygame.display.set_mode(window_size)
background_color = (0, 0, 0)
running = True

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

game_over_time = None


while running:
    screen.fill(background_color)

    if game_over_time:
        game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over_text, (window_size[0] // 2 - game_over_text.get_width() // 2,
        window_size[1] // 2 - game_over_text.get_height()))
        pygame.display.update()

        if time.time() - game_over_time > 2.5:
            running = False

        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y_pos - circle_radius > 0:
        y_pos -= speed

    if keys[pygame.K_s] and y_pos + circle_radius < window_size[1]:
        y_pos += speed

    if keys[pygame.K_a] and x_pos - circle_radius > 0:
        x_pos -= speed

    if keys[pygame.K_d] and x_pos + circle_radius < window_size[0]:
        x_pos += speed

    # if keys[pygame.K_SPACE]:
    #     score = 9


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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False