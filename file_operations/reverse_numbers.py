


file_path="C:\\Users\\Luminar\\Desktop\\development_journey_py_dj_oct\\python-works\\file_operations\\numbers.txt"


fr = open(file_path,"r")

result = []

for line in fr:

    line= line.rstrip("\n")

    rev= line[::-1]

    result.append(rev)

print(result)