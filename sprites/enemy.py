import pygame
screen = pygame.display.set_mode((1280, 720))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        self.x = 150
        self.y = 450
        self.width = width
        self.height = height
        self.run = [pygame.transform.scale(pygame.image.load(f'assets/Enemy/1.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/Enemy/2.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/Enemy/3.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/Enemy/4.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/Enemy/5.png'), (self.width, self.height)),
                     pygame.transform.scale(pygame.image.load(f'assets/Enemy/6.png'), (self.width, self.height))
                     ]
        self.state_run = True
        self.state_jump = False
        self.state_duck = False
        self.step_index_running = 0
        self.isJump = False
        self.right = False
        self.standing = True
        self.step_index_jumping = 0
        self.image = self.run[0] #the first image of the list is the standing image 
        self.rect = self.image.get_rect() #rect of the first image of the list 
        self.rect.x = self.x
        self.rect.y = self.y # set x and y of rect to x and y of image
        self.jumpCount = 10
        self.walkCount = 0
        self.vel = 5
        self.jump_delay = 60  # 60 frames (1 second delay)
        self.jump_delay_counter = 0

    def draw(self,screen, player_x):
        self.move_towards_player(player_x)
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.right or self.isJump:
            screen.blit(self.run[self.walkCount // 2 % len(self.run)], (self.x, self.y))
            self.walkCount += 1


    def jump(self):
        if self.jump_delay_counter >= self.jump_delay:
            self.isJump = True
            self.jump_delay_counter = 0
    def move_towards_player(self, player_x):
        if self.x < player_x:
            self.x += self.vel
        elif self.x > player_x:
            self.x -= self.vel