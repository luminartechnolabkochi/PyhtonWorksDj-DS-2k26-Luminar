vehicles = [
    {"name": "Swift", "brand": "Maruti Suzuki", "price": 650000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Baleno", "brand": "Maruti Suzuki", "price": 820000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Creta", "brand": "Hyundai", "price": 1500000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "i20", "brand": "Hyundai", "price": 950000, "model": 2021, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Seltos", "brand": "Kia", "price": 1600000, "model": 2023, "color": "Silver", "fuel_type": "Diesel"},
    {"name": "Sonet", "brand": "Kia", "price": 1200000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Harrier", "brand": "Tata", "price": 1900000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "Nexon", "brand": "Tata", "price": 1200000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Punch", "brand": "Tata", "price": 800000, "model": 2023, "color": "Green", "fuel_type": "Petrol"},
    {"name": "XUV700", "brand": "Mahindra", "price": 2200000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Thar", "brand": "Mahindra", "price": 1700000, "model": 2022, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Scorpio N", "brand": "Mahindra", "price": 2000000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "City", "brand": "Honda", "price": 1500000, "model": 2021, "color": "Silver", "fuel_type": "Petrol"},
    {"name": "Amaze", "brand": "Honda", "price": 900000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Kiger", "brand": "Renault", "price": 800000, "model": 2021, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Duster", "brand": "Renault", "price": 1300000, "model": 2020, "color": "Brown", "fuel_type": "Diesel"},
    {"name": "EcoSport", "brand": "Ford", "price": 1100000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Endeavour", "brand": "Ford", "price": 3600000, "model": 2020, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Altroz", "brand": "Tata", "price": 950000, "model": 2022, "color": "Golden", "fuel_type": "Petrol"},
    {"name": "Venue", "brand": "Hyundai", "price": 1300000, "model": 2023, "color": "Red", "fuel_type": "Petrol"}
]



# all_barnds

all_brands={v.get("brand") for v in vehicles }

# print(all_brands)

# display vehcle names whose color = red
# display vehicles names  whose model 2022
# display diesel vehile names
# display all vehicle price
# display vehicle names whose price > 10lac
# display tata vehicle names
# display tata vecle whose model 2022
# display vehcle availabe at lowest price
# dsipaly prices of maruthi suzuki vehicles
# display hundayi vehicle names avaiale at > 5lac
# display vehicle names whose model in range of 2022 - 2024
# which brand have most number of vehicle
# costly vehicle availabe in mahindra and tata
# which model has most number of vehicles

# prce_list=[v.get("price") for v in vehicles]

# min_price=min(prce_list)

# for v in vehicles:

#     if v.get("price")==min_price:

#         print(v)


# model_list=[v.get("model") for v in vehicles]

# model_count={m:model_list.count(m) for m in model_list}

# model_count_list=model_count.values()

# min_model = min(model_count_list)


# for k,v in model_count.items():

#     if v == min_model:

#         print(k,v)

mahindra_vehicles = [v for v in vehicles if v.get("brand")=="Mahindra"]

m_v_p_l= [v.get("price") for v in mahindra_vehicles]

mahindra_max_price = max(m_v_p_l)
for v in mahindra_vehicles:

    if v.get("pricie")==mahindra_max_price:

        print(v)