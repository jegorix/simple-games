import pygame

clock = pygame.time.Clock()

pygame.init()
w_width, w_height = 1280, 748


window_size = (w_width, w_height)
screen = pygame.display.set_mode(window_size)


label = pygame.font.Font('fonts/PTSerif-BoldItalic.ttf', 96)
lose_label = label.render("You Lose!", True, (193, 196, 199))
restart_label = label.render("Restart", True, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft = ((w_width - restart_label.get_width()) // 2,
                                                       lose_label.get_height() + (restart_label.get_height() + 50)))

background_image = pygame.image.load('images/bg.png').convert_alpha()


def load_and_scale(image_path, size):
    image = pygame.image.load(image_path).convert_alpha()
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

is_jump = False
jump_count = 12


score = 0
score_font = pygame.font.Font(None, 48)



ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_x = w_width + 10
ghost_y = 535
ghost_list_in_game = []


ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2000)

gameplay = True


running = True
while running:

    screen.blit(background_image, (bg_x, 0))
    screen.blit(background_image, (bg_x + w_width, 0))
    # screen.blit(ghost, (ghost_x, ghost_y))

    if gameplay:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y_pos))
        ghost_rect = ghost.get_rect(topleft = (ghost_x, ghost_y))

        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (50, 50))


        if ghost_list_in_game:
            for i, elem in enumerate(ghost_list_in_game):
                screen.blit(ghost, elem)
                elem.x -= 10


                if elem.x == ghost.get_width() - 4:
                    score += 1
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(elem):
                    gameplay = False
                    print("Connect!")

        screen.blit(walk_right[player_anim_count],(player_x, player_y_pos))



        if player_rect.colliderect(ghost_rect):
            print("Connect!")


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y_pos))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y_pos))


        if keys[pygame.K_RIGHT] and player_x < w_width - walk_right[player_anim_count].get_width() :
            player_x += player_speed

        elif keys[pygame.K_LEFT] and player_x > walk_right[player_anim_count].get_width():
            player_x -= player_speed


        if not is_jump:
            if keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -12:
                if jump_count >  0:
                    player_y_pos -= (jump_count ** 2) // 2
                else:
                    player_y_pos += (jump_count ** 2) // 2

                jump_count -= 2

            else:
                is_jump = False
                jump_count = 12







        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 5

        if bg_x == -w_width:
            bg_x = 0

    else:
        screen.fill((87,88,89))
        screen.blit(lose_label, ((w_width - lose_label.get_width()) // 2,  lose_label.get_height()))
        screen.blit(restart_label, restart_label_rect)
        screen.blit(score_text, (50, 50))

        mouse_pos = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            score = 0
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()







    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft = (ghost_x, ghost_y)))





    clock.tick(20)
