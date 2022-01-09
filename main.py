# ---------  Zombie Shooter Game --------- #
import pygame
from pygame.locals import *
from random import randint as rand

from player import Player
from bullet import Bullet
from zombie import Zombie

#variabls / constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#pygame initialization!
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Zombie invader')

BACKGROUND_COLOR = (30,30,30)
screen.fill(BACKGROUND_COLOR)


class Game():
    def __init__(self,surface):
        self.screen = surface

        self.keysPressed = []
        self.mouseX, self.mouseY = pygame.mouse.get_pos()

        self.bullets = []
        self.zombies = []

        #define these in the updateGame() function
        self.bulletDelay = 0
        self.zombieSpawnDelay = 0
    
    def updateGame(self):
        #Run all the or specific objects
        for bullet in self.bullets:
            bullet.run(self.screen)
        for zombie in self.zombies:
            zombie.run(self.screen)
        player.run()

        #Make The object
        if "space" in self.keysPressed:
            if self.bulletDelay < 0:
                self.BulletX = Bullet(player.x+player.width/2-1,player.y+player.height/2-1,self.mouseX,self.mouseY,self.bullets)
                self.bullets.append(self.BulletX)
                self.bulletDelay = 1
        
        if self.zombieSpawnDelay < 0:
            self.zombieSpawnDelay = 20
            self.zombieX = Zombie(SCREEN_WIDTH,rand(20,500),20,20,player,self.zombies)
            self.zombies.append(self.zombieX)
            #print(self.zombies)

        self.zombieSpawnDelay -= 0.1
        self.bulletDelay -= 0.1
    def run(self):
        #main loop  
        running = True
        while running:

            self.screen.fill(BACKGROUND_COLOR)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RIGHT or event.key == K_d:
                        self.keysPressed.append("right")
                    if event.key == K_LEFT or event.key == K_a:
                        self.keysPressed.append("left")
                    if event.key == K_UP or event.key == K_w:
                        self.keysPressed.append("up")
                    if event.key == K_DOWN  or event.key == K_s:
                        self.keysPressed.append("down")
                    if event.key == K_SPACE:
                        self.keysPressed.append("space")
                    if event.key == K_p:
                        self.keysPressed.append("p")
                        
                
                if event.type == KEYUP:
                    if event.key == K_RIGHT or event.key == K_d:
                        self.keysPressed.remove("right")
                    if event.key == K_LEFT or event.key == K_a:
                        self.keysPressed.remove("left")
                    if event.key == K_UP or event.key == K_w:
                        self.keysPressed.remove("up")
                    if event.key == K_DOWN  or event.key == K_s:
                        self.keysPressed.remove("down")
                    if event.key == K_SPACE:
                        self.keysPressed.remove("space")
                        

                if event.type == pygame.QUIT:
                    running = False

            self.mouseX, self.mouseY = pygame.mouse.get_pos()
            clock.tick(60)
            
            self.updateGame()
            pygame.display.update()
if __name__ == '__main__':
    main = Game(screen)
    player = Player(screen, main.keysPressed, SCREEN_WIDTH, SCREEN_HEIGHT)

    main.run()