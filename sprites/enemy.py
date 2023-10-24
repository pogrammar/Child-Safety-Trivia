import pygame

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.x = 10
        self.y = 320
        self.width = width
        self.height = height
        self.run = [
            pygame.transform.scale(pygame.image.load(f'assets/Enemy/run/1.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/Enemy/run/2.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/Enemy/run/3.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/Enemy/run/4.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/Enemy/run/5.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/Enemy/run/6.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/Enemy/run/7.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/Enemy/run/8.png'), (self.width, self.height))
        ]
        self.state_run = True
        self.walkCount = 0
        self.image = self.run[0]  # the first image of the list is the standing image
        self.rect = self.image.get_rect()  # rect of the first image of the list
        self.rect.x = self.x
        self.rect.y = self.y  # set x and y of rect to x and y of image
        self.hitbox = (self.x + 55, self.y + 70, 70, 170)
        self.rect = pygame.draw.rect(screen, (255,0,0), self.hitbox,2)

    def draw(self, screen):
        if self.walkCount + 1 >= 64:
            self.walkCount = 0
        if self.state_run:
            screen.blit(self.run[self.walkCount // 2 % len(self.run)], (self.x, self.y))
            self.walkCount += 1
            self.hitbox = (self.x + 55, self.y + 70, 70, 170)