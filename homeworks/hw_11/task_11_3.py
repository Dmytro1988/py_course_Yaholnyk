def bin_to_decimal(inp):
      
    num = 0
    for i in range(0, len(inp)):  
       num = num + int(inp[i])*(2**(len(inp)-i-1))
      
    return num



print (bin_to_decimal([1,0]))
print (bin_to_decimal([1,1]))
print (bin_to_decimal([1,0,1,0,1,0]))
print (bin_to_decimal([1,0,0,1,0,0,1]))


#Complete the function which converts a binary number (given as a string) to a decimal number