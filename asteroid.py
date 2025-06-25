from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),self.position, self.radius, width=2)
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        asteroidchunk_radius= self.radius - ASTEROID_MIN_RADIUS
        asteroidchunk_one = Asteroid(self.position.x, self.position.y, asteroidchunk_radius)
        asteroidchunk_two = Asteroid(self.position.x, self.position.y, asteroidchunk_radius)
        asteroidchunk_one.velocity = self.velocity.rotate(random_angle)
        asteroidchunk_two.velocity = self.velocity.rotate(-random_angle)
        asteroidchunk_one.velocity = asteroidchunk_one.velocity * 1.2
        asteroidchunk_two.velocity = asteroidchunk_two.velocity * 1.2

    def update(self, dt):
        self.dt=dt
        self.position += self.velocity * dt