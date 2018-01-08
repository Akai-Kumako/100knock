#13.col1.txtとcol2.txtをマージ
# paste col1.txt col2.txt

a = open("col1.txt", "r")
b = open("col2.txt", "r")
f = open("col.txt", "w")

text = "\t".join([a.read(), b.read()])
text = text.replace("\n", "")
f.write(text)

a.close()
b.close()
f.close()
