from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame

class Player(CircleShape) :
    def __init__(self, x, y) :
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dr):
        self.rotation += PLAYER_TURN_SPEED * dr
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(1)

        if keys[pygame.K_d]:
            self.rotate(-1)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.timer = PLAYER_SHOOT_COOLDOWN
            return self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, 2)
        shot.velocity = forward * 400
        return shot
    
    