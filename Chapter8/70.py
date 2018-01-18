#70. データの入手・整形

assu = ""
with open("rt-polarity.pos", "r+", encoding = "ISO-8859-1") as f:
  for i in f:
    assu += ("+1 " + i)
  f.seek(0)
  try: f.write(assu)
  except IOError:
    pass

assu = ""
with open("rt-polarity.neg", "r+", encoding = "ISO-8859-1") as f:
  for i in f:
    assu += ("-1 " + i)
  f.seek(0)
  try: f.write(assu)
  except IOError:
    pass
