import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

square = pygame.Surface((50,170))
square.fill('Blue')


running = True
while running:
    screen.blit(square, (0, 500 - square.get_height()))

    pygame.draw.circle(screen, 'Red', (200, 200), 40 )

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

