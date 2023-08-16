import pygame
win = pygame.display.set_mode((1280, 720))
class Obstacles(pygame.sprite.Sprite):
    def __init__(self, obstacle, width, height):
        self.type = obstacle
        self.width = width
        self.height = height
        self.x = 1220
        if self.type == "cone":
            self.obstacle = pygame.transform.scale(pygame.image.load(f'assets/obstacles/cone.png'), (self.width, self.height))
            self.y = 430
        if self.type == "rocket":
            self.obstacle = pygame.transform.scale(pygame.image.load(f'assets/obstacles/rocket.png'), (self.width, self.height))
            self.y = 300
        self.visible = True
    
    def move(self):
        if self.visible:
            if self.x < 5:
                self.visible = False
            if self.x <= -100: 
                self.kill()

    def draw(self):

        win.blit(self.obstacle, (self.x, self.y))
        self.move()
        
