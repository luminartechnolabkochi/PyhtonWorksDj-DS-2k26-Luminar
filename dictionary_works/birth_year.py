

years=[2004,2001,2003,2003,2002,2004,2007,2001,2004,2004,2003,2001,2004,2001,2003,2003,2002,2004,2007,2001,2004,2004,2003,2001]

yc={}

for y in years:

    if y in yc:

        yc[y]+=1#update
    else:
        yc[y]=1#add

print(yc)


text="helloworld"

# char count

# {h:1,e:1}
