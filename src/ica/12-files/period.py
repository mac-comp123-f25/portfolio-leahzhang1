def up_to_period(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    result = ""
    for ch in text:
        result += ch
        if ch == '.':
            break
    return result

up_to_period('../TextFiles/mockingbird.txt')