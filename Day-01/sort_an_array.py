from typing import List

def sort_zeros_ones_twos(arr: List[int]) -> List[int]:
    low = 0                 # next position to place a 0
    mid = 0                 # current index to inspect
    high = len(arr) - 1     # next position to place a 2

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# Test Case 1
arr = [0, 1, 2, 1, 0, 2, 1, 0]
print(sort_zeros_ones_twos(arr))  # [0, 0, 0, 1, 1, 1, 2, 2]

# Test Case 2
arr =  [2, 2, 2, 2]
print(sort_zeros_ones_twos(arr))  #  [2, 2, 2, 2]

# Test Case 3
arr = [0, 0, 0, 0]
print(sort_zeros_ones_twos(arr))  # [0, 0, 0, 0]

# Test Case 4
arr = [1, 1, 1, 1]
print(sort_zeros_ones_twos(arr))  #[1, 1, 1, 1]

# Test Case 5
arr =  [2, 0, 1]
print(sort_zeros_ones_twos(arr))  # [0,1,2]

# Test Case 6
arr = []
print(sort_zeros_ones_twos(arr))  # []