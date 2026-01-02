

# vehicles = name,brand,price,model,color,fuel_type 




products=[

    {"code":"sku123","name":"redminote14","brand":"redmi","price":22000,"display":"led"},
    {"code":"sku124","name":"redminote14pro","brand":"redmi","price":25000,"display":"led"},
    {"code":"sku125","name":"motoe55","brand":"motorola","price":22000,"display":"amoled"},
    {"code":"sku126","name":"oneplusnord9t","brand":"oneplus","price":32000,"display":"amoled"},
    {"code":"sku125","name":"iphone16","brand":"apple","price":72000,"display":"amoled"},
    {"code":"sku125","name":"iphone16pro","brand":"apple","price":82000,"display":"amoled"},

]
all_product_name = [p.get("name") for p in products]

# print(all_product_name)

all_brands={p.get("brand") for p in products}

print(all_brands)

all_display_types={p.get("display") for p in products}

print(all_display_types)

# display apple product name

apple_products=[p.get("name") for p in products if p.get("brand")=="apple" ]

print(apple_products)
