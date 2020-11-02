def range_sum(numbers, start, end):
    result = 0
    for number in numbers:
        if start <= number <= end:
            result += number
    return result


input_numbers = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
print(range_sum(input_numbers, a, b))
