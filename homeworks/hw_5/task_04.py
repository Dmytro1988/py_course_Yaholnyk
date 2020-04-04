list = [1,2,3,4,6,7,8]
i = 0
while i < len(list):
    if i+1 ==len(list):
        print("found list \n{}".format(list))
        break
    elif list[i+1] - list[i] != 1:
        print(list[i+1]) 
        break     
    else:
        i+=1 
        