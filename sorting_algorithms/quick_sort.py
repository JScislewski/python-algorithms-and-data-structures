# Takes last element as pivot and places it in correct position in sorted array,
# and places all smaller to left of pivot and all greater right of pivot
def partition(arr, left, right):
    i = left - 1
    pivot = arr[right]

    for j in range(left, right):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        partitioning_index = partition(arr, left, right)
        quick_sort(arr, left, partitioning_index - 1)
        quick_sort(arr, partitioning_index + 1, right)


arr = [2, 5, 3, 1, 2, 6, 2, 1, 4, 6, 8, 1, 2, 4, 6, 8, 1, 2, 22, 55, 11, 2, 3, 44]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
