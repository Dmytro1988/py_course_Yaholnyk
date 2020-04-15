def no_boring_zeros(n):
    # your code
    while n % 10 == 0 and len(str(n)) > 1:
        n = n / 10
    return n 


print(no_boring_zeros(1450), 145)
print(no_boring_zeros(960000), 96)
print(no_boring_zeros(1050), 105)    


#Numbers ending with zeros are boring.
#They might be fun in your world, but not here.
#Get rid of them. Only the ending ones
