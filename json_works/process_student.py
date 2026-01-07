

from json import load


file_path="json_works\\students.json"

fr = open(file_path,"r",encoding="utf-8")

data = load(fr)#convert json => python native type

for st in data:

    print(st.get("name"),st.get("gender"))




    
