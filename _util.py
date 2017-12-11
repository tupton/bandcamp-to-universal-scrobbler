def time_to_seconds(t):
    if not t:
        return 0
    convert = [3600, 60, 1]
    split = t.split(":")
    return sum(c * t for c, t in zip(convert[-1 * len(split):], map(int, split)))

