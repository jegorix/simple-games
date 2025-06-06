import pygame
import random

from pygame import K_SPACE

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Range: Target Hunting")

clock = pygame.time.Clock()

running = True

class Target():
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)
        self.radius = 30
        self.color = (255, 0, 0)

    def draw_target(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.speed = 10
        self.color = (0, 255, 0)

    def move(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def is_hit(self, target):
        return target.rect.collidepoint(self.x, self.y)




targets = [Target() for _ in range(5)]
bullets = []




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()


    screen.fill((0, 0, 0))
    for target in targets:
        target.draw_target(screen)

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        bullets.append(Bullet(mouse_pos[0], mouse_pos[1]))

    if bullets:
        for bullet in bullets:
            bullet.draw(screen)
            while bullet.y < HEIGHT + bullet.radius:
                bullet.move()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()


