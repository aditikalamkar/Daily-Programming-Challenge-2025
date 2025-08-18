def merge(arr1, arr2):
    m, n = len(arr1), len(arr2)

    # Function to calculate next gap
    def nextGap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    # Start with initial gap
    gap = nextGap(m + n)

    while gap > 0:
        i = 0
        j = gap

        while j < (m + n):
            # Compare elements in arr1
            if j < m and arr1[i] > arr1[j]:
                arr1[i], arr1[j] = arr1[j], arr1[i]

            # Compare elements across arr1 and arr2
            elif i < m and j >= m and arr1[i] > arr2[j - m]:
                arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

            # Compare elements in arr2
            elif i >= m and j >= m and arr2[i - m] > arr2[j - m]:
                arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        gap = nextGap(gap)


#Test Case 1
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merge(arr1, arr2)
print("arr1:", arr1, "arr2:", arr2)   

#Test Case 2
arr1 = [10, 12, 14]
arr2 = [1, 3, 5] 
merge(arr1, arr2)
print("arr1:", arr1, "arr2:", arr2)   

#Test Case 3
arr1 = [2, 3, 8]
arr2 = [4, 6, 10]
merge(arr1, arr2)
print("arr1:", arr1, "arr2:", arr2)   

#Test Case 4
arr1 = [1]
arr2 = [2]
merge(arr1, arr2)
print("arr1:", arr1, "arr2:", arr2)   


#Test Case 5
arr1 = list(range(1, 100001))
arr2 = list(range(50001, 100001))

merge(arr1, arr2)
print("arr1:", arr1, "arr2:", arr2)