import pygame
from circleshape import *
from constants import *
import random

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta):
        self.position += self.velocity * delta

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20, 50)
        velocity_p = self.velocity.rotate(new_angle)
        velocity_n = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_p = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid_p.velocity = velocity_p * 1.2

        asteroid_n = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid_n.velocity = velocity_n * 1.2
        