

file_path = "Errorhandling\\years.txt"

fr = open(file_path,"r",encoding="utf-8")

all_years=[]


for line in fr:#line = str

    line = line.rstrip("\n")

    try:
        year =int(line)


        all_years.append(year)

    except Exception as e:

        continue


leap_years=[]

for year in all_years:

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        leap_years.append(year)

print(leap_years)

lc_count={year:leap_years.count(year) for year in leap_years}
print(lc_count)




