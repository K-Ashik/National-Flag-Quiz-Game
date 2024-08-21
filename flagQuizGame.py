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
YELLOW = (239, 242, 22)
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
    
def draw_argentina():
    # Draw the light blue stripes (top and bottom)
    pygame.draw.rect(screen, (116, 172, 223), [300, 240, FLAG_WIDTH, 40])  # Top blue stripe
    pygame.draw.rect(screen, (116, 172, 223), [300, 320, FLAG_WIDTH, 40])  # Bottom blue stripe

    # Draw the white stripe in the middle
    pygame.draw.rect(screen, WHITE, [300, 280, FLAG_WIDTH, 40])

    # Draw the yellow circle (Sun) in the center of the white stripe
    pygame.draw.circle(screen, (255, 204, 0), (400, 300), 15)
    
def draw_armenia():
    pygame.draw.rect(screen, (206, 43, 55), [300, 240, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, (255, 199, 44), [300, 280, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, (0, 56, 168), [300, 320, FLAG_WIDTH, 40])
    
def draw_austria():
    pygame.draw.rect(screen, (237, 41, 57), [300, 240, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, WHITE, [300, 280, FLAG_WIDTH, 40])
    pygame.draw.rect(screen, (237, 41, 57), [300, 320, FLAG_WIDTH, 40])
    
def draw_chad():
    pygame.draw.rect(screen, (0, 38, 84), [300, 240, 66, FLAG_HEIGHT])
    pygame.draw.rect(screen, (255, 199, 44), [366, 240, 68, FLAG_HEIGHT])
    pygame.draw.rect(screen, (206, 17, 38), [434, 240, 66, FLAG_HEIGHT])

def draw_colombia():
    pygame.draw.rect(screen, (252, 209, 22), [300, 240, FLAG_WIDTH, 60])
    pygame.draw.rect(screen, (0, 56, 168), [300, 300, FLAG_WIDTH, 30])
    pygame.draw.rect(screen, (206, 17, 38), [300, 330, FLAG_WIDTH, 30])
    
def draw_czechia():
    pygame.draw.rect(screen, WHITE, [300, 240, FLAG_WIDTH, 60])          # Top white stripe
    pygame.draw.rect(screen, (215, 20, 26), [300, 300, FLAG_WIDTH, 60])  # Bottom red stripe
    pygame.draw.polygon(screen, (0, 56, 168), [(300, 240), (300, 360), (400, 300)])  # Blue triangle
    
def draw_denmark():
    pygame.draw.rect(screen, (198, 12, 48), [300, 240, FLAG_WIDTH, FLAG_HEIGHT]) # Red background
    pygame.draw.rect(screen, WHITE, [355, 240, 20, FLAG_HEIGHT])                 # Vertical white stripe
    pygame.draw.rect(screen, WHITE, [300, 290, FLAG_WIDTH, 20])                  # Horizontal white stripe


def draw_gambia():
    pygame.draw.rect(screen, (206, 17, 38), [300, 240, FLAG_WIDTH, 40])   # Top red stripe
    pygame.draw.rect(screen, WHITE, [300, 280, FLAG_WIDTH, 10])           # White border
    pygame.draw.rect(screen, (0, 56, 168), [300, 290, FLAG_WIDTH, 30])    # Blue stripe
    pygame.draw.rect(screen, WHITE, [300, 320, FLAG_WIDTH, 10])           # White border
    pygame.draw.rect(screen, (17, 168, 0), [300, 330, FLAG_WIDTH, 30])    # Bottom green stripe

def draw_guinea():
    pygame.draw.rect(screen, (206, 17, 38), [300, 240, 66, FLAG_HEIGHT])  # Left red stripe
    pygame.draw.rect(screen, (252, 209, 22), [366, 240, 68, FLAG_HEIGHT]) # Middle yellow stripe
    pygame.draw.rect(screen, (0, 155, 72), [434, 240, 66, FLAG_HEIGHT])   # Right green stripe
    
def draw_ireland():
    pygame.draw.rect(screen, (22, 155, 98), [300, 240, 66, FLAG_HEIGHT])  # Left green stripe
    pygame.draw.rect(screen, WHITE, [366, 240, 68, FLAG_HEIGHT])          # Middle white stripe
    pygame.draw.rect(screen, (255, 121, 0), [434, 240, 66, FLAG_HEIGHT])  # Right orange stripe
    
def draw_latvia():
    pygame.draw.rect(screen, (128, 0, 0), [300, 240, FLAG_WIDTH, 45])     # Top red stripe
    pygame.draw.rect(screen, WHITE, [300, 285, FLAG_WIDTH, 30])           # Middle white stripe
    pygame.draw.rect(screen, (128, 0, 0), [300, 315, FLAG_WIDTH, 45])     # Bottom red stripe

def draw_luxembourg():
    pygame.draw.rect(screen, (239, 51, 64), [300, 240, FLAG_WIDTH, 40])   # Top red stripe
    pygame.draw.rect(screen, WHITE, [300, 280, FLAG_WIDTH, 40])           # Middle white stripe
    pygame.draw.rect(screen, (97, 161, 199), [300, 320, FLAG_WIDTH, 40])  # Bottom blue stripe

def draw_lithuania():
    pygame.draw.rect(screen, (255, 206, 0), [300, 240, FLAG_WIDTH, 40])   # Top yellow stripe
    pygame.draw.rect(screen, (0, 106, 78), [300, 280, FLAG_WIDTH, 40])    # Middle green stripe
    pygame.draw.rect(screen, (200, 16, 46), [300, 320, FLAG_WIDTH, 40])   # Bottom red stripe

def draw_mali():
    pygame.draw.rect(screen, (0, 136, 81), [300, 240, 66, FLAG_HEIGHT])   # Left green stripe
    pygame.draw.rect(screen, (255, 223, 0), [366, 240, 68, FLAG_HEIGHT])  # Middle yellow stripe
    pygame.draw.rect(screen, (239, 51, 64), [434, 240, 66, FLAG_HEIGHT])  # Right red stripe

def draw_malta():
    pygame.draw.rect(screen, WHITE, [300, 240, 100, FLAG_HEIGHT])         # Left white section
    pygame.draw.rect(screen, (206, 17, 38), [400, 240, 100, FLAG_HEIGHT]) # Right red section
    # Add a grey cross on the white side (top left)
    pygame.draw.rect(screen, (128, 128, 128), [320, 260, 10, 30])         # Vertical cross bar
    pygame.draw.rect(screen, (128, 128, 128), [310, 270, 30, 10])         # Horizontal cross bar

def draw_mauritius():
    pygame.draw.rect(screen, (206, 17, 38), [300, 240, FLAG_WIDTH, 30])   # Top red stripe
    pygame.draw.rect(screen, (0, 32, 161), [300, 270, FLAG_WIDTH, 30])    # Blue stripe
    pygame.draw.rect(screen, (252, 209, 22), [300, 300, FLAG_WIDTH, 30])  # Yellow stripe
    pygame.draw.rect(screen, (0, 128, 58), [300, 330, FLAG_WIDTH, 30])    # Bottom green stripe

def draw_monaco():
    pygame.draw.rect(screen, (206, 17, 38), [300, 240, FLAG_WIDTH, 60])   # Top red stripe
    pygame.draw.rect(screen, WHITE, [300, 300, FLAG_WIDTH, 60])           # Bottom white stripe

def draw_nigeria():
    pygame.draw.rect(screen, (0, 136, 81), [300, 240, 66, FLAG_HEIGHT])   # Left green stripe
    pygame.draw.rect(screen, WHITE, [366, 240, 68, FLAG_HEIGHT])          # Middle white stripe
    pygame.draw.rect(screen, (0, 136, 81), [434, 240, 66, FLAG_HEIGHT])   # Right green stripe

def draw_poland():
    pygame.draw.rect(screen, WHITE, [300, 240, FLAG_WIDTH, 60])           # Top white stripe
    pygame.draw.rect(screen, (206, 17, 38), [300, 300, FLAG_WIDTH, 60])   # Bottom red stripe

def draw_romania():
    pygame.draw.rect(screen, (0, 38, 100), [300, 240, 66, FLAG_HEIGHT])   # Left blue stripe
    pygame.draw.rect(screen, (252, 209, 22), [366, 240, 68, FLAG_HEIGHT]) # Middle yellow stripe
    pygame.draw.rect(screen, (206, 17, 38), [434, 240, 66, FLAG_HEIGHT])  # Right red stripe

def draw_russia():
    pygame.draw.rect(screen, WHITE, [300, 240, FLAG_WIDTH, 40])           # Top white stripe
    pygame.draw.rect(screen, (0, 56, 168), [300, 280, FLAG_WIDTH, 40])    # Middle blue stripe
    pygame.draw.rect(screen, (206, 17, 38), [300, 320, FLAG_WIDTH, 40])   # Bottom red stripe

def draw_sierra_leone():
    pygame.draw.rect(screen, (0, 179, 89), [300, 240, FLAG_WIDTH, 40])    # Top green stripe
    pygame.draw.rect(screen, WHITE, [300, 280, FLAG_WIDTH, 40])           # Middle white stripe
    pygame.draw.rect(screen, (0, 107, 182), [300, 320, FLAG_WIDTH, 40])   # Bottom blue stripe

def draw_uae():
    pygame.draw.rect(screen, (0, 107, 63), [320, 240, FLAG_WIDTH-20, 40])  # Top green stripe
    pygame.draw.rect(screen, WHITE, [320, 280, FLAG_WIDTH-20, 40])         # Middle white stripe
    pygame.draw.rect(screen, (0, 0, 0), [320, 320, FLAG_WIDTH-20, 40])     # Bottom black stripe
    pygame.draw.rect(screen, (206, 17, 38), [300, 240, 20, FLAG_HEIGHT])   # Red vertical stripe on the left

def draw_ukraine():
    pygame.draw.rect(screen, (0, 87, 184), [300, 240, FLAG_WIDTH, 60])    # Top blue stripe
    pygame.draw.rect(screen, (255, 213, 0), [300, 300, FLAG_WIDTH, 60])   # Bottom yellow stripe

def draw_yemen():
    pygame.draw.rect(screen, (206, 17, 38), [300, 240, FLAG_WIDTH, 40])   # Top red stripe
    pygame.draw.rect(screen, WHITE, [300, 280, FLAG_WIDTH, 40])           # Middle white stripe
    pygame.draw.rect(screen, (0, 0, 0), [300, 320, FLAG_WIDTH, 40])       # Bottom black stripe
    
def draw_brazil():
    # Green background
    pygame.draw.rect(screen, (0, 156, 59), [300, 240, FLAG_WIDTH, FLAG_HEIGHT])
    
    # Yellow diamond (diamond has 4 points: top, right, bottom, left)
    pygame.draw.polygon(screen, (255, 223, 0), [(400, 240), (500, 300), (400, 360), (300, 300)])
    
    # Blue circle (in the center of the diamond)
    pygame.draw.circle(screen, (0, 39, 118), (400, 300), 40)
    
    # White banner across the blue circle
    pygame.draw.ellipse(screen, WHITE, [360, 290, 80, 20])
    
    # Small white stars inside the blue circle
    for star_pos in [(390, 290), (410, 290), (400, 300), (380, 310), (420, 310)]:
        pygame.draw.circle(screen, WHITE, star_pos, 3)

def draw_england():
    # White background
    pygame.draw.rect(screen, WHITE, [300, 240, FLAG_WIDTH, FLAG_HEIGHT])
    
    # Red cross - vertical and horizontal stripes
    pygame.draw.rect(screen, (200, 16, 46), [385, 240, 30, FLAG_HEIGHT])  # Vertical red stripe
    pygame.draw.rect(screen, (200, 16, 46), [300, 285, FLAG_WIDTH, 30])   # Horizontal red stripe    

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
    {"name": "Argentina", "draw": draw_argentina},
    {"name": "Armenia", "draw": draw_armenia},
    {"name": "Austria", "draw": draw_austria},
    {"name": "Chad", "draw": draw_chad},
    {"name": "Colombia", "draw": draw_colombia},
    {"name": "Czechia", "draw": draw_czechia},
    {"name": "Denmark", "draw": draw_denmark},
    {"name": "Gambia", "draw": draw_gambia},
    {"name": "Guinea", "draw": draw_guinea},
    {"name": "Ireland", "draw": draw_ireland},
    {"name": "Latvia", "draw": draw_latvia},
    {"name": "Luxembourg", "draw": draw_luxembourg},
    {"name": "Lithuania", "draw": draw_lithuania},
    {"name": "Mali", "draw": draw_mali},
    {"name": "Malta", "draw": draw_malta},
    {"name": "Mauritius", "draw": draw_mauritius},
    {"name": "Monaco", "draw": draw_monaco},
    {"name": "Nigeria", "draw": draw_nigeria},
    {"name": "Poland", "draw": draw_poland},
    {"name": "Romania", "draw": draw_romania},
    {"name": "Russia", "draw": draw_russia},
    {"name": "Sierra Leone", "draw": draw_sierra_leone},
    {"name": "U.A.E.", "draw": draw_uae},
    {"name": "Ukraine", "draw": draw_ukraine},
    {"name": "Yemen", "draw": draw_yemen},
    {"name": "Brazil", "draw": draw_brazil},
    {"name": "England", "draw": draw_england}
]

# Function to draw the game screen
def draw_game(flag, options, score, timer, turn):
    screen.fill(BROWN)
    flag["draw"]()
    
    turn_counter = font.render(f"Flag: {turn}", True, BLACK)
    screen.blit(turn_counter, (50, 50))

    question = font.render(f"Which country flag is this?", True, BLACK)
    screen.blit(question, (250, 150))
    
    option1_rect = pygame.draw.rect(screen, YELLOW, [100, 450, 200, 60])
    option2_rect = pygame.draw.rect(screen, YELLOW, [500, 450, 200, 60])

    option1_text = font.render(options[0], True, BLACK)
    option2_text = font.render(options[1], True, BLACK)
    
    screen.blit(option1_text, (option1_rect.x + 30, option1_rect.y + 20))
    screen.blit(option2_text, (option2_rect.x + 30, option2_rect.y + 20))
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (650, 50))

    timer_text = font.render(f"Timer: {timer}", True, RED)
    screen.blit(timer_text, (350, 50))
    
    pygame.display.flip()


# Function to show the final score screen
def show_final_score(score):
    screen.fill(BROWN)
    final_score_text = font.render(f"Final Score: {score}/10", True, BLACK)
    screen.blit(final_score_text, (320, 250))
    
    #Evaluation message
    if score > 7:
        champ = font.render(f"You are a champ!", True, BLACK)
        screen.blit(champ, (320, 200))
    elif score > 5 and score < 8:
        good = font.render(f"You are a good!", True, BLACK)
        screen.blit(good, (320, 200))
    else:
        bad = font.render(f"You need to improve!", True, BLACK)
        screen.blit(bad, (300, 200))
        
    restart_rect = pygame.draw.rect(screen, GREEN, [200, 350, 150, 60])
    exit_rect = pygame.draw.rect(screen, RED, [450, 350, 150, 60])

    restart_text = font.render("Restart", True, BLACK)
    exit_text = font.render("Exit", True, BLACK)

    screen.blit(restart_text, (restart_rect.x + 20, restart_rect.y + 20))
    screen.blit(exit_text, (exit_rect.x + 50, exit_rect.y + 20))
    
    pygame.display.flip()
    return restart_rect, exit_rect

# Main game loop
def main():
    score = 0
    turns = 1
    clock = pygame.time.Clock()
    listd = []
    while turns <= 10:
        flag = random.choice([f for f in flags if f not in listd])
        correct_option = flag["name"]
        wrong_option = random.choice([f["name"] for f in flags if f != flag])
        options = [correct_option, wrong_option]
        listd.append(flag)
        random.shuffle(options)
        
        timer = 10
        answered = False

        while timer > 0:
            clock.tick(60)
            timer -= 1 / 60
            draw_game(flag, options, score, int(timer), turns)

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

        turns += 1

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
