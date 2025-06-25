import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    x=SCREEN_WIDTH/2
    y=SCREEN_HEIGHT/2
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player_character=Player(x, y)
    asteroid_field=AsteroidField()
    dt=16/1000
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None, special_flags=0)
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        for a in asteroids:
            if a.collide(player_character):
                print("Game over!")
                return pygame.QUIT
            for s in shots:
                if a.collide(s):
                    a.split()
                    pygame.sprite.Sprite.kill(s)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

