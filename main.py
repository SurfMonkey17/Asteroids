import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
   
    asteroid_field = AsteroidField()
    
    clock = pygame.time.Clock()  
    dt=0
   
    running = True
    while running: 
        for event in pygame.event.get():
            #check if player has closed the window, makes close button work. 
            if event.type == pygame.QUIT:  
                running = False
       
        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            player.collision(asteroid)
  
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.position.distance_to(shot.position) <= (asteroid.radius + shot.radius):
                    asteroid.split() 
                    shot.kill()
                    

        screen.fill((0,0,0)) 
        
        for sprite in drawable:  
            sprite.draw(screen)  
      
      
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
    pygame.quit()

if __name__ == "__main__":
    main()
   