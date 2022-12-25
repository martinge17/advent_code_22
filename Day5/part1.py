
import re  # regex
# Ithe same thing can also be done with simple dictionary but using defaultdict is more efficient for such cases.
from collections import defaultdict, deque


def crates_to_stacks(str_crates) -> defaultdict[int, deque[str]]:
    # Since crates has '*', num_stacks only stores the last row
    *crates, num_stacks = str_crates.split("\n")

    # Create dictionary to store the stacks
    stacks = defaultdict(deque)  # Deque -> Double-linked list stack

    for row in reversed(crates):  # Start from bottom
        # Parse each row
        # row[1::4] -> String slicing. Starting at 1 advance 4 positions each time
        for snum, crate in enumerate(row[1::4], start=1):
            if crate.isalpha():  # If its in the alphabet
                stacks[snum].append(crate)

    return stacks


def parse_instruction(instruction):
    movements, src, dst = re.findall("\d+", instruction)
    return int(movements), int(src), int(dst)


def init():
    with open('input.txt', 'r') as file:
        # Space between the crates and the instructions
        crates_str, operations = file.read().split("\n\n")

    # Parse representation to stacks
    crates = crates_to_stacks(crates_str)

    return crates, operations


def main():
    dockyard, operations = init()

    # Execute instructions
    for line in operations.splitlines():
        movements, src, dst = parse_instruction(line)

        for _ in range(movements):
            dockyard[dst].append(dockyard[src].pop())

    # Get top element of each stack
    tops = []
    for stack in dockyard.values():
        tops.append(stack[-1])

    print(''.join(tops))


if __name__ == "__main__":
    main()
