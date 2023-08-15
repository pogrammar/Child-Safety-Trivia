import pygame
win = pygame.display.set_mode((1280, 720))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):

            
        self.x = x
        self.y = y
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.right = False
        self.width = width
        self.height = height
        self.walk = [pygame.transform.scale(pygame.image.load(f'assets/player/running/1.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/2.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/3.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/4.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/5.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/6.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/7.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/8.png'), (self.width, self.height)),]
        self.char = pygame.transform.scale(pygame.image.load(f'assets/player/standing.png'), (self.width, self.height))
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.right:
                win.blit(self.walk[self.walkCount // 2 % len(self.walk)], (self.x, self.y))
                self.walkCount += 1
        else:
            win.blit(self.char, (self.x, self.y))

        