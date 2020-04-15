def sum_array(arr):
    if arr != None and len(arr) > 2:
        return sum(sorted(arr)[1:-1])
    else:
        return 0

        
print(sum_array([6, 0, 1, 10, 10]), 17)
print(sum_array([-6, -20, -1, -10, -12]), -28)
print(sum_array([-6, 20, -1, 10, -12]),3)

#Sum all the numbers of the array (in F# and Haskell you get a list) 
#except the highest and the lowest element (the value, not the index!).
#(The highest/lowest element is respectively only one element at each edge, 
#even if there are more than one with the same value!)