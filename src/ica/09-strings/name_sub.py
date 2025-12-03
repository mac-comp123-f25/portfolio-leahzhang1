def count_words(word,text):
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count +=1
    return count

print(count_words("ban","ban is banana"))