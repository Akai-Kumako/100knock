#71. ストップワード

stop = ["the", "a", "an"]

def check(word):
  if word in stop:
    return True
  else:
    return False

print(check("the"))
print(check("panda"))
print(check("an"))
