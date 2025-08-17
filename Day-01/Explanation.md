# Sorting an Array of 0s, 1s, and 2s (Dutch National Flag Algorithm)



1\. Problem Statement



* You are given an array containing only 0, 1, and 2.



* Task: Sort the array in increasing order.



* Constraints:



Must run in O(n) time.



Must use O(1) extra space (in-place sorting).





















* We maintain three regions using pointers low, mid, and high.



* When we see a 0 at mid, we swap it left (to low), because all 0s must be at the beginning.



* When we see a 1, it’s already in the correct middle region, so just move mid.



* When we see a 2, we swap it right (to high), because all 2s must be at the end. We don’t advance mid after this swap because the element we just swapped in hasn’t been inspected yet.

#### 

#### Edge cases covered



* Empty array: high = -1, loop doesn’t run; returns \[].



* All equal elements: Logic still holds (only one branch runs).



* Already sorted: Minimal swaps; still linear.



* Mixed order: Correctly partitions and sorts.





#### Complexity



* Time: O(n) — each element is examined at most once.



* Space: O(1) — only the three pointers are used (in-place).





