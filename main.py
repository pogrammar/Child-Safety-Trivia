import pygame
from sprites.player import Player

pygame.init()

win = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
bg = pygame.image.load('assets/bg.png').convert_alpha()
bg_x = 0
game_speed = 10


man = Player(10, 430, 100, 100)

while True:
    win.blit(bg, (0, 0))

    for event in pygame.event.get(): #allows the user to exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and man.x < 1220 - man.width - man.vel:
        bg_x -= 10
        game_speed += 0.025
        win.fill("white")
        if bg_x <= -1280:
            bg_x = 0
        win.blit(bg, (bg_x, 0))
        win.blit(bg, (bg_x + 1280, 0))
        man.right = True
        man.standing = False
    else:
        man.right = False
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.3 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    man.draw(win)
    clock.tick(60)
    pygame.display.update()
