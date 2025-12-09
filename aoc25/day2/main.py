from typing import Literal
import math


class Solver:
    def __init__(self, expected_task1: int = None, expected_task2: int = None):
        self.expected_task1_test = expected_task1
        self.expected_task2_test = expected_task2

    def task1(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        ranges = self.read_input(filename)
        sum_of_ids = 0
        for low, high in ranges:
            if len(low) == len(high) and len(low) % 2 == 1:
                continue
            new_low = int(low)
            new_high = int(high) + 1
            if (len_low := len(low)) % 2 == 1:
                new_low = 10 ** (len_low)
            if (len_high := len(high)) % 2 == 1:
                new_high = 10 ** (len_high - 1)
            for i in range(new_low, new_high):
                # guaranteed to be even in length, i.e clog10(i) % 2 == 0
                num = str(i)
                midpoint = len(num) // 2
                if num[0:midpoint] == num[midpoint:]:
                    sum_of_ids += i

        return sum_of_ids

    def task2(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        ranges = self.read_input(filename)
        sum_of_ids = 0
        for low, high in ranges:
            for i in range(int(low), int(high) + 1):
                num = str(i)
                len_num = len(num)
                midpoint = len_num // 2
                for substring_len in range(1, midpoint + 1):
                    expected_substrings = math.ceil(len_num / substring_len)
                    subnum = num[0:substring_len]
                    if num.count(subnum) == expected_substrings:
                        sum_of_ids += i
                        break

        return sum_of_ids

    def read_input(self, filename: str):
        ranges: list[tuple[str, str]] = []
        with open(filename, "r") as f:
            for range in f.read().strip().split(","):
                low, high = range.split("-")
                ranges.append((low, high))
        return ranges

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
    solver = Solver(expected_task1=1227775554, expected_task2=4174379265)
    if solver.verify_task(1):
        print(f"Answer task 1: {solver.task1()}")
    if solver.verify_task(2):
        print(f"Answer task 2: {solver.task2()}")
