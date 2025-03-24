# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants as cons
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x=cons.SCREEN_WIDTH / 2, y=cons.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        updatable.update(dt)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
