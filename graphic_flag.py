from turtle import *

def draw_bangladesh_flag():
    # Drawing the green background
    bgcolor("grey")
    up()
    goto(-300, 150)
    down()
    color("green")
    begin_fill()
    for _ in range(2):
        fd(600)
        rt(90)
        fd(300)
        rt(90)
    end_fill()

    # Drawing the red circle
    up()
    goto(0, -90)
    down()
    color("red")
    begin_fill()
    circle(90)  # Radius of the circle
    end_fill()

def draw_germany_flag():
    # Draw the black stripe
    bgcolor("grey")
    up()
    goto(-300, 100)
    down()
    color("black")
    begin_fill()
    for _ in range(2):
        fd(600)
        rt(90)
        fd(100)
        rt(90)
    end_fill()

    # Draw the red stripe
    up()
    goto(-300, 0)
    down()
    color("red")
    begin_fill()
    for _ in range(2):
        fd(600)
        rt(90)
        fd(100)
        rt(90)
    end_fill()

    # Draw the yellow stripe
    up()
    goto(-300, -100)
    down()
    color("yellow")
    begin_fill()
    for _ in range(2):
        fd(600)
        rt(90)
        fd(100)
        rt(90)
    end_fill()

# Interactive User Input
print("Which flag would you like to draw?")
print("1: Bangladesh")
print("2: Germany")
flag_choice = input("Please enter the number corresponding to your choice (1 or 2): ").strip()

# Drawing the chosen flag
if flag_choice == "1":
    draw_bangladesh_flag()
elif flag_choice == "2":
    draw_germany_flag()
else:
    print("Invalid choice! Please enter either '1' for Bangladesh or '2' for Germany.")

done()
