# First define cases

# X -> Need to lose
# Y -> Need to draw
# Z -> Need to win

# Combinations
win = {"A": 'Y', "B": 'Z', "C": 'X'}
lose = {"A": 'Z', "B": 'X', "C": 'Y'}
draw = {"A": 'X', "B": 'Y', "C": 'Z'}

# Round outcome
outcomePoints = {"X": 0, "Y": 3, "Z": 6}
# Shape selected:points
shapePoints = {"X": 1, "Y": 2, "Z": 3}


def round_outcome(rival_shape, desired_outcome):  # Needed shape
    match desired_outcome:
        case "Z":  # Win
            return shapePoints[win[rival_shape]]
        case "X":  # Lose
            return shapePoints[lose[rival_shape]]
        case _:  # Draw
            return shapePoints[draw[rival_shape]]


round_file = open('input.txt', 'r')
lines = round_file.readlines()

total_score = 0

for line in lines:

    round_result = line.replace(" ", "").strip("\n")

    total_score += outcomePoints[round_result[1]] + \
        round_outcome(round_result[0], round_result[1])


print("Total Score -> " + str(total_score))
