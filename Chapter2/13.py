#13.col1.txtとcol2.txtをマージ
# paste col1.txt col2.txt

a = open("col1.txt", "r")
b = open("col2.txt", "r")
f = open("col.txt", "w")

col1 = a.readlines()
col2 = b.readlines()

for data1, data2 in zip(col1, col2):
  f.writelines(data1.replace("\n", "") + "\t" + data2);

a.close()
b.close()
f.close()
