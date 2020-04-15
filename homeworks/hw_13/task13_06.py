def array_madness(a,b):
    # Ready, get, set, GO!!!
    return True if sum(i ** 2 for i in a) > sum(j ** 3 for j in b) else False



print(array_madness([4, 5, 6], [1, 2, 3]),True)
print(array_madness([1, 2, 3],[4, 5, 6]),False)


#Given two integer arrays a, b, both of length >= 1, create a program that 
#returns true if the sum of the squares of each element in a is strictly 
#greater than the sum of the cubes of each element in b
