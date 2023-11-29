elves_calories = []
i = 0
current_elf = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            elves_calories.append(current_elf)
            current_elf = 0
            continue
        current_elf += int(line[:-1])

elves_calories.sort(reverse=True)

print(sum(elves_calories[:3]))

