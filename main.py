import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_object = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

   # Create the Groups (the collections)
    drawables = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    # Create the Groups (the collections) for asteroids
    asteroids = pygame.sprite.Group()

    # Tell the Player class to automatically add new instances to these Groups
    Player.containers = (drawables, updatable)
    player_object = Player(x,y)

    # Asteroid container
    Asteroid.containers = (asteroids, updatable, drawables)  # Add to all relevant groups
    AsteroidField.containers = (updatable,)  # Only updatable, not drawable or in asteroids group

    asteroid_field = AsteroidField()

    #shot container and group
    shots = pygame.sprite.Group()
    Shot.containers = (shots,drawables, updatable)

    #shot_object = Shot(x,y)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0,0))

        
        for drawing in drawables:
            drawing.draw(screen)


        # tick method
        tick_method = time_object.tick(60)
        dt = tick_method / 1000
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player_object):
                print("Game Over")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                collided_shot = asteroid.collision_check(shot)
                if collided_shot:
                    asteroid.split()  # Remove the asteroid
                    shot.kill()  # Remove the shot
            

        pygame.display.flip()



if __name__ == "__main__":
    main()