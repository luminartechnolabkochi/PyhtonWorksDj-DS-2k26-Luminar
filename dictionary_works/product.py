

product={"code":345,"title":"pe shirt","color":"blue","size":"m","price":1500,"offer":200}

print(product["price"])

# add offer of 100 rs if offer not exist else update offer as current offer +50

if "offer" in product:

    product["offer"]+=50  #update

else:

    product["offer"]=100 #add


print(product)


# set

