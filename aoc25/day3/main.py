from typing import Literal, Iterable


class Solver:
    def __init__(self, expected_task1: int = None, expected_task2: int = None):
        self.expected_task1_test = expected_task1
        self.expected_task2_test = expected_task2

    def task1(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        banks = self.read_input(filename)
        return self.find_joltage(banks, 2)

    def task2(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        banks = self.read_input(filename)
        return self.find_joltage(banks, 12)

    def find_joltage(self, banks: list[tuple[int]], num_batteries_on: int):
        # find the maximum element and it's index. If there are multiple maximums, the first one is selected
        def find_max_and_index_in_range(
            bank_range: Iterable[int], range_start: int, range_end: int
        ):
            m = -1
            index = -1
            for i in range(range_start, range_end):
                num = bank_range[i]
                if num > m:
                    m = num
                    index = i
            return m, index

        bank_len = len(banks[0])
        total_joltage = 0
        # start with the most significant digit and greedily select the maximum (as above) that is within index 0 and bank_len - num_batteries + 1.
        # This ensures we get the maximum possible element while still being able to turn on the required number of batteries.
        # When it is selected, we go onto the next most significant digit and do the same, only with adjusted range.
        # The starting point of the next range should be the next index from the maximum we found in the current iteration, meanwhile the
        # range end should be decremented by 1. Do this for num_batteries_on iterations.
        for bank in banks:
            joltage: list[int] = [0 for _ in range(num_batteries_on)]
            range_start = 0
            range_end = bank_len - num_batteries_on + 1
            for battery in range(num_batteries_on):
                m, index = find_max_and_index_in_range(bank, range_start, range_end)
                joltage[battery] = m
                range_start = index + 1
                range_end += 1

            # sum up joltage for the bank and add
            total_joltage += sum(
                [
                    10 ** (num_batteries_on - joltage_offset - 1)
                    * joltage[joltage_offset]
                    for joltage_offset in range(num_batteries_on)
                ]
            )

        return total_joltage

    def read_input(self, filename: str):
        batteries: list[tuple[int]] = []
        with open(filename, "r") as f:
            for battery in f.readlines():
                batteries.append(tuple(int(c) for c in battery.strip()))
        return batteries

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
    solver = Solver(expected_task1=357, expected_task2=3121910778619)
    if solver.verify_task(1):
        print(f"Answer task 1: {solver.task1()}")
    if solver.verify_task(2):
        print(f"Answer task 2: {solver.task2()}")
