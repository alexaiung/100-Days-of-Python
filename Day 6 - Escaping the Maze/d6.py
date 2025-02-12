# This code must be pasted in https://reeborg.ca/
# It has worked in multiple scenarios, including some that usually
# generates infinite loops
n_turns_right = 0

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if n_turns_right >= 4:
        n_turns_right = 0
        turn_left()
    if right_is_clear():
        turn_right()
        n_turns_right += 1
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        if wall_in_front():
            turn_left()
        move()