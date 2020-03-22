# a = input('Введите строку:')
# a = a.split()
# a.reverse()
# a2 = ' '
# for i in a:
    #a2 += i + ' '
# print(a2)

a = input('Введите строку:')
a2 = ' '
i = len(a)-1
while i >= 0:
    if a[i] == ' ':
        a2 = a2 + a[i+1:] + ' '
        a = a[:i]
        i = len(a) - 1
    else:
        i -= 1
a2 = a2 + a
print(a2)
