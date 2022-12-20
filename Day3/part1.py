# Pseudocode
# 1. Split string in half
# 2. Check common characters on each half
# 3. Convert characters to priority
# 4. Sum


# Dictionary
full_dictionary = {chr(i+96): i for i in range(1, 27)}
uppercase = {chr(i+64): 26+i for i in range(1, 27)}
full_dictionary.update(uppercase)


input_file = open('input.txt', 'r')
lines = input_file.readlines()

total_priority = 0

for line in lines:

    first_sack = set(line[:len(line)//2])
    second_sack = set(line[len(line)//2:])

    # Get common (intersection)
    common = first_sack.intersection(second_sack)

    # Add priority
    for i in common:
        total_priority += full_dictionary[i]


print("Total priority -> " + str(total_priority))
