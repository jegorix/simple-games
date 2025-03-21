import pygame
import random
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

    def draw_target(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


targets = [Target() for _ in range(5)]




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0))
    for target in targets:
        target.draw_target()



    pygame.display.flip()
    clock.tick(60)

pygame.quit()


