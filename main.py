import pygame
import sys
from sprites.player import Player
from sprites.enemy import Enemy
from pygame.locals import RESIZABLE
from questions import child_safety_questions
import random
# Initialize Pygame
pygame.init()

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

global win
global lose
global bg
global floor

htp = pygame.image.load('assets/Howtoplay.png').convert_alpha()
win = pygame.image.load('assets/you_win.png').convert_alpha()
lose = pygame.image.load('assets/lose.png').convert_alpha()
font = pygame.font.Font(None, 36)
bg = pygame.image.load("assets/bg.png").convert_alpha()
floor = pygame.image.load("assets/floor.png").convert_alpha()



def display_question(question_data, hovered_option):
    question = question_data["question"]
    options = question_data["options"]

    question_text = font.render(question, True, BLACK)
    question_rect = question_text.get_rect(topleft=(50, 50))
    pygame.draw.rect(screen, WHITE, question_rect.inflate(20, 10), border_radius=10)
    screen.blit(question_text, question_rect)

    y_position = 150
    for option_index, option in enumerate(options):
        option_text = font.render(option, True, BLACK)
        option_rect = option_text.get_rect(topleft=(50, y_position))

        if hovered_option == option_index:
            # Apply a colorful hover animation
            pygame.draw.rect(screen, HOVER_COLOR, option_rect.inflate(20, 10), border_radius=10)
            option_text = font.render(option, True, WHITE)  # Change text color when hovered
            scaled_width = int(option_rect.width * HOVER_SCALE)
            scaled_height = int(option_rect.height * HOVER_SCALE)
            scaled_text = pygame.transform.scale(option_text, (scaled_width, scaled_height))
            option_rect = scaled_text.get_rect(topleft=(50, y_position))
        else:
            pygame.draw.rect(screen, WHITE, option_rect.inflate(20, 10), border_radius=10)

        screen.blit(option_text, option_rect)
        y_position += 60

question_index = 0


player = Player(100, 100) 
enemy = Enemy(200, 200)
current_question_index = 0
questions = list(child_safety_questions.values())
random.shuffle(questions)

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
                screen.blit(lose, (0,0))
                pygame.display.update()
                pygame.time.delay(2000)
                reset_game()
                screen.blit(bg, (0, 0))
                screen.blit(floor, (0, 720))
                if current_question_index < len(questions):
                    display_question(questions[current_question_index], hovered_option)
def reset_game():
    global current_question_index
    current_question_index = 0
    player.x = 200
    enemy.x = 10
    random.shuffle(questions) 

def finish():
    if player.x > 1280:
        screen.blit(win, (0,0))
        pygame.display.update()
        pygame.time.delay(2000)  # Display the "You Win" screen for 2 seconds
        reset_game()  # Reset the game
        screen.blit(bg, (0, 0))  # Clear the screen

        # Check if you have more questions to display
        if current_question_index < len(questions):
            display_question(questions[current_question_index], hovered_option)


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
            floor = pygame.transform.scale_by(pygame.image.load("assets/floor.png").convert_alpha(), (new_width, 1))
            screen.blit(floor, (0, 0))
            
            win = pygame.transform.scale(pygame.image.load('assets/you_win.png').convert_alpha(), (new_width, new_height))
            lose = pygame.transform.scale(pygame.image.load('assets/lose.png').convert_alpha(), (new_width, new_height))

        if keys[pygame.K_ESCAPE]:
            print('keypress registered')
            if htpdisplayed:
                htpdisplayed = False
        if event.type == pygame.MOUSEMOTION:
            if not htpdisplayed:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if current_question_index < len(questions):

                    hovered_option = questions[current_question_index]["correct_answer"]

                    for option_index, option_y in enumerate(range(150, 350, 50)):
                        if option_y <= mouse_y < option_y + 50:
                            
                            hovered_option = option_index
                            break
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not htpdisplayed:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if current_question_index < len(questions):
                    correct_answer = questions[current_question_index]["correct_answer"]
                    if 150 <= mouse_y <= 200:
                        global chosen_option
                        chosen_option = questions[current_question_index]["options"][0]
                    elif 200 <= mouse_y <= 250:
                        chosen_option = questions[current_question_index]["options"][1]
                    elif 250 <= mouse_y <= 300:
                        chosen_option = questions[current_question_index]["options"][2]
                    elif 250 <= mouse_y <= 350:
                        chosen_option = questions[current_question_index]["options"][3]
                    else:
                        chosen_option = None
                    
                    if chosen_option == correct_answer and 150 <= mouse_y <= 350:
                        current_question_index += 1
                        player.x += 110
                        finish()

                    else:
                        enemy.x += 100
                    
    screen.blit(htp, (0, 0))
    if not htpdisplayed:
        screen.blit(bg, (0, 0))
        screen.blit(floor, (0, 0))

        if current_question_index < len(questions):
            display_question(questions[current_question_index], hovered_option)
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
        finish()
        check_collision()
    pygame.display.update()
    clock.tick(32)
    

pygame.quit()