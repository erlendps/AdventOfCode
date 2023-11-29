# part 1

from typing import List


num_fully_contained = 0


def is_fully_contained(range1: List[int], range2: List[int]):
    return range1[0] >= range2[0] and range1[1] <= range2[1] \
        or range2[0] >= range1[0] and range2[1] <= range1[1]


def is_overlapping(range1: List[int], range2: List[int]):
    return range1[0] >= range2[0] and range1[0] <= range2[1] \
        or range2[0] >= range1[0] and range2[0] <= range1[1]


with open("input.txt", "r") as f:
    for line in f.readlines():
        # string cleaning
        line = line.strip()
        pair = line.split(",")
        elf_1 = pair[0].split("-")
        elf_2 = pair[1].split("-")
        for i in range(2):
            elf_1[i] = int(elf_1[i])
            elf_2[i] = int(elf_2[i])
        if is_fully_contained(elf_1, elf_2):
            num_fully_contained += 1

print(num_fully_contained)


# part 2

num_overlapping = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        # string cleaning
        line = line.strip()
        pair = line.split(",")
        elf_1 = pair[0].split("-")
        elf_2 = pair[1].split("-")
        for i in range(2):
            elf_1[i] = int(elf_1[i])
            elf_2[i] = int(elf_2[i])
        if is_overlapping(elf_1, elf_2):
            num_overlapping += 1

print(num_overlapping)
