import pygame
import sys

global win
global lose

from sprites.player import Player
from sprites.enemy import Enemy
from questionconfig import ezQuestions, hardQuestions

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
bg1 = pygame.transform.scale(pygame.image.load("assets/bg1.jpg").convert_alpha(), (1280, 720))
bg2 = pygame.transform.scale(pygame.image.load("assets/bg2.png").convert_alpha(), (1280, 720))

gameover = pygame.mixer.Sound("music/Game_over.wav")
ansright = pygame.mixer.Sound("music/game-start-6104.mp3")
answrong = pygame.mixer.Sound("music/mixkit-losing-bleeps-2026.wav")
winsound = pygame.mixer.Sound("music/mixkit-ethereal-fairy-win-sound-2019.wav")


ezquestions = ezQuestions()
hardquestions = hardQuestions()


level1 = True
level2 = False


random.shuffle(ezquestions.ezquestions)
random.shuffle(hardquestions.hardquestions)


all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()

htpdisplayed = True

enemy = Enemy(10, 330, 200, 200)
enemy_sprites.add(enemy)
all_sprites.add(enemy)

player = Player(200, 435, 100, 100)
player_sprite.add(player)
all_sprites.add(player)
def check_collision():
    if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > enemy.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                pygame.mixer.Sound.play(gameover)
                screen.blit(lose, (0,0))
                pygame.display.update()
                pygame.time.delay(2000)
                reset_game()
                screen.blit(bg1, (0, 0))
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
            pygame.mixer.Sound.play(winsound)
            pygame.display.update()
            pygame.time.delay(2000)  # Display the "You Win" screen for 2 seconds
            reset_game()  # Reset the game
            screen.blit(bg1, (0, 0))  # Clear the screen

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
            
        

        if keys[pygame.K_ESCAPE]:
            print('keypress registered')
            if htpdisplayed:
                htpdisplayed = False
        if event.type == pygame.MOUSEMOTION:
            if not htpdisplayed:
                if level1:
                    ezquestions.get_hovered_option()
                if level2:
                    hardquestions.get_hovered_option()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not htpdisplayed:
                if level1:
                    anscheck = ezquestions.get_clicked_option()
                    if anscheck == True:
                        pygame.mixer.Sound.play(ansright)
                        player.x += 110
                        ezquestions.display_question(ezquestions.ezquestions[ezquestions.current_question_index], hovered_option)
                        if player.x > 1280:
                            level1 = False
                            level2 = True
                            level3 = False
                    if anscheck == False:
                        pygame.mixer.Sound.play(answrong)
                        enemy.x += 100
                if level2:
                    anscheck = hardquestions.get_clicked_option()
                    if anscheck == True:
                        pygame.mixer.Sound.play(ansright)
                        player.x += 110
                        hardquestions.display_question(hardquestions.hardquestions[hardquestions.current_question_index], hovered_option)
                        finish()
                        
                    if anscheck == False:
                        pygame.mixer.Sound.play(answrong)
                        enemy.x += 100
                    
    if htpdisplayed:                
        screen.blit(htp, (0, 0))
    if not htpdisplayed:
        if level1:
            screen.blit(bg1, (0, 0))
            if ezquestions.current_question_index < len(ezquestions.ezquestions):
                ezquestions.display_question(ezquestions.ezquestions[ezquestions.current_question_index], hovered_option)
                if player.x > 1280:
                    level1 = False
                    level2 = True

        if level2:
            screen.blit(bg2, (0, 0))
            if hardquestions.current_question_index < len(hardquestions.hardquestions):
                hardquestions.display_question(hardquestions.hardquestions[hardquestions.current_question_index], hovered_option)
                if player.x > 1280:
                    level1 = False
                    level2 = False

        

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