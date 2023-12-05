def task1(filename):
    with open(filename, "r") as f:
        seeds, *almanacs = f.read().split("\n\n")

    seeds = list(map(int, seeds.removeprefix("seeds:").strip().split()))

    for almanac in almanacs:
        ranges = []
        for line in almanac.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))

        next_seeds = []
        for seed in seeds:
            for dst, src, r in ranges:
                if src <= seed < src + r:
                    next_seeds.append(seed - src + dst)
                    # break early since we found for this seed
                    break
            else:
                next_seeds.append(seed)
        # update seeds to the next stage
        seeds = next_seeds

    print("Minimum location is:", min(seeds))


def task2(filename):
    with open(filename, "r") as f:
        seeds_line, *almanacs = f.read().split("\n\n")

    seeds_line = list(map(int, seeds_line.removeprefix("seeds:").strip().split()))
    seeds = [(i, i + j) for i, j in zip(seeds_line[0::2], seeds_line[1::2])]

    for almanac in almanacs:
        ranges = []
        for line in almanac.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))

        next_seeds = []

        while seeds:
            seed_start, seed_end = seeds.pop()

            for dst, src, r in ranges:
                overlap_start = max(seed_start, src)
                overlap_end = min(seed_end, src + r)

                # check if overlapping
                if overlap_start < overlap_end:
                    # add overlapping seed
                    next_seeds.append(
                        (overlap_start - src + dst, overlap_end - src + dst)
                    )
                    # add potential seed on left
                    if overlap_start > seed_start:
                        seeds.append((seed_start, overlap_start))

                    # add potential seed on the right
                    if overlap_end < seed_end:
                        seeds.append((overlap_end, seed_end))

                    # break for this seed
                    break
            else:
                # no overlap found
                next_seeds.append((seed_start, seed_end))

        seeds = next_seeds

    print("Minimum range is:", min(seeds, key=lambda x: x[0]))


if __name__ == "__main__":
    task1("input.txt")
    task2("input.txt")
