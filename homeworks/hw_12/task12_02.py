def index(array, n):
    return array[n]**n if len(array) >= n else -1


print(index([1, 2, 3, 4],2),9)
print(index([1, 3, 10, 100],3),1000000)    
print(index([1, 5, 8, 50],6),-1)

#You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. 
#Don't forget that the first element has the index 0