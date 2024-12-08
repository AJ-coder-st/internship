def count_bees(s, startIndex, endIndex):
    n = len(s)
    
    # Prefix sum for bees
    prefix_bees = [0] * (n + 1)
    for i in range(n):
        prefix_bees[i + 1] = prefix_bees[i] + (1 if s[i] == '*' else 0)
    
    # Nearest left and right flowers
    nearest_left_flower = [-1] * n
    nearest_right_flower = [-1] * n

    # Fill nearest_left_flower
    last_flower = -1
    for i in range(n):
        if s[i] == '|':
            last_flower = i
        nearest_left_flower[i] = last_flower

    # Fill nearest_right_flower
    last_flower = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last_flower = i
        nearest_right_flower[i] = last_flower

    # Answer each query
    results = []
    for start, end in zip(startIndex, endIndex):
        # Convert to 0-indexed
        start -= 1
        end -= 1

        # Find the valid range between nearest flowers
        right_flower = nearest_right_flower[start]
        left_flower = nearest_left_flower[end]

        if right_flower != -1 and left_flower != -1 and right_flower <= left_flower:
            # Bees count between flowers
            results.append(prefix_bees[left_flower + 1] - prefix_bees[right_flower])
        else:
            results.append(0)
    
    return results

# Input
s = input().strip()
n = int(input())
startIndex = [int(input()) for _ in range(n)]
endIndex = [int(input()) for _ in range(n)]

# Output
results = count_bees(s, startIndex, endIndex)
for res in results:
    print(res)
