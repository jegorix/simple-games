import pygame

pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

square = pygame.Surface((50,170))
square.fill('Blue')


header_font = pygame.font.Font(None, 72)
header_text = header_font.render("Press SPACE to start", True, (255,255,255))

background_image = pygame.image.load('images/back.jpeg')


myfont = pygame.font.Font('fonts/PTSerif-BoldItalic.ttf', 40)
text_surface = myfont.render("Jegorix", False, (255,255,255))


running = True
while running:
    screen.blit(square, (0, 500 - square.get_height()))

    pygame.draw.circle(screen, 'Red', (252, 85), 10 )

    pygame.draw.rect(screen, "Green", (5, 5, 50, 50))

    screen.blit(text_surface, (300,100))

    screen.blit(background_image, (550, 200))

    screen.blit(header_text, ((window_size[0] - header_text.get_width()) // 2,
                              (window_size[1] - header_text.get_height()) // 2 ))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

