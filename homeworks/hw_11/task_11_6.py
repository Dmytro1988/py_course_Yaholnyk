def sum_str(a, b):
    return str(sum(int(n) for n in (a, b) if n != ''))


print(sum_str("4","5"))
print(sum_str("34","5"))


#Create a function that takes 2 positive integers in form of a string as 
# an input, and outputs the sum (also as a string)