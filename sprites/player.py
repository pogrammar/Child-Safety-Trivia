import pygame

screen = pygame.display.set_mode((1280, 720))

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.x = 200
        self.y = 440
        self.width = width
        self.height = height
        self.run = [
            pygame.transform.scale(pygame.image.load(f'assets/player/running/1.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/running/2.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/running/3.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/running/4.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/running/5.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/running/6.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/running/7.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/running/8.png'), (self.width, self.height))
        ]
        self.jump = [
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/1.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/2.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/3.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/4.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/5.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/6.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/7.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/8.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/9.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/10.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load(f'assets/player/jumping/11.png'), (self.width, self.height))
        ]
        self.image = self.run[0]  # the first image of the list is the standing image
          # set x and y of rect to x and y of image


        self.isJump = False
        self.right = True
        self.jumpCount = 10
        self.walkCount = 0
        self.gravity = 0
        self.hitbox = (self.x + 20, self.y + 11, 45, 70)

        
    def draw(self, screen):
        if self.walkCount + 1 >= 64:
            self.walkCount = 0
        if self.right:
            screen.blit(self.run[self.walkCount // 2 % len(self.run)], (self.x, self.y))
            self.walkCount += 1

        if self.isJump:
            screen.blit(self.jump[self.walkCount // 3 % len(self.jump)], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 20, self.y + 11, 45, 70)
