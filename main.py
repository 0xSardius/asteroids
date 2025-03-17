import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updateable  = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        # use screen's fill method to fill screen with a solid black color
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))

        # Update game state
        dt = clock.get_time() / 1000
        updateable.update(dt)

        # Draw everything
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)
    
    pygame.quit()
        
        


if __name__ == "__main__":
    main()
