



roles = {
  'admin' : ["ivan", "igor"],
  'maintainer' : ["pol", "dasty"],
  'manager' : ["victor","izzy"],
  'developer' : ["franky","kate"],
}

name = input('Enter name:')
flag = False
for key,values in roles.items():
    if name  in values:  
        print(" Hello " +  str(key))
        flag = True
        break
             
if flag == False:
        print("Hello guest")
        
        
   
        
     
    
           