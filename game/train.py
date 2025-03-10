import pygame

clock = pygame.time.Clock()

pygame.init()
w_width, w_height = 1280, 748


window_size = (w_width, w_height)
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

bg_x = 0

# bg_sound = pygame.mixer.Sound('sounds/sad-sound.mp3')
# bg_sound.play()

player_speed = 10
player_x = 150
player_y_pos = 535


running = True
while running:

    screen.blit(background_image, (bg_x, 0))
    screen.blit(background_image, (bg_x + w_width, 0))


    screen.blit(walk_right[player_anim_count],(player_x, player_y_pos))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y_pos))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y_pos))


    if keys[pygame.K_RIGHT] and player_x < w_width - walk_right[player_anim_count].get_width() :
        player_x += player_speed

    elif keys[pygame.K_LEFT] and player_x > walk_right[player_anim_count].get_width():
        player_x -= player_speed


    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 5

    if bg_x == -w_width:
        bg_x = 0


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    clock.tick(10)
