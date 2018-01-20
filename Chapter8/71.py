#71. ストップワード

from stop_words import get_stop_words

def check(word):
  if word in get_stop_words("english"):
    return True
  else:
    return False

print(check("the"))
print(check("panda"))
print(check("an"))
