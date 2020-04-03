def digitize(n):
    result = []
    for i in str(n):
        result.append (int(i))
    result.reverse()

    return (result)
print((digitize(35231)))    
    
 #Convert number to reversed array of digits   