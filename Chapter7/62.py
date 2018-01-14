#62. KVS内の反復処理

import plyvel

artists = plyvel.DB('/tmp/kyoko.ldb', create_if_missing=True)

j = 0
for key, value in artists:
  j += value.decode("utf-8").count("Japan")

print(j)
