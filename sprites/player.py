import pygame
import random
screen = pygame.display.set_mode((1280, 720))


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height) -> None:
        self.x = 200
        self.y = 440
        self.width = width
        self.height = height
        self.run = [pygame.transform.scale(pygame.image.load(f'assets/player/running/1.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/2.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/3.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/4.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/5.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/6.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/7.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/player/running/8.png'), (self.width, self.height))
                     ]
        self.jump = [pygame.transform.scale(pygame.image.load(f'assets/player/jumping/1.png'), (self.width, self.height)),
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
        self.char = pygame.transform.scale(pygame.image.load(f'assets/player/standing.png'), (self.width, self.height))
        self.isJump = False
        self.right = True
        self.standing = False
        self.step_index_jumping = 0
        self.image = self.run[0] #the first image of the list is the standing image 
        self.rect = self.image.get_rect() #rect of the first image of the list 
        self.rect.x = self.x
        self.rect.y = self.y # set x and y of rect to x and y of image
        self.jumpCount = 10
        self.walkCount = 0
        self.jump_height = 10 # Adjust this value to control animation speed
        self.last_update_time = pygame.time.get_ticks()
        self.gravity = 0
        self.vel = self.jump_height
        
    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.right:
            screen.blit(self.run[self.walkCount // 2 % len(self.run)], (self.x, self.y))
            self.walkCount += 1

        if self.isJump:
            screen.blit(self.jump[self.walkCount // 3 % len(self.jump)], (self.x, self.y))
            self.gravity += 1
            self.rect.y += self.gravity
            self.walkCount += 1
        


        