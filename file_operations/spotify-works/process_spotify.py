
file_path="file_operations\\spotify-works\\spotify_data clean.csv"


fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [row for row in reader]

print(len(data))


artist_followers={s.get("artist_name") : int(s.get("artist_followers",0)) for s in data }

print(artist_followers)

sorted_records=sorted(artist_followers,key=artist_followers.get,reverse=True)[:5]

print(sorted_records)

