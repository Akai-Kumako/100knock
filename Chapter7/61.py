#61. KVSの検索

import plyvel

artists = plyvel.DB('/tmp/kyoko.ldb', create_if_missing=True)
print(artists.get("エレファントカシマシ".encode("utf-8")).decode("utf-8"))
