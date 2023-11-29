buffer = ""

with open("input.txt") as f:
    buffer = f.read()


def find_n_diff(n):
    for i in range(n-1, len(buffer)):
        substring = buffer[i]
        found = True
        for j in range(1, n):
            if buffer[i-j] in substring:
                found = False
                break
            substring += buffer[i-j]
        if found:
            return i+1
    return -1


# part 1
print(find_n_diff(4))

# part 2
print(find_n_diff(14))
