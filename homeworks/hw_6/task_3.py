lst = [22, -6, 32, 82, 9, 25, 66, 88]
lst_new = []
n = len(lst)
for i in range(1,n):
    if lst[i] % i == 0:
        lst_new.append(lst[i])  
print(lst_new)
  
  
