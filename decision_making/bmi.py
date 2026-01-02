# read height and weight
# calculate bmi

# <20  "underweight"

# 20-25 "normal weight"

# 25-30 "overweight"

# >30 "obese"



weight_in_kg = int(input("enter weight in kg "))

height_in_cm = int(input("enter height in cm "))


height_in_meter = height_in_cm / 100

bmi = weight_in_kg/(height_in_meter**2)#23.78908765434567

bmi = round(bmi,0)#28

if bmi < 20:#28<20

    print("underweight")

elif bmi<25:#28>=20 and 28<25

    print("normal weight")

elif bmi<30:

    print("overweight")

elif bmi>=30:

    print("obese")