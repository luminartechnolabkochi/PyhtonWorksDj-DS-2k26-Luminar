

file_path = "file_operations\\wordcount\\story.txt"

fr = open(file_path,"r")

wc={}
for line in fr:

    line = line.rstrip("\n")#line ="Learning new skills opens the door to endless opportunities."

    words = line.split(" ")#["Learning","new","skills"]

    for w in words:

        w=w.rstrip(",")

        w=w.rstrip(".")

        if w in wc:

            wc[w]+=1
        else:
            wc[w]=1

print(wc)


max_value=max(wc.values())


max_word=[k for k,v in wc.items() if v==max_value and k.isalpha()]

print(max_word)