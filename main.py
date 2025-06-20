import pygame
from player import *
from constants import *
from asteroids import *
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delt_time = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updates = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updates, drawables)
    Asteroids.containers = (asteroids, updates, drawables)
    AsteroidField.containers = updates
    Shot.containers = (shots, updates, drawables)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          
        pygame.Surface.fill(screen, (0,0,0))
        dt = clock.tick(40) / 1000

        updates.update(dt)

        for asteroid in asteroids:
            if asteroid.crash(player):
                print("u crashed noob")
                return
            for shot in shots:
                if asteroid.crash(shot):
                    shot.kill()
                    asteroid.split()

        
        for drawable in drawables:
            drawable.draw(screen)
        

        pygame.display.flip()

        

if __name__ == "__main__":
    main()