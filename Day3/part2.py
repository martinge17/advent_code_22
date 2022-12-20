# Pseudocode
# 1. Check common on each  group
# 4. Sum


# Dictionary
full_dictionary = {chr(i+96): i for i in range(1, 27)}
uppercase = {chr(i+64): 26+i for i in range(1, 27)}
full_dictionary.update(uppercase)


input_file = open('input.txt', 'r')
lines = input_file.readlines()

total_priority = 0

splited = []
group = ""
i = 1

for line in lines:

    if (i % 3 == 0):  # If empty line -> Check repeated and ..... At least 3 times

        group += line

        # https://stackoverflow.com/questions/70480885/find-common-character-in-list-of-strings

        splited = group.split()

        common = set.intersection(*map(set, splited))

        badge = list(common)[0]

        # Add priority
        if badge != None:
            total_priority += full_dictionary[badge]

        group = ""

    else:
        group += line  # Concat lines of a group

    i += 1

print("Total priority -> " + str(total_priority))
