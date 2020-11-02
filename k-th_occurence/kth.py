def kth(numbers, target, k):
    occurence_count = 0
    for i, number in enumerate(numbers):
        if number == target:
            occurence_count += 1
            if occurence_count == k:
                return i
    return -1


numbers = [int(x) for x in input().split()]
target = int(input())
k = int(input())
print(kth(numbers, target, k))
