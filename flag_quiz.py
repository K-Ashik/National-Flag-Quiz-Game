import turtle
import random
import time

# Screen Setup
screen = turtle.Screen()
screen.title("Flag Quiz Game")
screen.bgcolor("grey")
screen.setup(width=800, height=600)

# Turtle for drawing flags
flag_turtle = turtle.Turtle()
flag_turtle.hideturtle()
flag_turtle.speed(0)

# Turtle for showing messages and options
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.speed(0)

# List of available flags
flags = ["Bangladesh", "Germany", "France", "Belgium", "Japan"]

# Drawing flags
def draw_bangladesh_flag():
    flag_turtle.clear()
    flag_turtle.up()
    flag_turtle.goto(-150, 100)
    flag_turtle.down()
    flag_turtle.color("green")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(300)
        flag_turtle.rt(90)
        flag_turtle.fd(200)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

    flag_turtle.up()
    flag_turtle.goto(0, -50)
    flag_turtle.down()
    flag_turtle.color("red")
    flag_turtle.begin_fill()
    flag_turtle.circle(50)
    flag_turtle.end_fill()

def draw_germany_flag():
    flag_turtle.clear()
    flag_turtle.up()
    flag_turtle.goto(-150, 100)
    flag_turtle.down()
    flag_turtle.color("black")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(300)
        flag_turtle.rt(90)
        flag_turtle.fd(67)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

    flag_turtle.up()
    flag_turtle.goto(-150, 33)
    flag_turtle.down()
    flag_turtle.color("red")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(300)
        flag_turtle.rt(90)
        flag_turtle.fd(67)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

    flag_turtle.up()
    flag_turtle.goto(-150, -34)
    flag_turtle.down()
    flag_turtle.color("yellow")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(300)
        flag_turtle.rt(90)
        flag_turtle.fd(67)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

def draw_france_flag():
    flag_turtle.clear()
    flag_turtle.up()
    flag_turtle.goto(-150, 100)
    flag_turtle.down()
    
    # Draw blue stripe
    flag_turtle.color("blue")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(100)
        flag_turtle.rt(90)
        flag_turtle.fd(200)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

    flag_turtle.fd(100)
    
    # Draw white stripe
    flag_turtle.color("white")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(100)
        flag_turtle.rt(90)
        flag_turtle.fd(200)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

    flag_turtle.fd(100)
    
    # Draw red stripe
    flag_turtle.color("red")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(100)
        flag_turtle.rt(90)
        flag_turtle.fd(200)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

def draw_belgium_flag():
    flag_turtle.clear()
    flag_turtle.up()
    flag_turtle.goto(-150, 100)
    flag_turtle.down()

    # Draw black stripe
    flag_turtle.color("black")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(100)
        flag_turtle.rt(90)
        flag_turtle.fd(200)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

    flag_turtle.fd(100)

    # Draw yellow stripe
    flag_turtle.color("yellow")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(100)
        flag_turtle.rt(90)
        flag_turtle.fd(200)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

    flag_turtle.fd(100)

    # Draw red stripe
    flag_turtle.color("red")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(100)
        flag_turtle.rt(90)
        flag_turtle.fd(200)
        flag_turtle.rt(90)
    flag_turtle.end_fill()

def draw_japan_flag():
    flag_turtle.clear()
    flag_turtle.up()
    flag_turtle.goto(-150, 100)
    flag_turtle.down()
    flag_turtle.color("white")
    flag_turtle.begin_fill()
    for _ in range(2):
        flag_turtle.fd(300)
        flag_turtle.rt(90)
        flag_turtle.fd(200)
        flag_turtle.rt(90)
    flag_turtle.end_fill()
    
    # Draw red circle in the middle
    flag_turtle.up()
    flag_turtle.goto(0, -50)
    flag_turtle.down()
    flag_turtle.color("red")
    flag_turtle.begin_fill()
    flag_turtle.circle(50)
    flag_turtle.end_fill()

# List of flag functions
flag_functions = {
    "Bangladesh": draw_bangladesh_flag,
    "Germany": draw_germany_flag,
    "France": draw_france_flag,
    "Belgium": draw_belgium_flag,
    "Japan": draw_japan_flag
}

# Global variables for the game
score = 0
current_flag = None
flags_to_show = random.sample(flags, 5)
current_question = 0
options = []

# Function to display text options on screen
def display_options(option1, option2):
    text_turtle.clear()
    text_turtle.up()
    text_turtle.goto(-150, -250)  # Left option
    text_turtle.write(f"1: {option1}", font=("Arial", 24, "normal"))
    
    text_turtle.goto(50, -250)  # Right option
    text_turtle.write(f"2: {option2}", font=("Arial", 24, "normal"))



# Function to randomly display a flag and options
def show_next_flag():
    global current_flag, options
    if current_question >= len(flags_to_show):
        end_quiz()
        return

    current_flag = flags_to_show[current_question]
    countries = list(flag_functions.keys())
    wrong_flag = random.choice([country for country in countries if country != current_flag])
    
    # Randomize the positions of options
    options = [current_flag, wrong_flag]
    random.shuffle(options)
    
    # Draw the flag
    flag_functions[current_flag]()
    
    # Display options
    display_options(options[0], options[1])

# Check the answer based on the click location
def check_answer(x, y):
    global score, current_question
    if -200 < x < -100 and -270 < y < -230:  # Option 1
        selected_option = options[0]
    elif 0 < x < 100 and -270 < y < -230:  # Option 2
        selected_option = options[1]
    else:
        return
    
    if selected_option == current_flag:
        text_turtle.goto(0, 250)
        text_turtle.write("🎉 Correct!", align="center", font=("Arial", 24, "normal"))
        score += 1
    else:
        text_turtle.goto(0, 250)
        text_turtle.write("😞 Wrong!", align="center", font=("Arial", 24, "normal"))
    
    time.sleep(1)
    text_turtle.clear()
    current_question += 1
    show_next_flag()

# Function to end the quiz
def end_quiz():
    text_turtle.clear()
    
    if current_question == 0:
        return

    percentage_correct = (score / current_question) * 100
    
    # Determine performance
    if score == len(flags_to_show):
        medal = "🏅 Gold Medal"
    elif percentage_correct > 0:
        medal = "🥉 Bronze Medal"
    else:
        medal = "🦆 Duck"
    
    result_message = f"Quiz Ended! You scored: {score}/{len(flags_to_show)}\n{medal}"
    text_turtle.goto(0, 250)
    text_turtle.write(result_message, align="center", font=("Arial", 24, "normal"))

# Starting the quiz
def start_quiz():
    show_next_flag()
    
    # Set up the click event for choosing options
    screen.onscreenclick(check_answer)

# Set up the screen to restart game manually
button_turtle = turtle.Turtle()
button_turtle.hideturtle()
button_turtle.speed(0)
button_turtle.penup()




# Start the game
start_quiz()

# Keep the window open
screen.mainloop()
