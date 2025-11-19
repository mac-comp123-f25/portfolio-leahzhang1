def print_abbrev(filename):
    file = open(filename, 'r')
    for line in file:
        short_line = line[:20]
        print(short_line.rstrip())
    file.close()

print_abbrev("../TextFiles/alice.txt")