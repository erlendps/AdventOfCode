from typing import Literal
from functools import reduce
from collections.abc import Callable


def reduce_add(x: int, y: int):
    return x + y


def reduce_mul(x: int, y: int):
    return x * y


def interpret_token(token: str):
    try:
        return int(token)
    except ValueError:
        if token == "+":
            return reduce_add
        elif token == "*":
            return reduce_mul
        else:
            raise ValueError("Not a valid operation")


class Solver:
    def __init__(self, expected_task1: int = None, expected_task2: int = None):
        self.expected_task1_test = expected_task1
        self.expected_task2_test = expected_task2

    def task1(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        problems = self.read_input(filename)
        grand_total = 0
        for problem in problems:
            operation: Callable = problem[-1]
            grand_total += reduce(operation, problem[:-1])
        return grand_total

    def task2(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        grand_total = 0
        with open(filename, "r") as f:
            lines = f.readlines()

        # transpose matrix, then there will be an "empty" row indicating a new problem
        # also, each line will represent a number
        transposed_lines = ["".join(row) for row in zip(*lines)]
        problems: list[list[int | Callable]] = [[]]
        i = 0
        for line in transposed_lines:
            if (token := line.strip()) == "":
                # new problem
                problems.append([])
                i += 1
                continue
            elif token.isdigit():
                problems[i].append(int(token))
            else:
                # the operation will always be the first item on the list
                problems[i].append(interpret_token(token[-1]))
                problems[i].append(int(token[:-1]))

        for problem in problems:
            operation = problem[0]
            grand_total += reduce(operation, problem[1:])
        return grand_total

    def read_input(self, filename: str):
        """This only works for task 1"""

        problems: list[list[int | Callable]] = []

        with open(filename, "r") as f:
            for line in f.readlines():
                if len(problems) == 0:
                    problems = list(
                        map(lambda x: [x], map(interpret_token, line.split()))
                    )
                    continue
                for i, token in enumerate(line.split()):
                    problems[i].append(interpret_token(token))

        return problems

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
    solver = Solver(expected_task1=4277556, expected_task2=3263827)
    if solver.verify_task(1):
        print(f"Answer task 1: {solver.task1()}")
    if solver.verify_task(2):
        print(f"Answer task 2: {solver.task2()}")
