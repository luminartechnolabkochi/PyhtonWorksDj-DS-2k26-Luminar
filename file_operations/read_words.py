

file_path="C:\\Users\\Luminar\\Desktop\\development_journey_py_dj_oct\\python-works\\file_operations\\words.txt"


fr = open(file_path,"r")

result = []

for line in fr:

    line = line.rstrip("\n")

    word= line.replace(" ","")

    result.append(word)
print(result)

