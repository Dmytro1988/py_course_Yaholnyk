def maps(a):
    if len(a) > 0:
        for i in range(len(a)):
            a[i] = a[i] * 2
    return a

print(maps([1, 2, 3]), [2, 4, 6])
print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])   



#Given an array of integers, return a new array with each value doubled.
#For example:
#[1, 2, 3] --> [2, 4, 6]