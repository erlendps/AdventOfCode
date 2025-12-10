from typing import Iterable, Literal


class Solver:
    def __init__(self, expected_task1: int = None, expected_task2: int = None):
        self.expected_task1_test = expected_task1
        self.expected_task2_test = expected_task2

    def get_removable_paper(self, grid: list[Iterable[bool]]):
        permutations = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
        list_of_locations: list[tuple[int]] = []

        def find_num_adjacent(x: int, y: int):
            num = 0
            for permutation in permutations:
                lookup_x = x + permutation[0]
                lookup_y = y + permutation[1]
                if lookup_x == -1 or lookup_y == -1:
                    continue
                try:
                    num += 1 if grid[lookup_y][lookup_x] else 0
                except IndexError:
                    continue
            return num

        width = len(grid[0])
        depth = len(grid)
        for y in range(depth):
            for x in range(width):
                if grid[y][x]:
                    if find_num_adjacent(x, y) < 4:
                        list_of_locations.append((x, y))

        return list_of_locations

    def task1(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        grid = self.read_input(filename)

        return len(self.get_removable_paper(grid))

    def task2(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        grid = self.read_input(filename)

        total_paper = 0
        while True:
            removed_paper = self.get_removable_paper(grid)
            total_paper += len(removed_paper)

            if len(removed_paper) == 0:
                break

            # remove paper, it would be a tiny bit better to remove as soon as possible, i.e. in get_removable_paper
            for location in removed_paper:
                grid[location[1]][location[0]] = False

        return total_paper

    def read_input(self, filename: str):
        # grid is a 2d list where True indicates there is a toilet roll there
        grid: list[Iterable[bool]] = []
        with open(filename, "r") as f:
            for line in f.readlines():
                grid.append(
                    list(map(lambda x: True if x == "@" else False, line.strip()))
                )
        return grid

    def verify_task(self, task_num: Literal[1, 2]):
        print(f"Verifying task {task_num}")
        expected_val = (
            self.expected_task1_test if task_num == 1 else self.expected_task2_test
        )
        task = self.task1 if task_num == 1 else self.task2
        if expected_val is None:
            print("No expected value provided!")
            return False

        if (actual := task(use_test_input=True)) == expected_val:
            print(
                f"Task {task_num} is correct! Expected: {expected_val}. Actual: {actual}."
            )
            return True
        print(
            f"Task {task_num} is NOT correct! Expected: {expected_val}. Actual: {actual}."
        )
        return False


if __name__ == "__main__":
    solver = Solver(expected_task1=13, expected_task2=43)
    if solver.verify_task(1):
        print(f"Answer task 1: {solver.task1()}")
    if solver.verify_task(2):
        print(f"Answer task 2: {solver.task2()}")
