import pygame

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)
background_color = (0, 0, 0)
screen.fill(background_color)
running = True

background_image = pygame.image.load('images/back.jpeg')
background_image = pygame.transform.scale(background_image, window_size)
screen.blit(background_image, (0, 0))


while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False