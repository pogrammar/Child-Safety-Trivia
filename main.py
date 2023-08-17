import pygame
import os 
from random import *
import random
from sys import exit
import time
from sprites.player import Player
from sprites.enemy import Enemy

pygame.init()
player = Player(100, 100) 
enemy = Enemy(200, 200)
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

start = 5
death_screen = pygame.transform.scale(pygame.image.load('assets/final_screen.png'), (200,200))
finished = False
counter, text = 100, '100'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
finished_text = font.render('Mission Complete!', True, 'black')

crate_img = pygame.transform.scale(pygame.image.load('assets/obstacles/crate1.png'), (50, 50)).convert_alpha()
dustbin_img = pygame.image.load('assets/obstacles/dustbin.png').convert_alpha()

bg= pygame.image.load('assets/bg.png')

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 10
            if obstacle_rect.bottom == 530:
                screen.blit(crate_img, obstacle_rect)
            else:
                screen.blit(dustbin_img, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x  > -100]
        return obstacle_list
    else: return []
def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.rect.colliderect(obstacle_rect):
                print('hello world')
obstacle_rect_list = []




#timer

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, random.randrange(900 , 2500))

run = True
game_active = True

while run:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



        if event.type == obstacle_timer:
            if randint(0, 2):
                obstacle_rect_list.append(crate_img.get_rect(bottomright=(randint(1000, 2000), 530)))
            else:
                obstacle_rect_list.append(dustbin_img.get_rect(bottomright=(randint(1000, 1500), 535)))
        if event.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'

    
    if keys[pygame.K_d] and player.x < 1220 - player.width - player.vel:
        player.right = True
        player.standing = False
        enemy.right = True
        enemy.standing = False
    else:
        player.right = False
        player.standing = True
        player.walkCount = 0
        enemy.right = False
        enemy.standing = True
        enemy.walkCount = 0

    if not player.isJump:
        if keys[pygame.K_SPACE]:
            player.isJump = True
            player.right = False
            player.walkCount = 0
            enemy.isJump = True
            enemy.right = False
            enemy.walkCount = 0

    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.4 * neg
            player.jumpCount -= 1
            enemy.y -= (enemy.jumpCount ** 2) * 0.4 * neg
            enemy.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10
            enemy.isJump = False
            enemy.jumpCount = 10

    screen.blit(bg, (0, 0))

    # Obstacle movement
    for obstacle_rect in obstacle_rect_list:
        obstacle_rect.x -= 10
        if obstacle_rect.bottom == 530:
            screen.blit(crate_img, obstacle_rect)
        else:
            screen.blit(dustbin_img, obstacle_rect)
    obstacle_rect_list = [obstacle for obstacle in obstacle_rect_list if obstacle.x > -100]
    start -= 0.025
    if start <=0:
        finished = True
   
    collision(player, obstacle_rect_list)
    player.draw(screen)
    enemy.draw(screen, player.x)
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    
    
    

    pygame.display.update()
    clock.tick(60)

pygame.quit()