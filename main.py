import pygame
from constants import *
from player import * 
from asteroidfield import *
from circleshape import *
import sys

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	updatable  = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids  = pygame.sprite.Group()



	# Initialize pygame
	pygame.init()
	pygame.display.set_caption("Asteroids")
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)  # Note the comma to make it a tuple
	asteroid_field = AsteroidField()  # Create an instance
	player_object = Player(x,y)



	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	time_object = pygame.time.Clock()
	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		# Use RGB for black (no alpha)
		screen.fill((0, 0, 0))

		# Draw all drawable objects
		for drawable_object in drawable:
			drawable_object.draw(screen)
		
		tick_value = time_object.tick(60)
		dt = tick_value / 1000
		
		# Update all updatable objects
		updatable.update(dt)
		for asteroid in asteroids:
			if player_object.collision(asteroid):
				print("Game over!")
				pygame.quit()
				sys.exit()
		pygame.display.flip()



if __name__ == "__main__":
	main()
