


file_path="C:\\Users\\Luminar\\Desktop\\development_journey_py_dj_oct\\python-works\\file_operations\\numbers.txt"


fr = open(file_path,"r")

even=[]

odd=[]

for line in fr:

    number = int(line.rstrip("\n"))

    if number%2==0:

        even.append(number)
    else:
        odd.append(number)

print(odd)

print(even)
    

# create a file procees_numbers.py
# create a new list that contain reverse of each number