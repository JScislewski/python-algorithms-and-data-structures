def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break


first_array = [
    2,
    5,
    3,
    1,
    2,
    6,
    2,
    1,
    4,
    6,
    8,
    1,
    2,
    4,
    6,
    8,
    1,
    2,
    22,
    55,
    11,
    2,
    3,
    44,
]
second_array = [
    2,
    5,
    3,
    1,
    2,
    6,
    2,
    1,
    4,
    6,
    8,
    1,
    2,
    4,
    6,
    8,
    1,
    2,
    22,
    55,
    11,
    2,
    3,
    44,
]
bubble_sort(first_array)
optimized_bubble_sort(second_array)
print(first_array)
print(second_array)
