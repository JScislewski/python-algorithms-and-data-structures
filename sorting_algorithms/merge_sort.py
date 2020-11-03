def merge_sort(arr):
    if len(arr) > 1:
        middle_element = len(arr) // 2
        left_side = arr[:middle_element]
        right_side = arr[middle_element:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = j = k = 0

        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1

        # check if something left
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1

arr = [2, 5, 3, 1, 2, 6,2,1,4,6,8,1,2,4,6,8,1,2,22,55,11,2,3,44]
merge_sort(arr)
print(arr)