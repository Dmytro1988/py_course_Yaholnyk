row_1 =[2,6,9,8,5]
row_2 =[3,5,6,8,3]
row_3 =[]
if len(row_1) > len(row_2):
    print('Ряд один больше:\n', row_1) 
if len(row_1) < len(row_2):   
    print('Ряд два больше:\n', row_2)
if len(row_1) == len(row_2):
        for i in range(len(row_1)):
            row_3.append(row_1[i] + row_2[i])    
        print('Сумма двух рядов:\n', row_3)