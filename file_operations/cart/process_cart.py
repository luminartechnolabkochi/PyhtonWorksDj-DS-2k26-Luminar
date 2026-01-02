

file_path="file_operations\\cart\\cart_items_100.csv"


fr = open(file_path,"r",encoding="utf-8")

import csv

reader=csv.DictReader(fr)

data = [row for row in reader] #[{"id":,"title":"","quantity":"","user"},{},{}]


order_summary={}

for o in data:

    title =  o.get("title")

    qty = int(o.get("quantity",0))

    if title in order_summary:


        order_summary[title]+=qty

    else:

        order_summary[title] = qty


"""
order_summary={
'Camera': 32, 'Keyboard': 29, 
'Charger': 38, 'Tablet': 31, 
'Phone': 26, 'Headphones': 29, 
'Mouse': 17, 'Monitor': 50, 'Speaker': 18, 'Laptop': 24
}

"""
max_order=max(order_summary.values())#50

popular_item=[k for k,v in order_summary.items() if v==max_order]

print(popular_item)


low_order = min(order_summary.values())

cheapest_item=[k for k,v in order_summary.items() if v == low_order]

print(cheapest_item)


