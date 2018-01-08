#07.テンプレートによる文字生成

def template(time, factor, value):
  print("{0}時の{1}は{2}".format(time, factor, value))
  

template(12, "気温", 22.4)
