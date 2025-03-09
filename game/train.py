import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

square = pygame.Surface((50,170))
square.fill('Blue')

background_image = pygame.image.load('images/back.jpeg')

myfont = pygame.font.Font('fonts/PTSerif-BoldItalic.ttf', 40)
text_surface = myfont.render("Jegorix", False, (255,255,255))


running = True
while running:
    screen.blit(square, (0, 500 - square.get_height()))

    pygame.draw.circle(screen, 'Red', (252, 85), 10 )

    screen.blit(text_surface, (300,100))

    screen.blit(background_image, (550, 200))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

