import pygame
from circleshape import *
from constants import *
import random



class Asteroid(CircleShape):
    def __init__ (self,x,y,radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

        random_angle = random.uniform(20,50)
        new_vel1 = self.velocity.rotate(random_angle)
        new_vel2 = self.velocity.rotate(-random_angle)

        radius_small_asteroids = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x,self.position.y,radius_small_asteroids)
        asteroid2 = Asteroid(self.position.x,self.position.y,radius_small_asteroids)

        new_vel1 *= 1.2
        new_vel2 *= 1.2

        asteroid1.velocity = new_vel1
        asteroid2.velocity = new_vel2