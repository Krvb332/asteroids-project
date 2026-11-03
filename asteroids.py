import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
class Asteroid(CircleShape):
      def __init__(self, x: float, y: float, radius: float) -> None:
            super().__init__(x, y, radius)
      def draw(self, screen: pygame.Surface) :
            return pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
      
      def update(self,dt):
            self.position+=self.velocity*dt
      def split(self)->None:
            self.kill()
            if self.radius<=ASTEROID_MIN_RADIUS:
                  return
            else:
                  log_event("asteroid_split")
                  positive_roated_vector = self.velocity.rotate(random.uniform(20,50))
                  negative_rotated_vector = self.velocity.rotate(-random.uniform(20,50))
                  new_radius = self.radius - ASTEROID_MIN_RADIUS
                  asteroid_one = Asteroid(self.position.x,self.position.y,new_radius)
                  asteroid_one.velocity = positive_roated_vector * 1.2
                  asteroid_two = Asteroid(self.position.x,self.position.y,new_radius)
                  asteroid_two.velocity = negative_rotated_vector * 1.2
