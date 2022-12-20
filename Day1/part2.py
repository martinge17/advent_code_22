# Create array with one position for each elve.

calories_file = open('input.txt', 'r')
lines = calories_file.readlines()


first, second, third = 0, 0, 0
tmp = 0

for line in lines:

    if line.strip() == "":  # If line is empty -> next elve

        if tmp > first:
            third = second
            second = first
            first = tmp
        elif tmp > second:
            third = second
            second = tmp
        elif tmp > third:
            third = tmp

        tmp = 0
    else:
        tmp += int(line)

total = first+second+third

print("Total top3 calories -> " + str(total))
