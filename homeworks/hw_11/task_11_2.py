def count_sheep(n):
    result = ''
    number = 1
    for i in range(0, n):
        result = result + str(number) + ' sheep...'
        number += 1
    return result



print(count_sheep(1), "1 sheep...");
print(count_sheep(2), "1 sheep...2 sheep...")
print(count_sheep(3), "1 sheep...2 sheep...3 sheep...")




#If you can't sleep, just count sheep!!
#Task:
#Given a non-negative integer, 3 for example, return a string with
#a murmur: "1 sheep...2 sheep...3 sheep...". 
#Input will always be valid, i.e. no negative integers.








#def Sum_Of_the_digits(number): 

    #sum = 0

   #while(number > 0):
        #reminder = number % 10
        #sum = sum + reminder
        #number = number //10

   #return(sum)print(Sum_Of_the_digits(256), 13print(Sum_Of_the_digits(465), 15print(Sum_Of_the_digits(241), 7)


#Calculate Sum of digits of a number in a List using Functions 
