from turtle import *
import time

# --- Setup the animation stage ---
setup(800, 400)       # Create a wide screen for the fight
bgcolor("black")
hideturtle()
tracer(0)             # Turn off automatic screen updates for smooth animation
pensize(3)

# --- A function to draw one stickman in a fighting pose ---
def draw_fighter(x, y, color, is_attacking, is_hit=False):
    pencolor(color)
    penup()
    goto(x, y)
    
    # Body
    setheading(90)
    pendown()
    forward(50)
    
    # Head
    right(90)
    circle(15)
    
    # Legs (different poses for attacking or standing)
    if is_attacking:
        right(135)
        forward(40)
        penup()
        goto(x, y)
        pendown()
        right(90)
        forward(40)
    else:
        right(135)
        forward(40)
        penup()
        goto(x, y)
        pendown()
        left(90)
        forward(40)
        
    # Arms and Sword (the most important part!)
    penup()
    goto(x, y + 40) # Go to shoulder height
    pencolor("silver")
    if is_hit:
        # If hit, drop the sword
        setheading(-45)
        forward(20)
    else:
        # Otherwise, hold the sword
        setheading(45 if color == "cyan" else 135)
        pendown()
        forward(60)

# --- A function to draw the "fallen" stickman ---
def draw_fallen_fighter(x, y, color):
    pencolor(color)
    penup()
    goto(x, y - 20)
    
    # Body and limbs on the ground
    setheading(0)
    pendown()
    forward(40)
    left(120)
    forward(30)
    backward(30)
    right(180)
    forward(30)
    penup()
    goto(x + 40, y - 20)
    pendown()
    circle(15)
    
    # Dropped sword
    penup()
    goto(x + 10, y)
    pencolor("silver")
    setheading(-20)
    pendown()
    forward(60)

# --- A function to draw a "victory" pose ---
def draw_victory_pose(x, y, color):
    # Draw the fighter standing normally
    draw_fighter(x, y, color, is_attacking=False)
    # Redraw the sword arm in a raised position
    penup()
    goto(x, y + 40) # Shoulder height
    pencolor("silver")
    setheading(90)  # Sword pointing straight up
    pendown()
    forward(60)


# --- The Fight Animation Storyboard ---
def run_fight_scene():
    # Scene 1: Face off
    clear()
    draw_fighter(-100, 0, "cyan", False)
    draw_fighter(100, 0, "orange", False)
    update()
    time.sleep(1)
    
    # Scene 2: Cyan attacks, Orange defends
    clear()
    draw_fighter(-60, 0, "cyan", True) # Cyan moves forward
    draw_fighter(100, 0, "orange", False)
    update()
    time.sleep(0.5)

    # Scene 3: The parry! (Swords clash)
    clear()
    # Draw them close together, swords meeting
    draw_fighter(-40, 0, "cyan", False)
    draw_fighter(40, 0, "orange", False)
    update()
    time.sleep(0.7)
    
    # Scene 4: Orange strikes the final blow!
    clear()
    draw_fighter(0, 0, "orange", True)   # Orange lunges
    draw_fighter(-80, 0, "cyan", False, is_hit=True) # Cyan is hit
    update()
    time.sleep(0.3)
    
    # Scene 5: Victory!
    clear()
    draw_victory_pose(80, 0, "orange") # Winner's pose
    draw_fallen_fighter(-80, 0, "cyan") # Loser on the ground
    update()

# --- Run the animation ---
run_fight_scene()
done()