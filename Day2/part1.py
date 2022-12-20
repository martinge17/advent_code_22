# First define cases

# Round outcome
win = ['AY', 'BZ', 'CX']  # 6 points
draw = ['AX', 'BY', 'CZ']  # 3 points

# Shape selected:points
shapePoints = {"X": 1, "Y": 2, "Z": 3}


def round_outcome(outcome):
    if str(outcome) in win:
        return 6
    if str(outcome) in draw:
        return 3
    else:
        return 0


round_file = open('input.txt', 'r')
lines = round_file.readlines()

total_score = 0

for line in lines:

    round_result = line.replace(" ", "").strip("\n")

    total_score += shapePoints[round_result[1]] + round_outcome(round_result)


print("Total Score -> " + str(total_score))
