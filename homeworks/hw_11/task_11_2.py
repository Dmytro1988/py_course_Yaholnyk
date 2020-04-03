def Sum_Of_the_digits(number): 

    sum = 0

    while(number > 0):
        reminder = number % 10
        sum = sum + reminder
        number = number //10

    return(sum)

print(Sum_Of_the_digits(256), 13)
print(Sum_Of_the_digits(465), 15)
print(Sum_Of_the_digits(241), 7)


#Calculate Sum of digits of a number in a List using Functions 
