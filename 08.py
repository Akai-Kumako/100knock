#08.暗号文

a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

def cipher(text):
  encr = ""
  for char in text:
    if char.islower():
      encr = "".join([encr, chr(219 - ord(char))])
    else:
      encr = "".join([encr, char])
  return encr

print(cipher(a))
print(cipher(cipher(a)))
