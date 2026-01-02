

file_path="C:\\Users\\Luminar\\Desktop\\development_journey_py_dj_oct\\python-works\\file_operations\\words.txt"


fr = open(file_path,"r")


pal_words=[]

for line in fr:

    line = line.rstrip("\n")

    word=line.replace(" ","")

    if word==word[::-1]:

        pal_words.append(word)

print(pal_words)

