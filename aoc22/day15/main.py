from re import sub
from typing import List


class Sensor:
    def __init__(self, x: int, y: int, bx: int, by: int) -> None:
        self.x = x
        self.y = y
        self.bx = bx
        self.by = by
        self.mhd = abs(x - bx) + abs(y - by)

    def get_tiles_at_y(self, y: int) -> set[tuple]:
        dy = y - self.y
        new_y = self.y + dy
        if abs(dy) > self.mhd:
            return set()
        elif abs(dy) == self.mhd:
            return set([(self.x, new_y)])
        dx = self.mhd - abs(dy)
        s = set()
        for x in range(self.x - dx, self.x + dx + 1):
            s.add((x, new_y))
        return s

    def covers(self, x, y):
        return abs(x - self.x) + abs(y - self.y) <= self.mhd

    def get_right_bound_at_y(self, y):
        dy = y - self.y
        bound_x = self.x + self.mhd - abs(dy)
        bound_y = self.y + dy
        return [bound_x, bound_y]

    def __str__(self) -> str:
        return f"Sensor@x:{self.x},y:{self.y}"

    def __repr__(self) -> str:
        return self.__str__()


def get_sensors(file: str) -> List[Sensor]:
    sensors = []
    with open(file, "r") as f:
        for line in f.readlines():
            x, y, bx, by = tuple([int(sub(r",|:|=|x|y", "", c))
                                  for c in line.strip().split(" ") if "=" in c])
            s = Sensor(x, y, bx, by)
            sensors.append(s)
    return sensors


def part1(file: str, y: int):
    """This solution is quite bad I think"""
    sensors = get_sensors(file)
    no_beacon = set()
    beacons = set()
    for sensor in sensors:
        no_beacon = no_beacon.union(sensor.get_tiles_at_y(y))
        if sensor.by == y:
            beacons.add((sensor.bx, sensor.by))
    no_beacon.difference_update(beacons)
    print(len(no_beacon))


def part2(file: str, limit: int):
    """This however is much smarter."""
    sensors = get_sensors(file)
    position = [0, 0]
    y = 0
    cont = False
    while y <= limit:
        for sensor in sensors:
            if sensor.covers(position[0], position[1]):
                position = sensor.get_right_bound_at_y(position[1])
                if position[0] >= limit:
                    y += 1
                    position = [0, y]
                else:
                    position[0] += 1
                cont = True
                break
        if cont:
            cont = False
            continue
        break
    print("Position:", tuple(position))
    print(position[0] * 4000000 + position[1])


if __name__ == "__main__":
    print("Part 1 Example")
    part1("test.txt", 10)
    print("\nPart 1 Result")
    part1("input.txt", 2000000)
    print("\nPart 2 Example")
    part2("test.txt", 20)
    print("\nPart 2 Result")
    part2("input.txt", 4000000)
