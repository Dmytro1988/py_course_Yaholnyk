
N = [1,3,-5,-2,6]
summa = summa_d = 0
for i in N:
    if i < 0:
        summa += i
        summa_d += 1 
S = summa/summa_d        
print(S)
N_min = min(N)
print(N_min)
if summa_d != 0:
    min_id = N.index(N_min)
    N[min_id] = S
print(N)
     

