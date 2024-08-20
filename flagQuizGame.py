import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FLAG_WIDTH = 200
FLAG_HEIGHT = 120
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (245, 199, 140)
# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flag Quiz Game")
font = pygame.font.SysFont(None, 35)

# Flag drawing functions
def draw_bangladesh():
    pygame.draw.rect(screen, (0, 106, 78), [300, 240, FLAG_WIDTH, FLAG_HEIGHT])
    pygame.draw.circle(screen, (244, 42, 65), (400, 300), 40)

def draw_france():
    pygame.draw.rect(screen, (0, 85, 164), [300, 240, 66, FLAG_HEIGHT])
    pygame.draw.rect(screen, WHITE, [366, 240, 68, FLAG_HEIGHT])
    pygame.draw.rect(screen, (239, 65, 53), [434, 240, 66, FLAG_HEIGHT])

def draw_germany():
    pygame.draw.rect(screen, (0, 0, 0), [300, 240, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, (221, 0, 0), [300, 280, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, (255, 206, 0), [300, 320, FLAG_WIDTH, 40])

def draw_netherland():
    pygame.draw.rect(screen, (174, 28, 40), [300, 240, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, WHITE, [300, 280, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, (33, 70, 139), [300, 320, FLAG_WIDTH, 40])

def draw_italy():
    pygame.draw.rect(screen, (0, 146, 70), [300, 240, 66, FLAG_HEIGHT])
    pygame.draw.rect(screen, WHITE, [366, 240, 68, FLAG_HEIGHT])
    pygame.draw.rect(screen, (206, 43, 55), [434, 240, 66, FLAG_HEIGHT])

def draw_belgium():
    pygame.draw.rect(screen, (0, 0, 0), [300, 240, 66, FLAG_HEIGHT])
    pygame.draw.rect(screen, (255, 255, 0), [366, 240, 68, FLAG_HEIGHT])
    pygame.draw.rect(screen, (239, 51, 64), [434, 240, 66, FLAG_HEIGHT])

def draw_bulgaria():
    pygame.draw.rect(screen, WHITE, [300, 240, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, (0, 166, 81), [300, 280, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, (204, 55, 55), [300, 320, FLAG_WIDTH, 40])

def draw_japan():
    pygame.draw.rect(screen, WHITE, [300, 240, FLAG_WIDTH, FLAG_HEIGHT])
    pygame.draw.circle(screen, (188, 0, 45), (400, 300), 40)

def draw_hungary():
    pygame.draw.rect(screen, (206, 43, 55), [300, 240, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, WHITE, [300, 280, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, (67, 111, 76), [300, 320, FLAG_WIDTH, 40])

def draw_indonesia():
    pygame.draw.rect(screen, (206, 43, 55), [300, 240, FLAG_WIDTH, 60])
    pygame.draw.rect(screen, WHITE, [300, 300, FLAG_WIDTH, 60])

flags = [
    {"name": "Bangladesh", "draw": draw_bangladesh},
    {"name": "France", "draw": draw_france},
    {"name": "Germany", "draw": draw_germany},
    {"name": "Netherland", "draw": draw_netherland},
    {"name": "Italy", "draw": draw_italy},
    {"name": "Belgium", "draw": draw_belgium},
    {"name": "Bulgaria", "draw": draw_bulgaria},
    {"name": "Japan", "draw": draw_japan},
    {"name": "Hungary", "draw": draw_hungary},
    {"name": "Indonesia", "draw": draw_indonesia},
]

# Function to draw the game screen
def draw_game(flag, options, score, timer):
    screen.fill(BROWN)
    flag["draw"]()
    
    option1_rect = pygame.draw.rect(screen, GREEN, [100, 450, 200, 60])
    option2_rect = pygame.draw.rect(screen, GREEN, [500, 450, 200, 60])

    option1_text = font.render(options[0], True, BLACK)
    option2_text = font.render(options[1], True, BLACK)
    
    screen.blit(option1_text, (option1_rect.x + 20, option1_rect.y + 10))
    screen.blit(option2_text, (option2_rect.x + 20, option2_rect.y + 10))
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (50, 50))

    timer_text = font.render(f"Time: {timer}", True, BLACK)
    screen.blit(timer_text, (650, 50))
    
    pygame.display.flip()

# Function to show the final score screen
def show_final_score(score):
    screen.fill(BROWN)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(final_score_text, (250, 200))

    restart_rect = pygame.draw.rect(screen, GREEN, [200, 350, 150, 60])
    exit_rect = pygame.draw.rect(screen, RED, [450, 350, 150, 60])

    restart_text = font.render("Restart", True, BLACK)
    exit_text = font.render("Exit", True, BLACK)

    screen.blit(restart_text, (restart_rect.x + 20, restart_rect.y + 10))
    screen.blit(exit_text, (exit_rect.x + 50, exit_rect.y + 10))
    
    pygame.display.flip()
    return restart_rect, exit_rect

# Main game loop
def main():
    score = 0
    turns = 5
    clock = pygame.time.Clock()
    
    while turns > 0:
        flag = random.choice(flags)
        correct_option = flag["name"]
        wrong_option = random.choice([f["name"] for f in flags if f != flag])
        options = [correct_option, wrong_option]
        random.shuffle(options)
        
        timer = 10
        answered = False

        while timer > 0:
            clock.tick(60)
            timer -= 1 / 60
            draw_game(flag, options, score, int(timer))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not answered:
                        pos = pygame.mouse.get_pos()
                        if 100 < pos[0] < 300 and 450 < pos[1] < 510:
                            answered = True
                            if options[0] == correct_option:
                                score += 1
                               
                        elif 500 < pos[0] < 700 and 450 < pos[1] < 510:
                            answered = True
                            if options[1] == correct_option:
                                score += 1
                        timer = 0

        turns -= 1

    restart_rect, exit_rect = show_final_score(score)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart_rect.collidepoint(pos):
                    main()
                elif exit_rect.collidepoint(pos):
                    pygame.quit()
                    return

# Run the game
main()
