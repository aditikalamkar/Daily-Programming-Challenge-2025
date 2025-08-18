# 📘 Merge Two Sorted Arrays (In-Place)

## 1. Problem Statement
- You are given two **sorted arrays** `arr1` (size `m`) and `arr2` (size `n`).  
- Merge them so that both arrays remain sorted **without using extra space**.  
- After merging:  
  - `arr1` should contain the smallest `m` elements.  
  - `arr2` should contain the largest `n` elements.  

---

## 2. Constraints
- `1 ≤ m, n ≤ 10^5`
- Both arrays are initially **sorted in non-decreasing order**.
- Must use **O(1) extra space**.
- Time complexity target: **O((m+n) log(m+n))** or better.

---

## 3. Algorithm Used (Gap Method – Shell Sort)

1. **Initialize gap** = `ceil((m + n) / 2)`.  
2. Compare elements `i` and `j` that are `gap` apart:  
   - If `i` in `arr1` and `j` in `arr1` → swap if out of order.  
   - If `i` in `arr1` and `j` in `arr2` → swap if out of order.  
   - If `i` in `arr2` and `j` in `arr2` → swap if out of order.  
3. Reduce gap → `ceil(gap / 2)` until gap = 0.  
4. Arrays are sorted and merged **in-place**.

---

## 4. Alternative Approaches

1. **Naive Swap + Sort**  
   - Swap larger elements from `arr1` with smaller ones in `arr2`, then sort both.  
   - **Time:** O((m+n) log(m+n)), **Space:** O(1).  

2. **Insertion Method**  
   - For each element in `arr1`, place it in correct position in `arr2`.  
   - **Time:** O(m × n), **Space:** O(1).  
   - ⚠️ Very slow for large inputs.

3. **Gap Method (Best Practice)** ✅  
   - **Time:** O((m+n) log(m+n))  
   - **Space:** O(1)  

---

## 5. Pseudocode

```
function merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    gap = ceil((m + n) / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < (m + n):
            # Case 1: Both in arr1
            if j < m and arr1[i] > arr1[j]:
                swap(arr1[i], arr1[j])

            # Case 2: i in arr1, j in arr2
            elif i < m and j >= m and arr1[i] > arr2[j - m]:
                swap(arr1[i], arr2[j - m])

            # Case 3: Both in arr2
            elif i >= m and j >= m and arr2[i - m] > arr2[j - m]:
                swap(arr2[i - m], arr2[j - m])

            i += 1
            j += 1

        if gap == 1:
            gap = 0
        else:
            gap = ceil(gap / 2)
```

---

## 6. Edge Cases
1. `arr1 = [1, 3, 5], arr2 = [2, 4, 6]` → Output: arr1 = `[1, 2, 3]`, arr2 = `[4, 5, 6]`  
2. All elements of `arr1` smaller than `arr2` → Arrays remain unchanged.  
3. All elements of `arr1` larger than `arr2` → Complete swap needed.  
4. Large arrays (`10^5` elements) → Efficient in O((m+n) log(m+n)).  

---

## 7. Complexity Analysis
- **Time Complexity:** O((m+n) log(m+n)) – gap reduces like Shell Sort.  
- **Space Complexity:** O(1) – In-place merge, no extra storage used.  
