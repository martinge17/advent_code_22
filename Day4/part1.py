
def check_pair_cointains(firstPair, secondPair):

    print(firstPair[0], firstPair[1])

    if (firstPair[0] <= secondPair[0]) and (firstPair[1] >= secondPair[1]):
        return True
    if (secondPair[0] <= firstPair[0]) and (secondPair[1] >= firstPair[1]):
        return True


input_file = open('input.txt', 'r')
lines = input_file.readlines()


number_pairs = 0  # Number of pairs that fully contain the other.


for line in lines:

    pairs = line.strip().split(",")

    firstPair = pairs[0].split("-")

    secondPair = pairs[1].split("-")

    if check_pair_cointains(firstPair, secondPair):
        number_pairs += 1


print("Number of pairs -> " + str(number_pairs))

# TODO: NOn funciona conta de mais.
