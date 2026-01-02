

# product={"code":123,"brand":"lp","price":1200}

# # chk offer is exist if not exist add offer as 100 else update offer as current offer+75

# if "offer" in product:

#     product["offer"]+=75

# else:

#     product["offer"]=100



words=["hai","hello","hai","hello","python"]


wc={}

for w in words:

    if w in wc:

        wc[w]+=1

    else:

        wc[w]=1

print(wc)

