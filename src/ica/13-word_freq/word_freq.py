def compute_frequencies()
    text = 'one fish, two fish, red fish, blue fish'
    words = text.split()
    for word in words:
        print(word)

import string
text = 'one fish, two fish, red fish, blue fish'
words = text.split()
for word in words:
    newWord = word.strip(string.punctuation)
    print(word, newWord)
