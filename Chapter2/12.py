#12.1列目をcol1.txtに,2列目をcol2.txtに保存
# cut col1.txt / cut col2.txt

f = open("hightemp.txt", "r")
a = open("col1.txt", "w")
b = open("col2.txt", "w")

lines = f.readlines()

for i in lines:

f.close()
a.close()
b.close()
