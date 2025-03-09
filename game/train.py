import pygame

pygame.init()
window_size = (1280, 748)
screen = pygame.display.set_mode(window_size)



background_image = pygame.image.load('images/bg.png')


def load_and_scale(image_path, size):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, size)


player_size = (60, 70)

walk_left = [
    load_and_scale('images/player-left/l_1.png', player_size),
    load_and_scale('images/player-left/l_2.png', player_size),
    load_and_scale('images/player-left/l_3.png', player_size),
    load_and_scale('images/player-left/l_4.png', player_size)
]

walk_right = [
    load_and_scale('images/player-right/r_1.png', player_size),
    load_and_scale('images/player-right/r_2.png', player_size),
    load_and_scale('images/player-right/r_3.png', player_size),
    load_and_scale('images/player-right/r_4.png', player_size)
]

player_anim_count = 0

running = True
while running:

    screen.blit(background_image, (0, 0))
    screen.blit(walk_right[player_anim_count],(300, 535))


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

