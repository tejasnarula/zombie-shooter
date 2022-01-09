import pygame
import math

class Bullet():
    def __init__(self,x,y,mouseX, mouseY,bullets_class,width = 5, height = 5,color = (255,255,255)):
        self.bullets = bullets_class

        # -- bullet stats -- 
        self.color = color
        #self.radius = radius
        self.width = width
        self.height= height
        self.x = x
        self.y = y
        
        # -- bullet var --
        self.speed = 10

        #as each bullet is new - it only has 1 target (current)
        self.targetX,self.targetY = mouseX, mouseY
        self.distanceX,self.distanceY = self.targetX - self.x,self.targetY - self.y
        self.angle = math.atan2(self.distanceX,self.distanceY)
        self.moveX,self.moveY = math.sin(self.angle) * self.speed,math.cos(self.angle) * self.speed
    
    def run(self, surface):
        self.draw(surface)
        self.shoot()

    def draw(self, surface):
        #bulletCircle = (self.x,self.y)
        #self.bullet = pygame.draw.circle(surface,self.color,bulletCircle,self.radius)
        self.bullet = pygame.draw.rect(surface,self.color,pygame.Rect(self.x,self.y,self.width,self.height))

    def shoot(self):
        self.x += self.moveX
        self.y += self.moveY
        for bullet in self.bullets:
            #print(self.bullets)
            if self.x > 800 or self.x < 0:
                #print("remove" + str(self.bullets.index(bullet)))
                self.bullets.remove(bullet)
                break
