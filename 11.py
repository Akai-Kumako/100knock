#11.タブをスペースに置換
# expand -t 1 hightemp.txt

f = open("hightemp.txt", "r")

print(f.read().replace("\t", " "))

f.close()
