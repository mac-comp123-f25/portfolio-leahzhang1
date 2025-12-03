def every_other (items):
    return items[::2]
print(every_other([1, 2, 3, 4, 5, 6]))

def sum_positive (pos):
    return sum([x for x in pos if x>0])
print(sum_positive([-1, 2, 3, 4, 5, 6]))