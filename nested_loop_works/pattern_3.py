"""
pattern_2.py

*   *   *   *   *(5)
*   *   *   *(4)
*   *   *(3)
*   *(2)
*(1)

"""


for r in range(1,6):#r=[1,2,3,4,5]

    for c in range(6,r,-1):

        print("*",end="\t")

    print()