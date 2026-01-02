"""

comprehension

easy way for creating list,tuple,set,dict from a sequence


syntax:

result=[return iteration condition] => list comprehension

result = {return iteration condition} => set comprehension

result= {k:v iterarton condition} => dictionary comprehension
"""

arr=[3,4,5,6,7,8]

cubes=[num**3 for num in arr]

print(cubes)


evens=[num for num in arr if num%2==0]

print(evens)

odds=[num for num in arr if num%2!=0]

print(odds)

num_gt_five=[num for num in arr if num>5]

print(num_gt_five)