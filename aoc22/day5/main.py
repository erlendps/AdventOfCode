from typing import List, Dict


def decode_instruction(instruction: str):
    ins = instruction.split(" ")
    amount = ins[1]
    from_stack = ins[3]
    to_stack = ins[5]
    return (int(amount), int(from_stack), int(to_stack))


# part 1
def cratemover_9000(amount, from_stack, to_stack):
    for _ in range(1, amount + 1):
        crate = crates[from_stack].pop()
        crates[to_stack].append(crate)


# part 2
def cratemover_9001(amount, from_stack, to_stack):
    crates_to_move = crates[from_stack][-amount:]
    crates[from_stack] = crates[from_stack][:-amount]
    crates[to_stack] += crates_to_move


crates: Dict[int, List] = {}

f = open("input.txt", "r")
lines = f.readlines()
f.close()

split_index = lines.index("\n")
for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")

configuration = lines[:split_index-1]
instructions = lines[split_index+1:]

for line in configuration:
    crate_no = 1
    for i in range(1, len(line), 4):
        if line[i].isalpha():
            if crate_no in crates:
                crates[crate_no].insert(0, line[i])
            else:
                crates[crate_no] = [line[i]]
        crate_no += 1

for instruction in instructions:
    amount, from_stack, to_stack = decode_instruction(instruction)
    cratemover_9001(amount, from_stack, to_stack)

output = ""
for i in range(1, len(crates) + 1):
    output += crates[i][-1]

print(output)
