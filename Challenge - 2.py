def bees_between_flowers(s, startIndex, endIndex):
    n = len(s)
    bee_count_prefix = [0] * (n + 1)
    
    left_flower = [-1] * n
    right_flower = [-1] * n
    
    for i in range(n):
        bee_count_prefix[i + 1] = bee_count_prefix[i] + (1 if s[i] == '*' else 0)
    
    last_flower = -1
    for i in range(n):
        if s[i] == '|':
            last_flower = i
        left_flower[i] = last_flower
    last_flower = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last_flower = i
        right_flower[i] = last_flower

    results = []
    for i in range(len(startIndex)):
        start = startIndex[i] - 1
        end = endIndex[i] - 1

        left_bound = right_flower[start]  
        right_bound = left_flower[end]    
        if left_bound != -1 and right_bound != -1 and left_bound < right_bound:
            bees_count = bee_count_prefix[right_bound + 1] - bee_count_prefix[left_bound + 1]
            results.append(bees_count)
        else:
            results.append(0)

    return results

# Input and output handling for custom testing
s = input().strip()
n = int(input().strip())
startIndex = [int(input().strip()) for _ in range(n)]
m = int(input().strip())
endIndex = [int(input().strip()) for _ in range(m)]

# Calculating results
output = bees_between_flowers(s, startIndex, endIndex)
for result in output:
    print(result)
