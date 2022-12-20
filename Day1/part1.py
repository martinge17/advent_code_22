# Create array with one position for each elve.

calories_file = open('input.txt', 'r')
lines = calories_file.readlines()


best_elve = 0
tmp = 0

for line in lines:

    if line.strip() == "":  # If line is empty -> next elve
        if tmp > best_elve:
            best_elve = tmp

        tmp = 0
    else:
        tmp += int(line)


print("Most calories -> " + str(best_elve))
