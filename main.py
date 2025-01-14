import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    clock = pygame.time.Clock()
    dt=0

    while True: 
        for event in pygame.event.get():
            #check if player has closed the window, makes close button work. 
            if event.type == pygame.QUIT:  
                return
        #player.update(dt)
        for player in updatable: 
            player.update(dt)
        screen.fill((0,0,0))
        #player.draw(screen)
        for player in drawable:
            player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
    

if __name__ == "__main__":
    main()
    pygame.quit()