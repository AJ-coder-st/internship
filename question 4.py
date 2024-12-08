def find_first_odd_flavor(N, C):
    # Dictionary to count occurrences
    flavor_count = {}
    
    # Count the frequency of each flavor
    for flavor in C:
        if flavor in flavor_count:
            flavor_count[flavor] += 1
        else:
            flavor_count[flavor] = 1
    
    # Find the first flavor with an odd count
    for flavor in C:
        if flavor_count[flavor] % 2 != 0:
            return flavor
    
    # If no odd count found, return "All are even"
    return "All are even"

# Input processing
N = int(input())  # Number of flavors
C = [input().strip() for _ in range(N)]  # List of flavors

# Output the result
print(find_first_odd_flavor(N, C))
