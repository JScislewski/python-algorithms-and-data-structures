def linear_search(elements, target):
    index = -1

    for i, elem in enumerate(elements):
        if elem == target:
            index = i
            return index
    return index


elements = [int(x) for x in input().split()]
target = int(input())
print(linear_search(elements, target))
