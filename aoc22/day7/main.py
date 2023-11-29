from typing import List


class ItemNode:
    def __init__(self, name: str, type: str, size: int) -> None:
        self.name = name
        self.type = type
        self.size = size
        self.children: List[ItemNode] = []

    def getChild(self, name, type):
        for child in self.children:
            if child.name == name and child.type == type:
                return child
        return None

    def getSize(self) -> int:
        if len(self.children) == 0:
            return self.size
        size = 0
        for child in self.children:
            size += child.getSize()
        return size

    def addChild(self, name, type, size):
        self.children.append(ItemNode(name, type, size))

    def print_tree(self, indent=0):
        print(" " * (indent - 1), self)
        for child in self.children:
            child.print_tree(indent=indent+4)

    def __str__(self) -> str:
        return f"- {self.name} ({self.type}, size={self.size})"


lines = []
filesystem = ItemNode("root", "dir", 0)
filesystem.addChild("/", "dir", 0)
path_args = []
current_dir = filesystem


with open("input.txt", "r") as f:
    lines = f.readlines()


def get_dir():
    current = filesystem
    for dir in path_args:
        current = current.getChild(dir, "dir")
    return current


def cd(to: str):
    if to == "..":
        path_args.pop()
    else:
        path_args.append(to)
    return get_dir()


def append_dir(name):
    if current_dir.getChild(name, "dir") == None:
        current_dir.addChild(name, "dir", 0)


def append_file(file):
    f = current_dir.getChild(file[1], "file")
    if f != None:
        f.size = int(file[0])
    else:
        current_dir.addChild(file[1], "file", int(file[0]))


def append_item(item):
    if item[0] == "dir":
        append_dir(item[1])
    else:
        append_file(item)


total_sum = 0


def get_sum(current: ItemNode, n):
    global total_sum
    size = current.getSize()
    if size <= n:
        total_sum += size
    for child in current.children:
        if child.type == "dir":
            get_sum(child, n)


for line in lines:
    line = line.strip().split(" ")
    if line[0] == "$" and line[1] == "cd":
        current_dir = cd(line[2])
    elif line[0] == "$":
        continue
    else:
        append_item(line)

filesystem.print_tree()

# part1
get_sum(filesystem.getChild("/", "dir"), 100000)
print(total_sum)

# part2
threshold = 30000000 - (70000000 - filesystem.getChild("/", "dir").getSize())
minimum = 70000000
dir_to_be_deleted = ""


def find_lowest(current: ItemNode):
    global minimum, dir_to_be_deleted
    size = current.getSize()
    if size >= threshold and size < minimum:
        minimum = size
        dir_to_be_deleted = current.name
    for child in current.children:
        if child.type == "dir":
            find_lowest(child)


find_lowest(filesystem.getChild("/", "dir"))

print(threshold)
print(dir_to_be_deleted, minimum)
