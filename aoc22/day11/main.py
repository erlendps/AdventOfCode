from typing import List


ops = {0: (lambda old: old * 13), 1: (lambda old: old * old), 2: (lambda old: old + 6),
       3: (lambda old: old + 2), 4: (lambda old: old + 3), 5: (lambda old: old + 4),
       6: (lambda old: old + 8), 7: (lambda old: old * 7)}


ops_test = {0: (lambda old: old * 19), 1: (lambda old: old + 6),
            2: (lambda old: old * old), 3: (lambda old: old + 3)}


class Monkey:
    def __init__(self, operation, test: int, choices: tuple) -> None:
        self.operation = operation
        self.test = test
        self.choices = choices
        self.items = []
        self.inspects = 0

    def addItem(self, item):
        self.items.append(item)

    def testItem(self, value):
        if value % self.test == 0:
            return self.choices[0]
        return self.choices[1]

    def inspect(self, lcm):
        self.inspects += 1
        value = self.items.pop(0)
        new_val = self.operation(value)
        # new_val = int(new_val / 3) part 1
        new_val = new_val % lcm
        result = self.testItem(new_val)
        return result, new_val


lines = []
monkeys: List[Monkey] = []

with open("input.txt", "r") as f:
    lines = f.readlines()

lcm = 1
count = 0
for i in range(1, len(lines), 7):
    # test
    test = int(lines[i+2].split(" ")[-1].strip())
    lcm *= test

    # choices
    if_true = int(lines[i+3].split(" ")[-1].strip())
    if_false = int(lines[i+4].split(" ")[-1].strip())
    choices = (if_true, if_false)

    m = Monkey(ops[count], test, choices)

    # items
    items = lines[i].split(":")[1].split(",")
    for j in range(len(items)):
        items[j] = int(items[j].strip())
        m.addItem(items[j])
    count += 1
    monkeys.append(m)

# part 1
for i in range(len(monkeys) * 10000):
    monkey = monkeys[i % len(monkeys)]
    while len(monkey.items) != 0:
        result, value = monkey.inspect(lcm)
        monkeys[result].addItem(value)

highest = 0
next_highest = 0

for i, monkey in enumerate(monkeys, 1):
    num_inspects = monkey.inspects
    print(f"Monkey {i}: {num_inspects}")
    if num_inspects > highest:
        next_highest = highest
        highest = num_inspects
    elif num_inspects > next_highest:
        next_highest = num_inspects

print(highest * next_highest)
