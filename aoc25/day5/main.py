from typing import Iterable, Literal


class Solver:
    def __init__(self, expected_task1: int = None, expected_task2: int = None):
        self.expected_task1_test = expected_task1
        self.expected_task2_test = expected_task2

    def task1(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        fresh_ranges, ids = self.read_input(filename)
        num_fresh = 0

        for id in ids:
            for start, end in fresh_ranges:
                if id >= start and id <= end:
                    num_fresh += 1
                    break

        return num_fresh

    """_summary_
    First sort the ranges by the minimum value. The idea is to create a new list of non-overlapping ranges. The first range will be the range with the lowest minimum.
    Since fresh_ranges is sorted, we can exploit the fact that if the minimum of the next range is LARGER than our current tail of non-overlapping ranges,
    then all other will be as well. This means that we can create a new range that is guaranteed not to overlap with the tail of non-overlapping ranges and set it as
    the new tail of the non-overlapping ranges array.

    If on the other hand the minimum of the current range is smaller than the maximum of the tail of non-overlapping ranges (and the maximum is larger), then we can
    safely adjust the tail maximum to the current one. If none of these cases are true, then we know the current range is a full subset of the current tail and we
    can safely discard it.
    """

    def task2(self, use_test_input: bool = False) -> int:
        filename = "test.txt" if use_test_input else "input.txt"
        fresh_ranges, _ = self.read_input(filename)
        non_overlapping_ranges: list[list[int]] = []
        fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])

        non_overlapping_ranges.append(fresh_ranges[0])
        nor_index = 0
        for minimum, maximum in fresh_ranges[1:]:
            if (
                minimum <= non_overlapping_ranges[nor_index][1] + 1
                and maximum > non_overlapping_ranges[nor_index][1]
            ):
                non_overlapping_ranges[nor_index][1] = maximum
            elif minimum > non_overlapping_ranges[nor_index][1]:
                nor_index += 1
                non_overlapping_ranges.append([minimum, maximum])

        return sum(map(lambda x: x[1] - x[0] + 1, non_overlapping_ranges))

    def read_input(self, filename: str):
        fresh_id_ranges: list[Iterable[int]] = []
        ingredients: list[int] = []
        with open(filename, "r") as f:
            while True:
                line = f.readline()
                if line == "\n":
                    break
                minimum, maximum = map(lambda x: int(x), line.strip().split("-"))
                fresh_id_ranges.append([minimum, maximum])

            while True:
                line = f.readline()
                if line == "":
                    break
                ingredients.append(int(line.strip()))

        return fresh_id_ranges, ingredients

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
    solver = Solver(expected_task1=3, expected_task2=14)
    if solver.verify_task(1):
        print(f"Answer task 1: {solver.task1()}")
    if solver.verify_task(2):
        print(f"Answer task 2: {solver.task2()}")
