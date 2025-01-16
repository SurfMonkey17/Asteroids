import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        self.velocity = pygame.Vector2()


    def draw(self, surface):
            pygame.draw.circle(surface, "white", (self.position.x, self.position.y), self.radius)

    def update(self, dt): 
       self.position += self.velocity * dt