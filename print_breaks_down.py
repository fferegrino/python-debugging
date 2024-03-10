def binary_search(arr, low, high, x):
    print(f"low: {low}, high: {high}")
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, it's in the left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element is in the right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1

# Test array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26,
    27, 28, 29, 30, 31, 32, 33, 34,
    35, 36, 37, 38, 39, 40, 41, 42,
    43, 44, 45, 46, 47, 48, 49, 50]
x = 43

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

print(f"Element is present at index {result}")
