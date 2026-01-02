


set_a={100,200,300,400,10,20}

set_b={10,20,100,200,500,600,700}

#(set_a - set_b) U  (set_b- set_a)


symm= set_a.symmetric_difference(set_b)

print(symm)


