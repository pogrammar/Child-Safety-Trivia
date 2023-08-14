import pygame
from sprites.player import Player

pygame.init()

win = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
bg = pygame.image.load('assets/bg.jpg')
floor = pygame.image.load('assets/floor.png')

man = Player(10, 320, 100, 100)

while True:
    win.blit(bg, (0, 0))
    win.blit(floor, (0, 720))
    

    for event in pygame.event.get(): #allows the user to exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and man.x < 1220 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.standing = False
    else:
        man.right = False
        man.standing = True
        man.walkCount = 0
        
    
    man.draw(win)
    clock.tick(60)
    pygame.display.update()
