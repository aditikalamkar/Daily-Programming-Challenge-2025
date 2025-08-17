# 📘 Explanation: Sorting an Array of 0s, 1s, and 2s (Dutch National Flag Algorithm)

## 1. Problem Statement
- You are given an array containing only `0`, `1`, and `2`.
- Task: Sort the array in **increasing order**.
- Constraints:
  - Must run in **O(n)** time.
  - Must use **O(1)** extra space (in-place sorting).

---

## 2. Why Not Use Normal Sorting?
- Python’s `sorted()` is **O(n log n)** and uses extra memory.  
- Here we need **linear time** (`O(n)`) and **no extra space** (`O(1)`).

---

## 3. Algorithm Used — Dutch National Flag (DNF)
- Developed by **Edsger Dijkstra**.
- Idea: Partition the array into 3 regions using **3 pointers**:
  - `low` → boundary for `0`s
  - `mid` → current element to check
  - `high` → boundary for `2`s

At any point:
- `[0 .. low-1]` → all `0`s  
- `[low .. mid-1]` → all `1`s  
- `[mid .. high]` → unknown (to be processed)  
- `[high+1 .. end]` → all `2`s  

---


## 4. Pseudocode
```
low = 0, mid = 0, high = n-1
while mid <= high:
    if arr[mid] == 0:
        swap(arr[low], arr[mid])
        low++, mid++
    else if arr[mid] == 1:
        mid++
    else:
        swap(arr[mid], arr[high])
        high--
```

---


## 5. Edge Cases
- Empty array: high = -1, loop doesn’t run; returns [].

- All equal elements: Logic still holds (only one branch runs).

- Already sorted: Minimal swaps; still linear.
- Mixed order: Correctly partitions and sorts.


## 6. Complexity Analysis
- **Time Complexity:** `O(n)` (each element is inspected at most once).  
- **Space Complexity:** `O(1)` (only uses three pointers).  







