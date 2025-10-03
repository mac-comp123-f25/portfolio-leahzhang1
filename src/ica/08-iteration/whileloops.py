def print_every_fifth(x):
  while x >= 0:  # x is the loop variable
    print(x)
    x = x - 5
  # when indentation stops, while loop is over
  print("Done!")

print_every_fifth(20)
print_every_fifth(11)


def square_user_nums():
  # Initialize loop variable
  user_inp = input("Enter the next number (negative to quit): ")
  user_num = int(user_inp)
  while user_num >= 0:
    print(user_num, "squared is", user_num ** 2)
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp)


def sum_to_n(topNum):
    """
    Takes in a number and computes and returns the sum of the numbers
    from zero to the input number.
    """
    curr_val = 0  # the loop variable
    total = 0  # the accumulator variable
    while curr_val < topNum:
        total = total + curr_val  # add next value to accumulator
        curr_val = curr_val + 1  # update the loop variable

    return total
 

def nextWord(text):
    """
    Takes in a string of text and builds and returns a new string
    that is the next "word" in the text. In other words, the next
    sequence of characters up to a space, tab, or newline.
    """
    wordStr = ""
    i = 0
    for ch in text:
        if ch in " \t\n":  # if character is space, tab (\t), or newline (\n)
            break
        else:
            wordStr = wordStr + ch

    return wordStr
