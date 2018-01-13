#61. KVSの検索

import plyvel

artists = plyvel.DB('/tmp/artist.ldb', create_if_missing=True)
print(artists.get("Oasis".encode("utf-8")).decode("utf-8"))
