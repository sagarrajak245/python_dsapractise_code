def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12

index = binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found")


