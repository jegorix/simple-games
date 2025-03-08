import pygame

pygame.init()

window_size = (800, 600)
pygame.display.set_caption("Project")
screen = pygame.display.set_mode(window_size)
background_color = (0, 0, 0)
running = True

# background_image = pygame.image.load('images/back.jpeg')
# background_image = pygame.transform.scale(background_image, window_size)
# screen.blit(background_image, (0, 0))
rect_size = (100, 100)
rect_color = (255, 255, 255)
circle_radius = 20
circle_color = (255, 0, 0)
x_pos = int((window_size[0] - rect_size[0]) / 2)
y_pos = int((window_size[1] - rect_size[1]) / 2)
# x_pos = 0
# y_pos = 0
speed = 1

while running:
    screen.fill(background_color)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y_pos - circle_radius > 0:
        y_pos -= speed

    if keys[pygame.K_DOWN] and y_pos + circle_radius < 600:
        y_pos += speed

    if keys[pygame.K_LEFT] and x_pos - circle_radius > 0:
        x_pos -= speed

    if keys[pygame.K_RIGHT] and x_pos + circle_radius < 800:
        x_pos += speed




    pygame.draw.circle(screen, circle_color, (x_pos, y_pos), circle_radius)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False