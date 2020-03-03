from math import *

x = int(input("Enter x:"))
y = ((log10(x))**1/4 + acos(x+3))*1/abs(x+(2*(x)**2))
print(y)
