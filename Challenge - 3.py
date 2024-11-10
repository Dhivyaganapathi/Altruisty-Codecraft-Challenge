def min_of_maximums(k, arr):
    n = len(arr)
    min_of_max = float('inf')

    # Iterate through each possible subarray of size 'k'
    for i in range(n - k + 1):
        # Find the maximum in the current subarray of size 'k'
        max_in_window = max(arr[i:i+k])
        # Update the minimum of the maximums
        min_of_max = min(min_of_max, max_in_window)

    return min_of_max

# User Input
k = int(input("Enter the length of the subarray (k): "))
n = int(input("Enter the size of the array (n): "))
arr = list(map(int, input("Enter the elements of the array: ").split()))

# Get result
result = min_of_maximums(k, arr)
print("The minimum of the maximums is:", result)
