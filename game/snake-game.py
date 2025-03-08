import pygame

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)
# background_color = (0, 0, 0)
# screen.fill(background_color)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()