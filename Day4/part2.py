# If they have at least one common element


input_file = open('input.txt', 'r')
lines = input_file.readlines()


number_pairs = 0  # Number of pairs that fully contain the other.


for line in lines:

    pairs = line.strip().split(",")

    firstPair = pairs[0].split("-")

    secondPair = pairs[1].split("-")

    # Because range(1,2) -> [1]
    first = set(range(int(firstPair[0]), int(firstPair[1])+1))
    second = set(range(int(secondPair[0]), int(secondPair[1])+1))

    if first & second:  # If they have at least one common element
        number_pairs += 1


print("Number of pairs -> " + str(number_pairs))
