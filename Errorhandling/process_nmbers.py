
# input => numbers.txt
# lst =
# max
# min
# sum
# most frequent number

file_path = "Errorhandling\\numbers.txt"


fr = open(file_path,"r")

lst = []


for line in fr:

    line = line.rstrip("\n")

    try:

        num = int(line)

        lst.append(num)

    except Exception as e:

        continue

print(max(lst))

print(min(lst))

print(min(lst))

number_count = {num:lst.count(num) for num in lst}

max_value=max(number_count.values())

freq=[k for k,v in number_count.items() if v==max_value]

print(freq)


