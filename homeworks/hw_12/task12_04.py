def first_non_consecutive(arr):
    for i, v in enumerate(arr, arr[0]):
        if v != i:
            return v




print(first_non_consecutive([1,2,3,4,5,6,7,8]),None)
print(first_non_consecutive([4,6,7,8,9,11]),6)
print(first_non_consecutive([4,5,6,7,8,9,11]),11)  


#Your task is to find the first element of an array that is not consecutive.

#By not consecutive we mean not exactly 1 larger than the previous 
#element of the array.

#E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are 
#a#ll consecutive but 6 is not, so that's the first non-consecutive number.