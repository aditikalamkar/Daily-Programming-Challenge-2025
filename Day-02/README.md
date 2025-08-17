
# 📘Find the Missing Number  (Sum Formula Approach)

## 1. Problem Statement
- You are given an array arr containing n-1 distinct integers.
- The integers are taken from the range 1 to n, meaning exactly one integer is missing.

  

---

## 2. Constraints
- The array contains exactly `n-1` distinct integers.  
- All integers are in the range `[1, n]`.  
- Time complexity must be `O(n)`.  
- Space complexity must be `O(1)`.  
- `1 ≤ n ≤ 10^6`  

---

## 3. Approach (Sum Formula Method)

1. The sum of first `n` natural numbers is given by the formula:

   
   total\_sum = n * (n+1) / 2 
   

2. Compute the **actual sum** of all elements in the array.

3. The **missing number** is:

   \[
   missing = total\_sum - actual\_sum
   \]

---

## 4. Pseudocode (Sum Formula)
```python

def find_missing_sum(arr):
    # Step 1: Calculate expected number count (n)
    n = len(arr) + 1   # because one number is missing

    # Step 2: Calculate expected sum of numbers from 1 to n
    total_sum = n * (n + 1) // 2

    # Step 3: Calculate actual sum of given array
    actual_sum = sum(arr)

    # Step 4: Missing number is the difference
    missing_number = total_sum - actual_sum

    # Step 5: Return result
    return missing_number

```

---


## 5. Edge Cases
- **Empty smallest array case (n=2):** Only 1 element given, missing can be 1 or 2.  
- **Largest case (n=10^6):** Still efficient due to O(n) time and O(1) space.  

---

## 6. Complexity Analysis
- **Time Complexity:** `O(n)` (we compute the sum once).  
- **Space Complexity:** `O(1)` (only a few variables).  



