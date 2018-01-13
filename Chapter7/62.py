#62. KVS内の反復処理

import plyvel

artists = plyvel.DB('/tmp/artist.ldb', create_if_missing=True)

j = 0
for key, value in artists:
  if value == "Japan".encode("utf-8"):
    j += 1

print(j)
