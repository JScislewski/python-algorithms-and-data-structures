def count(numbers, target):
    occurences = 0
    for number in numbers:
        if number == target:
            occurences += 1
    return occurences


numbers = [int(x) for x in input().split()]
target = int(input())
print(count(numbers, target))
