import pygame
from circleshape import CircleShape


class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
               

    def draw(self, surface):
        #pygame.draw.circle: use position, radius, and width of 2
        pygame.draw.circle(surface, "white", (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt): 
       self.position += self.velocity * dt