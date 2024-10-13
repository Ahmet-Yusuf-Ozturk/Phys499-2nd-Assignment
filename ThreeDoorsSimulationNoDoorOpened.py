# Simulate 3-door game
import random
from math import floor

# Simulate the game N times
# Return the number of times a game player guessed correctly.


def simulate(N):
    correct_guess_count = 0
    for i in range(0, N):
        # Game organizers select a door randomly and places a car behind it
        door_with_car = select_door()
        # Game player selects a door randomly hoping that the car is behind it
        guessed_door_no = select_door()
        # Did the player guess correctly?

        if door_with_car == guessed_door_no:
            correct_guess_count += 1
        else:
            guessed_door_no = change_selection(guessed_door_no)
            # I defined a new function change_selection() below. It handles
            # most of the work.
            if door_with_car == guessed_door_no:
                correct_guess_count += 1
    return correct_guess_count


# Simulate the choice of the door with a car behind it
def select_door():
    # Draw a random number between 0 and 1. If between 0 and 1/3, then
    # door 1 selected, if between 1/3 and 2/3, then door 2, otherwise
    # door 3.
    doors = ["A", "B", "C"]
    r = random.random()*3
    return doors[floor(r)]


def change_selection(chosen_door):
    r = random.random()*2
    door_list = ["A", "B", "C"]
    door_list.remove(chosen_door)  # It removes the chosen door from the list
    # and we can choose another door. For example let door A have the car behind.
    # Let B our initial choice. We remove door B from the list, and we have two
    # choices left. A or C and we choose randomly, either A or C.
    return door_list[floor(r)]


with open("output text file.txt", "w") as f:
    for N in [10**4, 10**5, 10**6]:
        hits = simulate(N)
        print("Percentage of times guess was right = %", round((100.0 * hits) / N, 4))
        f.write("Percentage of times guess was right = %" + str(round((100.0 * hits) / N, 4)) + "\n")
    f.close()
