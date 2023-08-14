import pygame
win = pygame.display.set_mode((1280, 720))

char = pygame.image.load('assets/player/standing.png')

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.walk = [pygame.image.load('assets/player/1.png'),
                     pygame.image.load('assets/player/2.png'),
                     pygame.image.load('assets/player/3.png'),
                     pygame.image.load('assets/player/4.png'),
                     pygame.image.load('assets/player/5.png'),
                     pygame.image.load('assets/player/6.png'),
                     pygame.image.load('assets/player/7.png'), 
                     pygame.image.load('assets/player/8.png'), 
                     pygame.image.load('assets/player/9.png'),
                     pygame.image.load('assets/player/10.png')
                     ]
        self.x = x
        self.y = y
        self.vel = 5

        self.right = False
        self.width = width
        self.height = height
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.right:
                win.blit(self.walk[self.walkCount//5], (self.x,self.y))
                self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))