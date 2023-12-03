def get_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def is_symbol(char: str):
    return char != "."


def is_adjacent(i, j, last_line, current_line, next_line):
    local_indexes = (i - 1 if i > 0 else i, j + 1 if j < len(current_line) - 1 else j)
    if (i > 0 and is_symbol(current_line[i - 1])) or (
        j < len(current_line) - 1 and is_symbol(current_line[j + 1])
    ):
        return True
    elif last_line and any(
        [is_symbol(char) for char in last_line[local_indexes[0] : local_indexes[1] + 1]]
    ):
        return True
    elif next_line and any(
        [is_symbol(char) for char in next_line[local_indexes[0] : local_indexes[1] + 1]]
    ):
        return True
    return False


def task1(filename):
    lines = get_lines(filename)
    num_lines = len(lines)

    num_sum = 0

    for l in range(num_lines):
        last_line = lines[l - 1] if l > 0 else None
        current_line = lines[l]
        next_line = lines[l + 1] if l < num_lines - 1 else None
        current_num = ""
        i = 0
        while i < len(current_line):
            if not current_line[i].isnumeric():
                if l == 0:
                    print(i, current_line[i])
                i += 1
                continue
            else:
                current_num += current_line[i]
                j = i + 1
                while j < len(current_line) and current_line[j].isnumeric():
                    current_num += current_line[j]
                    j += 1
                j -= 1
                if is_adjacent(i, j, last_line, current_line, next_line):
                    num_sum += int(current_num)
                current_num = ""
                i = j + 1

    print(num_sum)


def find_nums_in_line(line):
    if not line:
        return None
    line_length = len(line)
    j = 0
    current_num = ""
    nums = []
    while j < line_length:
        if not line[j].isnumeric():
            j += 1
            continue
        h = j + 1
        current_num += line[j]
        while h < line_length and line[h].isnumeric():
            current_num += line[h]
            h += 1
        number = {
            "num": int(current_num),
            "start": j - 1 if j > 0 else j,
            "stop": h if h < line_length else h - 1,
        }
        nums.append(number)
        current_num = ""
        j = h
    return nums


def task2(filename):
    lines = get_lines(filename)
    num_lines = len(lines)
    line_length = len(lines[0])

    gear_sum = 0

    nums_in_last = []
    nums_in_current = find_nums_in_line(lines[0])

    for l in range(num_lines):
        current_line = lines[l]
        next_line = lines[l + 1] if l < num_lines - 1 else None
        nums_in_next = find_nums_in_line(next_line)
        i = 0
        num_adjacent = 0
        product = 1

        while i < line_length:
            if current_line[i] != "*":
                i += 1
                continue
            # potential gear
            # find above
            for num in nums_in_last:
                if i >= num["start"] and i <= num["stop"]:
                    num_adjacent += 1
                    if num_adjacent > 2:
                        break
                    product *= num["num"]

            for num in nums_in_current:
                if i == num["stop"] or i == num["start"]:
                    num_adjacent += 1
                    if num_adjacent > 2:
                        break
                    product *= num["num"]

            for num in nums_in_next:
                if i >= num["start"] and i <= num["stop"]:
                    num_adjacent += 1
                    if num_adjacent > 2:
                        break
                    product *= num["num"]

            if num_adjacent == 2:
                gear_sum += product

            product = 1
            num_adjacent = 0
            i += 1

        nums_in_last = nums_in_current
        nums_in_current = nums_in_next
    print(gear_sum)


if __name__ == "__main__":
    task1("input.txt")
    task2("input.txt")
