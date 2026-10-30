import pygame
<<<<<<< HEAD
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 
pygame.init()
=======

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
>>>>>>> refs/remotes/origin/main
from logger import log_state


def main() -> None:
    print(f"Starting Asteroids with pygame version{pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
<<<<<<< HEAD
    clock:object = pygame.time.Clock()
    dt:float = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()

=======
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
>>>>>>> refs/remotes/origin/main
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
<<<<<<< HEAD
        dt = clock.tick(60) / 1000
=======
>>>>>>> refs/remotes/origin/main
if __name__ == "__main__":
    main()


