

arr=[12,22,23,34]
#     1  2  3  4

# {12:12**1,22:22**2,23:23**3,34:34**4}

result ={num:num**index for index,num in enumerate(arr,1)}

print(result)


