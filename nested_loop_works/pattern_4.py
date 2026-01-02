"""

pattern_3.py

1   2   3   4   5 (5)
1   2   3   4 (4)  
1   2   3 (3)  
1   2 (2)     
1(1)        

"""

for r in range(6,1,-1):#[6,5,4,3,2,1]

    for c in range(1,r):#c[1,2,2,4,5]

        print(c,end=" ")
    
    print()


