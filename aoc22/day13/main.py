from functools import cmp_to_key

lines = []


def compare(left, right):
    if type(left) == list and type(right) == list:
        i = 0
        while i < min(len(left), len(right)):
            result = compare(left[i], right[i])
            if result != 0:
                return result
            i += 1
        if (diff := len(right) - len(left)) > 0:
            return -1
        elif diff == 0:
            return 0
        else:
            return 1
    elif type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    else:
        if type(left) == int:
            return compare([left], right)
        else:
            return compare(left, [right])


with open("input.txt", "r") as f:
    for line in f.readlines():
        if line != "\n":
            line = line.strip()
            line = eval(line)
            lines.append(line)

sum_indexes = 0
for i in range(0, len(lines), 2):
    left = lines[i]
    right = lines[i+1]
    result = compare(left, right)
    if result == -1:
        sum_indexes += (i // 2 + 1)

print(sum_indexes)

# part 2
lines.append([[2]])
lines.append([[6]])
# first sort lines completely
lines.sort(key=cmp_to_key(compare))

# then find indexes
start = lines.index([[2]])
end = lines.index([[6]], start)

print((start + 1) * (end + 1))
