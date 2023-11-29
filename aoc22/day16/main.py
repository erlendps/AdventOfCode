from typing import List
from re import sub


class Valve:
    def __init__(self, id: str, rate: int, leadsTo: List[str]) -> None:
        self.id = id
        self.rate = rate
        self.leadsTo: List[str] = leadsTo

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Valve) and __o.id == self.id

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return self.__str__()


def get_valves(file):
    valves: dict[str, Valve] = {}
    with open(file, "r") as f:
        for line in f.readlines():
            line = line.strip().replace("=", " ")
            line = sub(r";|,", "", line)
            line = line.split(" ")
            valves[line[1]] = Valve(line[1], int(line[5]), line[10:])
    return valves


valves: dict[str, Valve] = {}


def get_leading_to(f: Valve):
    return [valve for valve in valves.values() if valve.id in f.leadsTo]


def bfs(start: Valve, goal: Valve):
    def propogate(parent_graph: dict[str, str], curr: str):
        path = [curr]
        while curr in parent_graph.keys():
            curr = parent_graph[curr]
            path.insert(0, curr)
        return path

    queue = [start]
    explored = [start]
    parent = {}
    while len(queue) != 0:
        current = queue.pop(0)
        if current == goal:
            length = len(propogate(parent, current.id)) - 1
            return length
        for node in get_leading_to(current):
            if node in explored:
                continue
            explored.append(node)
            queue.append(node)
            parent[node.id] = current.id
    return 0


def find_next(start: Valve, to_open: List[Valve], time: int):
    current_max = 0
    current_valve: Valve = None
    time_used = 0

    for valve in to_open:
        dead_time = bfs(start, valve) + 1
        if (score := valve.rate * (time - dead_time) / dead_time) > current_max:
            print(valve, score)
            current_max = score
            current_valve = valve
            time_used = dead_time
    return current_valve, time_used


def search(start: Valve, to_open: List[Valve], time):
    if time <= 1:
        return 0
    if len(to_open) == 0:
        return start.rate * time

    results = []
    for node in to_open:
        new_list = [n for n in to_open if n != node]
        path = bfs(start, node)
        result = start.rate * time + \
            search(node, new_list, time-path-1)
        results.append(result)
    return max(results)


def searth_two_agent(start_a: Valve, start_e: Valve, to_open: List[Valve], time_a, time_e):
    if len(to_open) == 0:
        if start_a == None:
            return start_e.rate * time_e
        elif start_e == None:
            return start_a.rate * time_a
        else:
            return start_a.rate * time_a + start_e.rate * time_e

    results = []
    for node in to_open:
        e_choices = [n for n in to_open if n != node]
        path_a = bfs(start_a, node)
        if len(e_choices) == 0:
            path_e = bfs(start_e, node)
            remaining_time = min(time_a - path_a - 1, time_e - path_e - 1)
            return node.rate * remaining_time
        for choice in e_choices:
            new_list = [n for n in e_choices if n != choice]
            path_e = bfs(start_e, choice)
            result = start_a.rate * time_a + start_e.rate * time_e + \
                searth_two_agent(node, choice, e_choices,
                                 time_a - path_a - 1, time_e - path_e - 1)
            results.append(result)
    return max(results)


def part1(file):
    global valves
    valves = get_valves(file)
    to_open = [valve for valve in valves.values() if valve.rate > 0]
    result = search(valves["AA"], to_open, 30)
    print(result)


def part2(file):
    global valves
    valves = get_valves(file)
    to_open = [valve for valve in valves.values() if valve.rate > 0]
    result = searth_two_agent(valves["AA"], valves["AA"], to_open, 26, 26)
    print(result)


if __name__ == "__main__":
    print("Part 1 Test")
    part1("test.txt")
    #print("Part 1 Results")
    # part1("input.txt")
    print("Part 2 Example")
    part2("test.txt")
