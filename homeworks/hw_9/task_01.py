a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    if i in b:
        c.append(i)
        print(c)



# через функцию       
#c = list(filter(lambda elem: elem in b, a))
#print (c)
