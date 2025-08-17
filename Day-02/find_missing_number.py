from typing import List

def find_missing_number(arr: List[int]) -> int:
 
    n = len(arr) + 1   # since one number is missing
    total_sum = n * (n + 1) // 2   # expected sum of 1..n
    actual_sum = sum(arr)          # sum of given array
    return total_sum - actual_sum


print(find_missing_number([1, 2, 4, 5]))      # 3
print(find_missing_number([2, 3, 4, 5]))      # 1
print(find_missing_number([1, 2, 3, 4]))      # 5
print(find_missing_number([1]))               # 2
print(find_missing_number(list(range(1, 1000000))))  # 1000000
