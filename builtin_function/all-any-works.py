


lst=["housefull","beautiful","peaceful","harmful","thinkful","powerful"]

bool_list=[w.endswith("ful") for w in lst]

print(all(bool_list))

words=["program","problem","perfect","apple"]

# is there any word staring with pro in words

b_l=[w.startswith("pro") for w in words]

print(any(b_l))



number=15

print(not any([number%i==0 for i in range(2,number)]))


# map(func,iterable)
# filter(fuc,iterable)
#functools> reduce(func,iterable)
# all()
# any()




