import turtle
import time
import random

def draw_environment(x_offset, y_offset, ground_y):

    # Moon
    t.pencolor("gray")
    t.penup()
    t.goto(x_offset - 250, y_offset + 100)
    t.dot(40)
    
    # Stars
    t.pencolor("white")
    for _ in range(30):
        x_star = random.randint(-400, 400)
        y_star = random.randint(ground_y + 20, 300)
        size = random.randint(2, 4)
        t.goto(x_star, y_star)
        t.dot(size)

    # Ground
    t.pencolor("white")
    t.goto(x_offset - 400, ground_y)
    t.pendown()
    t.goto(x_offset + 400, ground_y)

def draw_blood_splatter(x, y):

    t.penup()
    t.pencolor("darkred")
    for _ in range(15):
        t.goto(x, y)
        angle = random.randint(0, 360)
        distance = random.randint(5, 20)
        t.setheading(angle)
        t.forward(distance)
        t.dot(random.randint(2, 5))

def draw_sword(x, y, angle=45):

    t.pencolor("silver")
    t.pensize(3)
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.pencolor("brown") # Hilt
    t.forward(15)
    t.pencolor("gold") # Guard
    t.left(90)
    t.forward(7)
    t.backward(14)
    t.forward(7)
    t.right(90)
    t.pencolor("silver") # Blade
    t.forward(50)

def draw_stickman(
    x, y, color,
    pose="stand", run_phase=0
):

    t.setheading(0)
    t.pencolor(color)
    t.pensize(5)
    
    if pose == "dead":
        t.penup()
        t.goto(x - 30, y)
        t.pendown()
        t.forward(100)
        t.dot(30)
        t.backward(50)
        t.left(45)
        t.forward(40)
        t.backward(40)
        t.right(90)
        t.forward(40)
        return

    hip_y = y + 50
    body_top_y = y + 100

    # Draw Torso and Head
    t.penup()
    t.goto(x, hip_y)
    t.pendown()
    t.goto(x, body_top_y)
    t.dot(30)
    
    # Add Ninja "Rags" for the blue stickman
    if color == "deepskyblue":
        # Headband
        t.pensize(8)
        t.penup()
        t.goto(x - 14, body_top_y + 5)
        t.pendown()
        t.goto(x + 14, body_top_y + 5)
        t.pensize(5) # Reset pensize
        
        # Lower face covering
        t.penup()
        t.goto(x - 8, body_top_y - 5)
        t.pendown()
        t.begin_fill()
        t.goto(x + 8, body_top_y - 5)
        t.goto(x, body_top_y - 15)
        t.goto(x - 8, body_top_y - 5)
        t.end_fill()

    t.penup()
    t.goto(x, body_top_y - 20) # Go to neck to draw arms
    t.pendown()

    # Draw Arms and Legs based on pose
    if pose == "stand":
        t.goto(x - 30, body_top_y - 40)
        t.penup()
        t.goto(x, body_top_y - 20)
        t.pendown()
        t.goto(x + 30, body_top_y - 40)
    elif pose == "run":
        # Arms swept back
        t.goto(x - 30, body_top_y - 30)
        t.penup()
        t.goto(x, body_top_y - 20)
        t.pendown()
        t.goto(x - 35, body_top_y - 40)
        
        # Dynamic running with one foot lifted
        t.penup()
        if run_phase == 0:
            # Right leg planted, left leg lifted
            t.goto(x, hip_y)
            t.pendown()
            t.goto(x + 20, y) 
            t.penup()
            t.goto(x, hip_y)
            t.pendown()
            t.goto(x - 15, y + 20) # Lifted foot
        else:
            # Left leg planted, right leg lifted
            t.goto(x, hip_y)
            t.pendown()
            t.goto(x - 20, y)
            t.penup()
            t.goto(x, hip_y)
            t.pendown()
            t.goto(x + 15, y + 20) # Lifted foot
    elif pose == "reach_for_sword":
        t.goto(x - 20, body_top_y + 5)
        t.penup()
        t.goto(x, body_top_y - 20)
        t.pendown()
        t.goto(x + 30, body_top_y - 40)
    elif pose == "sword_stance" or pose == "slash":
        angle = -45 if pose == "sword_stance" else 10
        hand_x = x + 40 if pose == "sword_stance" else x + 55
        hand_y = body_top_y - 40 if pose == "sword_stance" else body_top_y - 30
        t.goto(hand_x, hand_y)
        t.penup()
        t.goto(x, body_top_y - 20)
        t.pendown()
        t.goto(x - 20, body_top_y - 40)
        draw_sword(hand_x, hand_y, angle)

    # Draw standard legs for all poses except 'run'
    if pose != "run":
        t.penup()
        t.goto(x, hip_y)
        t.pendown()
        t.goto(x - 20, y)
        t.penup()
        t.goto(x, hip_y)
        t.pendown()
        t.goto(x + 20, y)

def draw_scene(p1_pos, p2_pos, p1_pose, p2_pose, p1_run_phase=0, blood_pos=None):
    """Clears the screen and redraws all elements for a new frame."""
    t.clear()
    draw_environment(X_OFFSET, Y_OFFSET, GROUND_Y)
    draw_stickman(
        p1_pos[0], p1_pos[1], "deepskyblue", p1_pose, run_phase=p1_run_phase
    )
    draw_stickman(
        p2_pos[0], p2_pos[1], "red", p2_pose
    )
    if blood_pos:
        draw_blood_splatter(blood_pos[0], blood_pos[1])
    screen.update()

def main():
    """Runs the main animation sequence."""
    time.sleep(1)
    p1 = [P1_X, GROUND_Y]
    p2 = [P2_X, GROUND_Y]
    p1_pose = "stand"
    p2_pose = "stand"
    
    # Scene 1: Initial Standoff
    draw_scene(p1, p2, p1_pose, p2_pose)
    time.sleep(1)

    p1_pose = "run"
    
    # Scene 2: P1 runs, P2 reacts
    run_cycle = 0
    drew_sword = False
    ATTACK_RANGE = 70
    
    while p2[0] - p1[0] > ATTACK_RANGE:
        p1[0] += 12 # Increased speed slightly
        run_cycle += 1
        
        if not drew_sword and p2[0] - p1[0] < 200:
            p2_pose = "reach_for_sword"
            draw_scene(p1, p2, p1_pose, p2_pose, p1_run_phase=run_cycle % 2)
            time.sleep(0.3)
            p2_pose = "sword_stance"
            drew_sword = True

        draw_scene(p1, p2, p1_pose, p2_pose, p1_run_phase=run_cycle % 2)
        time.sleep(0.06)

    # Scene 3: The Kill
    p2_pose = "slash"
    p1_pose = "dead"
    p2[0] -= 15 # P2 lunges slightly
    impact_pos = [p1[0] + 20, GROUND_Y + 70]
    
    draw_scene(p1, p2, p1_pose, p2_pose, blood_pos=impact_pos)
    t.penup()
    t.goto(impact_pos[0] - 15, impact_pos[1] + 20)
    t.pencolor("red")
    t.write("SPLAT!", font=("Arial", 20, "bold"))
    screen.update()
    time.sleep(1.5)

    # Scene 4: Aftermath
    p2_pose = "sword_stance"
    p2[0] += 15 # P2 retracts lunge
    draw_scene(p1, p2, p1_pose, p2_pose)
    time.sleep(2)

    # End credits at the top
    t.pencolor("gold")
    t.penup()
    t.goto(0, 250)
    t.write(
        "Thanks for Watching",
        align="center",
        font=("Arial", 36, "bold")
    )
    screen.update()

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Stickman Duel Animation")
    screen.tracer(0)
    t = turtle.Turtle()
    t.hideturtle()
    
    # Global position settings
    X_OFFSET = 0
    Y_OFFSET = 0
    GROUND_Y = -150 + Y_OFFSET
    P1_X = -350 + X_OFFSET
    P2_X = 150 + X_OFFSET
    
    main()
    turtle.done()