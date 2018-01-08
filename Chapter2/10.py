#10.行数のカウント
# wc -l hightemp.txt

f = open("hightemp.txt", "r")

print(len(f.readlines()))

f.close()
