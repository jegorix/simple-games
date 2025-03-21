import pygame
import random



clock = pygame.time.Clock()

pygame.init()
w_width, w_height = 1280, 748


window_size = (w_width, w_height)
screen = pygame.display.set_mode(window_size)


label = pygame.font.Font('fonts/PTSerif-BoldItalic.ttf', 96)
quit_font = pygame.font.Font('fonts/PTSerif-BoldItalic.ttf', 64)



lose_label = label.render("You Lose!", True, (193, 196, 199))
restart_label = label.render("Restart", True, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft = ((w_width - restart_label.get_width()) // 2,
                                                       lose_label.get_height() + (restart_label.get_height() + 50)))


quit_label = quit_font.render('Quit', True, (255, 255, 255))
quit_label_rect = quit_label.get_rect(topleft = ((w_width - quit_label.get_width()) // 2,
                                    lose_label.get_height() + restart_label.get_height() + (quit_label.get_height() + 150)))


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


record = 0

ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_x = w_width + 10
ghost_y = 535
ghost_list_in_game = []
ghost_speed = 10




ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 1000)

bullet_timer = pygame.USEREVENT + 1
pygame.time.set_timer(bullet_timer, 5000)

# change ghost speed

fireball = pygame.image.load('images/fireball.png').convert_alpha()
fireball_list = []
fireball_count = 5
player_bullets = []




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
        record_text = score_font.render(f"Record: {record}", True, (255,255,255))
        bullet_text = score_font.render(f"Bullets: {fireball_count}", True, (255,255,255))
        screen.blit(score_text, (50, 50))
        screen.blit(record_text, (50, 100))
        screen.blit(bullet_text, (50, 150))

        if player_bullets:
            for i, bullet in enumerate(player_bullets):
                if len(player_bullets) > 3:
                    player_bullets.pop(i)


                screen.blit(fireball, bullet)
                if player_rect.colliderect(bullet):
                    fireball_count += 1
                    player_bullets.pop(i)



        if ghost_list_in_game:
            for i, elem in enumerate(ghost_list_in_game):
                screen.blit(ghost, elem)
                elem.x -= ghost_speed


                if elem.x == ghost.get_width() - 4:
                    fireball_count += 1
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

        # if keys[pygame.K_SPACE]:
        #     fireball_list.append(fireball.get_rect(topleft = (player_x + 35, player_y_pos + 13)))

        if fireball_list:
            for i, elem in enumerate(fireball_list):
                screen.blit(fireball, (elem.x, elem.y))
                elem.x += 10

                if elem.x > w_width:
                    fireball_list.pop(i)

                if ghost_list_in_game:
                    for j, ghost_elem in enumerate(ghost_list_in_game):
                        if elem.colliderect(ghost_elem):
                            score += 1
                            ghost_list_in_game.pop(j)
                            fireball_list.pop(i)

        if score > record:
            record = score





    else:
        screen.fill((87,88,89))
        screen.blit(lose_label, ((w_width - lose_label.get_width()) // 2,  lose_label.get_height()))
        screen.blit(restart_label, restart_label_rect)
        screen.blit(score_text, (50, 50))
        screen.blit(record_text, (50, 100))
        screen.blit(quit_label, quit_label_rect)


        mouse_pos = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            score = 0
            fireball_count = 5
            gameplay = True
            player_x = 150
            ghost_speed = 10
            ghost_list_in_game.clear()
            fireball_list.clear()
            player_bullets.clear()

        elif quit_label_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            running = False






    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft = (ghost_x, ghost_y)))

        if event.type == bullet_timer:
            player_bullets.append(fireball.get_rect(topleft=(random.randint(100, w_width - 100), w_height - 160)))
            ghost_speed += 5




        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and fireball_count > 0:
            fireball_list.append(fireball.get_rect(topleft=(player_x + 35, player_y_pos + 13)))
            fireball_count -= 1






    clock.tick(20)
