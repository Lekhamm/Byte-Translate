def max_game_seconds(s):
    occupied_cells = [i for i, c in enumerate(s) if c == 'T']
    max_seconds = 0

    for i in range(len(occupied_cells)):
        seconds = occupied_cells[i] - i
        max_seconds = max(max_seconds, seconds)

    return max_seconds

# Sample input
s = input().strip()

# Output
result = max_game_seconds(s)
print(result)