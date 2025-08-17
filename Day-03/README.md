# 📘 Find the Duplicate Number

## 1. Problem Statement
- You are given an array `arr` containing `n+1` integers, where each integer is in the range `[1, n]` inclusive.  
- There is exactly **one duplicate number** in the array, but it may appear more than once.  
- Find the duplicate number **without modifying the array** and using constant extra space.

---

## 2. Constraints
- `1 ≤ n ≤ 10^5`
- There is only **one duplicate number**, but it may appear more than once.
- You must **not modify** the array (`arr`).
- You must use **O(1) extra space**.
- Time complexity must be **O(n)**.

---

## 3. Algorithm Used (Floyd’s Tortoise and Hare Algorithm)

1. **Treat the array like a linked list**  
   - Each index points to the next element (`i → arr[i]`).  
   - Since a duplicate exists, a **cycle** will form.

2. **Phase 1: Detect cycle**  
   - Use two pointers:  
     - `slow` → moves **1 step** (`arr[slow]`)  
     - `fast` → moves **2 steps** (`arr[arr[fast]]`)  
   - Continue until they meet inside the cycle.

3. **Phase 2: Find the entry point**  
   - Reset `slow` to the start (`arr[0]`).  
   - Move both `slow` and `fast` one step at a time.  
   - The position where they meet is the **duplicate number**.
---

## 4. Alternative Approaches

1. **Sorting**  
   - Sort the array and check adjacent elements.  
   - **Time:** O(n log n), **Space:** O(1).  
   - ⚠️ Modifies the array.

2. **HashSet**  
   - Track visited numbers in a set.  
   - **Time:** O(n), **Space:** O(n).  
   - ⚠️ Extra space not allowed.

3. **Binary Search on Value**  
   - Count elements ≤ mid to narrow duplicate range.  
   - **Time:** O(n log n), **Space:** O(1).  
   - Slower but valid.


## 5. Pseudocode

```
function findDuplicate(arr):
    slow = arr[0]
    fast = arr[0]

    # Phase 1: Detect cycle
    repeat:
        slow = arr[slow]
        fast = arr[arr[fast]]
    until slow == fast

    # Phase 2: Find cycle start (duplicate)
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow
```

---

## 6. Edge Cases
1. Smallest possible array: `[1, 1]` → Output: 1  
2. Duplicate appears more than twice → should still detect correctly.  
3. Large array up to `10^5` elements → Algorithm runs efficiently.

---

## 7. Complexity Analysis
- **Time Complexity:** O(n) – Two linear traversals (cycle detection + finding entry).  
- **Space Complexity:** O(1) – Uses only two pointers (`slow`, `fast`).

