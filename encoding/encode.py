def encode(input):
    counter = 1
    result = ""
    for i in range(0, len(input)):
        if i == len(input) - 1 or input[i] != input[i + 1]:
            result += str(counter) + str(input[i])
            counter = 1
        else:
            counter += 1
    return result


text = "ssssssttssrrrqqqwwwiiinnss"
print(encode(text))
