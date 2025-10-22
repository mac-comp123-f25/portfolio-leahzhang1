def string_of_nums(n):
    acc = ""
    for i in range(1, n + 1):
        acc = acc + str(i) + ""
    return acc

print(string_of_nums(10))
