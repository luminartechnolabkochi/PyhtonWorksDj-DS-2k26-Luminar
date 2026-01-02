

file_path="file_operations\\titanic\\Titanic-Dataset.csv"

fr = open(file_path,"r")

import csv


reader =csv.DictReader(fr)

data = [row for row in reader] #[{},{},{}]

"""
data=[
    {
        'PassengerId': '1', 'Survived': '0', 
        'Pclass': '3', 'Name': 'Braund, Mr. Owen Harris', 
        'Sex': 'male', 'Age': '22', 
        'SibSp': '1', 'Parch': '0',
        'Ticket': 'A/5 21171', 'Fare': '7.25', 
        'Cabin': '', 'Embarked': 'S'
    },

]

[{},{},{},{},{},{},{}]
"""


passengers_count = len(data)

# print("passenger_count=",passengers_count)

survived_unsurvived=[p.get("Survived") for p in data ]

# print("survived count=",survived_unsurvived.count("1"))
# print("unsurvived count=",survived_unsurvived.count("0"))

genders=[p.get("Sex") for p in data ]

# print("malecount",genders.count("male"))
# print("femalecount",genders.count("female"))

all_class=[p.get("Pclass") for p in data ]

class_count = {c:all_class.count(c) for c in all_class}

# print(class_count)

ages=[ int(p.get("Age")) for p in data if p.get("Age").isdigit()]


youngest_age=min(ages)

oldest_ae=max(ages)

you_p=[(p.get("Name"),p.get("Age")) for p in data if p.get("Age").isdigit() and int(p.get("Age"))==youngest_age]

print(you_p)




first_ten=data[:11]

first_ten_names=[p.get("Name") for p in first_ten]

# print(first_ten_names)

boarding_stations=[p.get("Embarked") for p in data if len(p.get("Embarked")) >0]

bc={s:boarding_stations.count(s) for s in boarding_stations}

# print(bc)


childrens= [p for p in data if p.get("Age").isdigit() and int(p.get("Age"))<10]

print(len(childrens))

survived_children=[p for p in childrens if p.get("Survived")=="1"]

print("survived childern",len(survived_children))


survived_passengers=[p for p in data if p.get("Survived")=="1"]

survived_passenger_count=len(survived_passengers)

survival_rate = (survived_passenger_count/len(data))*100

print("survival rate",survival_rate)



unsurvived_passenges=[p for p in data if p.get("Survived")=="0"]

unsurvived_p_count = len(unsurvived_passenges)

unsurvived_rate = (unsurvived_p_count/len(data))*100

print("unsurvival rate",unsurvived_rate)

# (male_survived/total_males)*100 => survived rate of males
# (fmale_survived/total_females)*100 => survived rate of males

male_passengers=[p for p in data if p.get("Sex")=="male"]

male_survived=[p for p in male_passengers if p.get("Survived")=="1"] 

male_survival_rate =( len(male_survived)/len(male_passengers))*100

print(male_survival_rate,"male survival rate")




all_p_classes=[p.get("Pclass") for p in data]

class_count = {c:all_p_classes.count(c) for c in all_p_classes}

print(class_count)

all_p_survuived_class= [p.get("Pclass") for p in data if p.get("Survived")=="1"]

class_survived_count = {c:all_p_survuived_class.count(c) for c in all_p_survuived_class }

print(class_survived_count)
"""
class_count={'3': 491, '1': 216, '2': 184}
class_survived_count={'1': 136, '3': 119, '2': 87}
"""

for k,v in class_count.items():

    # k=class
    # v=p_count

    s_p=class_survived_count.get(k)

    rate=(s_p/v)*100

    print(k,rate)



#