clock_cycle = [0]
clock_counter = 0
register_value = [1]


with open("input.txt", "r") as f:
    last_val = register_value[0]
    for line in f.readlines():
        operation = line.strip().split(" ")
        if operation[0] == "noop":
            clock_counter += 1
            register_value.append(last_val)
            clock_cycle.append(clock_counter)
        else:
            for _ in range(2):
                clock_counter += 1
                register_value.append(last_val)
                clock_cycle.append(clock_counter)
            last_val += int(operation[1])
    clock_counter += 1
    register_value.append(last_val)
    clock_cycle.append(clock_counter)

# part 1
sum_signal_strength = 0
for i in range(20, 221, 40):
    sum_signal_strength += i * register_value[i]

print(sum_signal_strength)

# part 2

screen = [[" " for _ in range(40)] for _ in range(6)]


def get_pixel(cycle):
    current_pos = register_value[cycle]
    cycle_pos = (cycle - 1) % 40
    if abs(current_pos-cycle_pos) <= 1:
        return "#"
    return "."


def print_screen(buffer):
    for line in buffer:
        print("".join(line))


for y in range(6):
    for x in range(40):
        screen[y][x] = get_pixel(x + 40 * y + 1)

print_screen(screen)
