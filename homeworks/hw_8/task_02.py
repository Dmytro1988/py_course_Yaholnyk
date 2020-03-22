list = [-1,-6,2,-6,5,3,4,-7,8,-9,1,4,6]
j = 0;
S =1
new_list = []
for i in list:
    if int(i)>0:
        j +=1
        if j == 1:
            new_list.append(i)
        if j == 3:
            new_list.append(i)
        if j == 6:
            new_list.append(i)
for f in new_list:
    S *= int(f)
print(S)