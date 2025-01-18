import pygame
import random
from circleshape import CircleShape
from constant import *

class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
               

    def draw(self, surface):
        #pygame.draw.circle: use position, radius, and width of 2
        pygame.draw.circle(surface, "white", (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt): 
       self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random.uniform(20, 50)