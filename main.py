import pygame
import sys

global win
global lose
global bg

from sprites.player import Player
from sprites.enemy import Enemy
from questionconfig import ezQuestions

from pygame.locals import RESIZABLE
#from pygame import mixer
import random
# Initialize Pygame
pygame.init()
#mixer.init()
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (200, 200, 200) 
HOVER_SCALE = 1.05
clock = pygame.time.Clock()
# Set up the display
screen = pygame.display.set_mode((1280, 720), RESIZABLE)
screen_x, screen_y = screen.get_size()
a = pygame.display.set_caption("Child Safety Trivia")

htp = pygame.image.load('assets/Howtoplay.png').convert_alpha()
win = pygame.image.load('assets/you_win.png').convert_alpha()
lose = pygame.image.load('assets/lose.png').convert_alpha()
font = pygame.font.Font(None, 36)
bg = pygame.image.load("assets/bg.png").convert_alpha()

#gameover = pygame.mixer.Sound("music/Game_over.wav")




ezquestions = ezQuestions()

player = Player(100, 100) 
enemy = Enemy(200, 200)

random.shuffle(ezquestions.ezquestions)

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()

htpdisplayed = True
enemy = Enemy(250, 250)
enemy_sprites.add(enemy)
all_sprites.add(enemy)

player = Player(100, 100)
player_sprite.add(player)
all_sprites.add(player)
def check_collision():
    if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > enemy.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                #pygame.mixer.Sound.play(gameover)
                screen.blit(lose, (0,0))
                pygame.display.update()
                pygame.time.delay(2000)
                reset_game()
                screen.blit(bg, (0, 0))
                if current_question_index < len(ezquestions.ezquestions):
                    ezquestions.display_question(ezquestions.ezquestions[ezquestions.current_question_index], hovered_option)
def reset_game():
    global current_question_index
    current_question_index = 0
    player.x = 200
    enemy.x = 10
    random.shuffle(ezquestions.ezquestions) 
def finish():
        if player.x > 1280:
            screen.blit(win, (0,0))
            pygame.display.update()
            pygame.time.delay(2000)  # Display the "You Win" screen for 2 seconds
            reset_game()  # Reset the game
            screen.blit(bg, (0, 0))  # Clear the screen

            # Check if you have more questions to display
            if ezquestions.current_question_index < len(ezquestions.ezquestions):
                ezquestions.display_question(ezquestions.ezquestions[ezquestions.current_question_index], ezquestions.hovered_option)

###Main
global hovered_option
hovered_option = None

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.VIDEORESIZE:
            # Handle window resizing event
            
            new_width, new_height = event.size
            screen_x, screen_y = new_width, new_height
            # Adjust your game's content to fit the new window dimensions
            bg = pygame.transform.scale(pygame.image.load("assets/bg.png").convert_alpha(), (new_width, new_height))
            screen.blit(bg, (0, 0))
            
            win = pygame.transform.scale(pygame.image.load('assets/you_win.png').convert_alpha(), (new_width, new_height))
            lose = pygame.transform.scale(pygame.image.load('assets/lose.png').convert_alpha(), (new_width, new_height))

        if keys[pygame.K_ESCAPE]:
            print('keypress registered')
            if htpdisplayed:
                htpdisplayed = False
        if event.type == pygame.MOUSEMOTION:
            if not htpdisplayed:
                ezquestions.get_hovered_option()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not htpdisplayed:
                anscheck = ezquestions.get_clicked_option()
                if anscheck == True:
                    player.x += 110
                    ezquestions.display_question(ezquestions.ezquestions[ezquestions.current_question_index], hovered_option)
                    finish()
                if anscheck == False:
                    enemy.x += 100
                    
    screen.blit(htp, (0, 0))
    if not htpdisplayed:
        screen.blit(bg, (0, 0))
        if ezquestions.current_question_index < len(ezquestions.ezquestions):
            ezquestions.display_question(ezquestions.ezquestions[ezquestions.current_question_index], hovered_option)
        else:
            # Display game over or next level screen
            pass

        if not player.isJump:
            if keys[pygame.K_SPACE]:
                player.isJump = True
                player.right = False
                player.walkCount = 0

        else:
            if player.jumpCount >= -10:
                neg = 1
                if player.jumpCount < 0:
                    neg = -1
                player.y -= (player.jumpCount ** 2) * 0.4 * neg
                player.jumpCount -= 1
            else:
                player.isJump = False
                player.jumpCount = 10
        
        player.draw(screen)
        player.right = True
        player.standing = False
        enemy.draw(screen)
        enemy.right = True
        enemy.standing = False
        ezquestions.finish()
        check_collision()
    pygame.display.update()
    clock.tick(32)
    

pygame.quit()