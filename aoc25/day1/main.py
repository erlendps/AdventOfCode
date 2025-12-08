from typing import Literal


class Solver:
    def __init__(self, expected_task1: int = None, expected_task2: int = None):
        self.expected_task1_test = expected_task1
        self.expected_task2_test = expected_task2

    def task1(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        lines = self.read_input(filename)
        password = 0
        dial = 50
        for line in lines:
            line = line.strip()
            value = int(line[1:])
            value = -value if line[0] == "L" else value
            dial = (dial + value) % 100
            if dial == 0:
                password += 1
        return password

    def task2(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        lines = self.read_input(filename)
        password = 0
        dial = 50
        for line in lines:
            line = line.strip()
            value = int(line[1:])
            password += value // 100
            value = -value if line[0] == "L" else value
            new_dial = (dial + value) % 100
            if line[0] == "L":
                if new_dial > dial and dial != 0:
                    password += 1
                if new_dial == 0:
                    password += 1
            else:
                if new_dial < dial:
                    password += 1
            dial = new_dial

        return password

    def read_input(self, filename: str):
        with open(filename, "r") as f:
            return f.readlines()

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
    solver = Solver(expected_task1=3, expected_task2=6)
    if solver.verify_task(1):
        print(f"Answer task 1: {solver.task1()}")
    if solver.verify_task(2):
        print(f"Answer task 2: {solver.task2()}")
