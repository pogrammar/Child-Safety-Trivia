import pygame

from lists.ezquestions import child_safety_questions_ez
from lists.medquestions import child_safety_questions_med
from lists.hardquestions import child_safety_questions_hard
from sprites.enemy import Enemy
from sprites.player import Player
import random
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font(None, 36)
bg = pygame.image.load("assets/bg.png").convert_alpha()
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOVER_COLOR = (200, 200, 200) 
HOVER_SCALE = 1.05


class ezQuestions():
    def __init__(self) -> None:
        self.ezquestions = list(child_safety_questions_ez.values())
        self.question_index = 0
        self.current_question_index = 0
        self.hovered_option = None
        self.player = Player(100, 100)
        self.enemy = Enemy(200, 200)

    def display_question(self, question_data, hovered_option):
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

            if self.hovered_option == option_index:
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
    def get_hovered_option(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if self.current_question_index < len(self.ezquestions):

            self.hovered_option = self.ezquestions[self.current_question_index]["correct_answer"]

            for option_index, option_y in enumerate(range(150, 350, 50)):
                if option_y <= mouse_y < option_y + 50:
                    
                    self.hovered_option = option_index
                    break
    def reset_game(self):
        self.current_question_index = 0
        self.player.x = 200
        self.enemy.x = 10
        random.shuffle(self.ezquestions) 
    def finish(self):
        if self.player.x > 1280:
            screen.blit(screen, (0,0))
            pygame.display.update()
            pygame.time.delay(2000)  # Display the "You Win" screen for 2 seconds
            self.reset_game()  # Reset the game
            screen.blit(bg, (0, 0))  # Clear the screen

            # Check if you have more questions to display
            if self.current_question_index < len(self.ezquestions):
                self.display_question(self.ezquestions[self.current_question_index], self.hovered_option)

    def get_clicked_option(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
                
        if self.current_question_index < len(self.ezquestions):
            correct_answer = self.ezquestions[self.current_question_index]["correct_answer"]
            if 150 <= mouse_y <= 200:
                global chosen_option
                chosen_option = self.ezquestions[self.current_question_index]["options"][0]
            elif 200 <= mouse_y <= 250:
                chosen_option = self.ezquestions[self.current_question_index]["options"][1]
            elif 250 <= mouse_y <= 300:
                chosen_option = self.ezquestions[self.current_question_index]["options"][2]
            elif 250 <= mouse_y <= 350:
                chosen_option = self.ezquestions[self.current_question_index]["options"][3]
            else:
                chosen_option = None
            
            if chosen_option == correct_answer and 150 <= mouse_y <= 350:
                self.current_question_index += 1
                return True
                

            else:
                return False
        