def find_duplicate(arr):

    # Phase 1: Detect cycle
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]           # move 1 step
        fast = arr[arr[fast]]      # move 2 steps
        if slow == fast:
            break

    # Phase 2: Find cycle entry (the duplicate value)
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


print(find_duplicate([1, 3, 4, 2, 2]))   # 2
print(find_duplicate([3, 1, 3, 4, 2]))   # 3
print(find_duplicate([1, 1]))            # 1
print(find_duplicate([1, 4, 4, 2, 3]))   # 4

# Test Case 5: [1, 2, 3, ..., 99999, 50000] -> duplicate is 50000
n = 99999
big_arr = list(range(1, n + 1))  # 1..99999
big_arr.append(50000)            # add duplicate
print(find_duplicate(big_arr))   # 50000
