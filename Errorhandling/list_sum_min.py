

# ZeroDivisionError
# FileNotFound
# KeyError
# ValueError
# IndexError
# raise InvalidAge
lst=["10","20","hello","300","hai","4 00"]

print(lst[10])
# error handling

# sum, min,max,sort


numbers = []

for el in lst:

   try:
       num = int(el)

       numbers.append(num)
   except Exception as e:
       
       continue

print(numbers)

max_element = max(numbers)

min_element = min(numbers)

srt_numbers=sorted(numbers)

total = sum(numbers)
print(max_element)
print(min_element)
print(srt_numbers)
