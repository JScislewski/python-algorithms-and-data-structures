def range_sum(numbers, start, end):
    sum = 0
    for i in range(0, len(numbers)):
        if start <= numbers[i] <= end:
            sum += numbers[i]
    return sum


input_numbers = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
print(range_sum(input_numbers, a, b))
