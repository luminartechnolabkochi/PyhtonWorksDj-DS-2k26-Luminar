# create a dictionary menu_items with key as name of item and value as price


veigitables={
    "onion":35,"potatto":45,
    "brinjal":50,"drumstick":120,
    "chilly":100,"ginger":250,
    "carrot":75,"beetroot":50
}


# display all keys
for k in veigitables.keys():

    print(k)

# display all key values

for k,v in veigitables.items():

    print(k,v)

# display all vegitable names available under rs 50

for k,v in veigitables.items():

    if v<50:

        print(k,v)

# fetch price of elephant_foot_yam

ite_price=veigitables.get("onion",0)

print(ite_price)

# chk item potatto is exist if exist update potattos price as current price + 15

if "potatto" in veigitables:

    veigitables["potatto"]+=15

print(veigitables)
