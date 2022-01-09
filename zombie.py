import pygame
import math
import random

class Zombie():
    def __init__(self,x,y,width,height,player,zombies,bullets, radius = 10,health = 1,speed=1, color = (0,0,255)):
        self.player = player
        self.zombies = zombies
        self.bullets = bullets

        # -- zombie stats --
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius
        self.color = color
        self.speed = speed
        self.health = health
    
    def run(self, surface):
        self.draw(surface)
        self.move()
        self.collide()
    
    def collide(self):
        for zombie in self.zombies:
            index = self.zombie.collidelist(self.bullets)
            if index:
                print("hit")
            else:
                pass
    
    def draw(self, surface):
        if self.health > 0:
            self.zombieRect = pygame.Rect(self.x, self.y, self.width,self.height)
            self.zombie = pygame.draw.rect(surface,self.color, self.zombieRect)
    
    def move(self):
        #define target , distance and angle . Then get the moveX and Move Y
        self.targetX,self.targetY = self.player.x, self.player.y
        self.distanceX,self.distanceY = self.targetX - self.x,self.targetY - self.y
        self.angle = math.atan2(self.distanceX,self.distanceY)
        self.moveX,self.moveY = math.sin(self.angle) * self.speed,math.cos(self.angle) * self.speed

        #move
        self.x += self.moveX * self.speed
        self.y += self.moveY * self.speed
    
    def __str__(self) -> str:
        try:
            self.zc += 1
        except:
            self.zc = 0
        return str(self.zc)


