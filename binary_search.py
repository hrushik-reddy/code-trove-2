def binary_search(arr, target):
    left = 0
    right = len(arr)  

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid 
        else:
            right = mid 
    return -1


# Test
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
