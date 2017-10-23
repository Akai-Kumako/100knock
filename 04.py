#04.元素記号

import re

a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

pull = [1, 5, 6, 7, 8, 9, 15, 16, 19]

a = re.sub(r'[\.,]+', "", a)
a = a.split(" ")
result = {}

for i in range(len(a)):
  if i + 1 in pull:
    result[i + 1] = a[i][0:1]
  else:
    result[i + 1] = a[i][0:2]

print(result)
