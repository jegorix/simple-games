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
x_pos = (window_size[0] - rect_size[0]) / 2
y_pos = (window_size[1] - rect_size[1]) / 2

while running:
    screen.fill(background_color)
    pygame.draw.rect(screen, rect_color, (x_pos, y_pos, rect_size[0], rect_size[1]))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False