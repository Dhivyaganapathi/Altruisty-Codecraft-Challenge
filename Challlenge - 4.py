def find_odd_flavor(N, C):
    # Create a dictionary to count occurrences of each flavor
    flavor_count = {}
    
    # Count the occurrences of each flavor
    for flavor in C:
        if flavor in flavor_count:
            flavor_count[flavor] += 1
        else:
            flavor_count[flavor] = 1
    
    # Loop through the list of flavors in their original order
    for flavor in C:
        if flavor_count[flavor] % 2 != 0:  # If the count is odd
            return flavor  # Return the first flavor with an odd count
    
    return "All are even"  # If no flavor has an odd count

# Input
N = int(input())  # Input the number of flavors
C = [input().strip() for _ in range(N)]  # Input the list of candy flavors

# Output the result
print(find_odd_flavor(N, C))
