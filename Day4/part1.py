
def check_pair_cointains(firstPair, secondPair):

    if (int(firstPair[0]) <= int(secondPair[0])) and (int(firstPair[1]) >= int(secondPair[1])):  # Ex: 2-8 3-7
        return True
    if (int(firstPair[0]) >= int(secondPair[0])) and (int(firstPair[1]) <= int(secondPair[1])):  # Ex: 6-6 4-6
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
