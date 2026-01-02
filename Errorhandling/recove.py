
# list:

    #append

    # insert

    # pop

    # remove

    # sort

    # reverse

    # count

#dict
    #keys()

    #values()

    #items()

    #get(key)

    #pop(key)



text="python programming is simple this python program is very very simple"

words=text.split(" ") #["python","programming","is"]

wc={w:words.count(w) for w in words}

print(wc)

max_val=max(wc.values())

freq=[k for k,v in wc.items() if v==max_val]

print(freq)


"""
Errorhandling

    try
    except
    finally

"""
