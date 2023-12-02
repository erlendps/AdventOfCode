def task1():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    total_sum = 0
    for line in lines:
        line = line.strip()
        only_nums = []
        for char in line:
            if char.isnumeric():
                only_nums.append(char)
        total_sum += int(only_nums[0] + only_nums[-1])

    print("Task 1:", total_sum)


def task2():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    total_sum = 0
    sorted_keys = sorted(number_map.keys(), key=lambda x: len(x), reverse=True)

    for line in lines:
        line = line.strip()
        length = len(line)
        i = 0
        num = ""
        while i < length:
            if line[i].isnumeric():
                num += line[i]
                break
            else:
                found = False
                for digit in sorted_keys:
                    str_slice = i + len(digit)
                    if line[i:str_slice] == digit:
                        num += number_map[digit]
                        found = True
                        break
                if found:
                    break
            i += 1

        i = length - 1
        while i >= 0:
            if line[i].isnumeric():
                num += line[i]
                break
            else:
                found = False
                for digit in sorted_keys:
                    str_slice = i - len(digit) + 1
                    if line[str_slice : i + 1] == digit:
                        num += number_map[digit]
                        found = True
                        break
                if found:
                    break
            i -= 1
            print(i)
        print(num)
        total_sum += int(num)

    print(total_sum)


if __name__ == "__main__":
    # task1()
    task2()
