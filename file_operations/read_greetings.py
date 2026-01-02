

file_path="C:\\Users\\Luminar\\Desktop\\development_journey_py_dj_oct\\python-works\\file_operations\\greetings.txt"

fr = open(file_path,"r")

st= {line.rstrip("\n") for line in fr }

print(st)