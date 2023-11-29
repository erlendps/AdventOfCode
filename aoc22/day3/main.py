import string

priority_map = {}

for i, letter in enumerate(string.ascii_letters, start=1):
    priority_map[letter] = i

score_part1 = 0
score_part2 = 0

# part 1
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        length = len(line)
        first_half = line[:length//2]
        second_half = line[length//2:]
        for item in first_half:
            if item in second_half:
                score_part1 += priority_map[item]
                break

print(score_part1)

# part 2
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines) - 1, 3):
        line1 = lines[i].strip()
        line2 = lines[i+1].strip()
        line3 = lines[i+2].strip()
        for item in line1:
            if item in line2 and item in line3:
                score_part2 += priority_map[item]
                break

print(score_part2)
