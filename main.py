import pygame
import sys
from sprites.player import Player
from sprites.enemy import Enemy
# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (200, 200, 200) 
clock = pygame.time.Clock()
# Set up the display
screen = pygame.display.set_mode((1280, 720))
bg = pygame.display.set_caption("Child Safety Trivia")

# Define fonts
font = pygame.font.Font(None, 36)
bg = pygame.image.load("assets/bg.png").convert_alpha()
crate_img = pygame.transform.scale(pygame.image.load('assets/obstacles/crate1.png'), (50, 50)).convert_alpha()
dustbin_img = pygame.image.load('assets/obstacles/dustbin.png').convert_alpha()




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

obstacle_rect_list = []


child_safety_questions = {
    "Q1": {
        "question": "Q1) What should you do when crossing the street?",
        "options": ["Run as fast as you can", "Look both ways before crossing", "Text on your phone", "Close your eyes and cross"],
        "correct_answer": "Look both ways before crossing"
    },
    "Q2": {
        "question": "Q2) Who should you talk to if a stranger approaches you?",
        "options": ["Tell them your name", "Run away", "Find a trusted adult", "Give them your address"],
        "correct_answer": "Find a trusted adult"
    },
    "Q3": {
        "question": "Q3) Why is it important to wear a helmet when riding a bike?",
        "options": ["Because it looks cool", "To protect your head in case of a fall", "To carry things on your head", "To see better"],
        "correct_answer": "To protect your head in case of a fall"
    },
    "Q4": {
        "question": "Q4) What information should you avoid sharing online?",
        "options": ["Your favorite color", "Your full name, address, and phone number", "Your school's name", "Your favorite food"],
        "correct_answer": "Your full name, address, and phone number"
    },
    "Q5": {
        "question": "Q5) What should you do if you're home alone and the doorbell rings?",
        "options": ["Open the door for anyone", "Answer the door and invite them in", "Don't open the door and stay quiet", "Shout loudly and ask who's there"],
        "correct_answer": "Don't open the door and stay quiet"
    },
    "Q6": {
        "question": "Q6) What's the first thing you should do in case of a fire?",
        "options": ["Start cooking marshmallows", "Call your friends", "Sound the alarm and exit the building", "Take a nap"],
        "correct_answer": "Sound the alarm and exit the building"
    },
    "Q7": {
        "question": "Q7) Why is it important to wear a seatbelt in a car?",
        "options": ["To keep your clothes clean", "To show off to your friends", "To avoid getting a ticket", "To stay safe in case of an accident"],
        "correct_answer": "To stay safe in case of an accident"
    },
    "Q8": {
        "question": "Q8) What should you do if you get lost in a public place?",
        "options": ["Hide and wait for someone to find you", "Start screaming loudly", "Approach a security guard or a trusted adult", "Try to find your way home on your own"],
        "correct_answer": "Approach a security guard or a trusted adult"
    },
    "Q9": {
        "question": "Q9) Why is it important to wash your hands?",
        "options": ["To waste water", "To make them smell nice", "To get rid of germs and stay healthy", "To impress your parents"],
        "correct_answer": "To get rid of germs and stay healthy"
    },
    "Q10": {
        "question": "Q10) What's the best way to stay safe around the swimming pool?",
        "options": ["Run and jump into the pool", "Push your friends into the pool for fun", "Stay away from the pool", "Follow the rules and ask an adult for supervision"],
        "correct_answer": "Follow the rules and ask an adult for supervision"
    }
}




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
            pygame.draw.rect(screen, HOVER_COLOR, option_rect.inflate(20, 10), border_radius=10)
        else:
            pygame.draw.rect(screen, WHITE, option_rect.inflate(20, 10), border_radius=10)

        screen.blit(option_text, option_rect)
        y_position += 60

    pygame.display.flip()
question_index = 0


player = Player(100, 100) 
enemy = Enemy(200, 200)
current_question_index = 0
questions = list(child_safety_questions.values())

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()

enemy = Enemy(200, 200)
enemy_sprites.add(enemy)
all_sprites.add(enemy)

player = Player(100, 100)
player_sprite.add(player)
all_sprites.add(player)
def check_collision():
    if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > enemy.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                print('sdsd')


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if current_question_index < len(questions):
                global hovered_option
                hovered_option = None

                for option_index, option_y in enumerate(range(150, 350, 50)):
                    if option_y <= mouse_y < option_y + 50:
                        
                        hovered_option = option_index
                        break
        
        if event.type == pygame.MOUSEBUTTONDOWN:
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
                    player.x += 100

                else:
                    enemy.x += 100
                    obstacle_rect = crate_img.get_rect(midtop=(1280, 500))
                    obstacle_rect_list.append(obstacle_rect)
                    

    screen.blit(bg, (0, 0))

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
    check_collision()
    obstacle_rect_list = obstacle_movement(obstacle_rect_list)
    pygame.display.update()
    clock.tick(60)
    

pygame.quit()



