def find_lunch_mate(input):
    lines = input.strip().splitlines()

    nikki = lines[0].strip().split()
    nikki_start, nikki_end = int(nikki[1]), int(nikki[2])

    matches = []

    for line in lines[1:]:
        parts = line.strip().split()
        name, start, end = parts[0], int(parts[1]), int(parts[2])

        # Step 1: Check if start time is within Nikki's window
        if nikki_start <= start <= nikki_end:
            # Step 2: Check actual overlap
            overlap = min(nikki_end, end) - start
            if overlap >= 30:
                matches.append((overlap, start, name))

    if not matches:
        return "NO MATCH"

    # Sort by overlap time (desc), then by earliest start time
    matches.sort(key=lambda x: (-x[0], x[1]))
    return matches[0][2]


def best_split_point(arr):
    min_diff = float('inf')
    best_index = -1

    for i in range(1, len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i:])
        diff = abs(left - right)

        if diff < min_diff:
            min_diff = diff
            best_index = i

    return best_index