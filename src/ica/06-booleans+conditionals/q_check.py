def has_q(word):
    return 'q' in word.lower()

if __name__ == "__main__":
  assert has_q("quick") == True
  assert has_q("math") == False
  print("All tests passed!")
