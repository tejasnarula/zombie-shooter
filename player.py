import pygame

class Player():
    def __init__(self,surface, keysPressed, SCREEN_WIDTH, SCREEN_HEIGHT) -> None:
        self.screen = surface
        self.keysPressed = keysPressed

        # -- Player Stats --
        self.color = pygame.Color('dodgerblue1')
        self.width = 20
        self.height = 20
        self.x = 20
        self.y = SCREEN_HEIGHT/2 - self.height/2
    
    def run(self):
        #running all the Player function
        self.draw()
        self.move()
    def draw(self):
        #drawing player on the screen
        self.player = pygame.draw.rect(self.screen,self.color,pygame.Rect(self.x,self.y,self.width,self.height))
    
    def move(self):
        #moving player
        if "right" in self.keysPressed:
            self.x += 4
        if "left" in self.keysPressed:
            self.x -= 4
        if "up" in self.keysPressed:
            self.y -= 4
        if "down" in self.keysPressed:
            self.y += 4