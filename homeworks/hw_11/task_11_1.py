def count_sheeps(sheep):
      return (sheep.count(True))
     

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]


print(count_sheeps(array1),"There are 17 sheeps in total, not %s" % count_sheeps(array1))       


#Consider an array/list of sheep where some sheep may be missing 
# from their place. We need a function that counts the number of sheep present in the array 
# (true means present)
