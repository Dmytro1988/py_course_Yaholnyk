my_str = input('Введите имя и фамилию:')
new_my_str = my_str.split()
if my_str.count(' ')+1>=2 and new_my_str[0][1].isalpha():
    print(new_my_str[0][0:1:] + "." + new_my_str[1][0:1:] + ".")   
  
        