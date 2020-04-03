



roles = {
  'admin' : ["ivan", "igor"],
  'maintainer' : ["pol", "dasty"],
  'manager' : ["victor","izzy"],
  'developer' : ["franky","kate"],
}

name = input('Enter name:')
for key,values in roles.items():
    if name  in values:  
        print(" Hello " +  str(key))
        break      
if name not in values:
  print("Hello guest")
      
        
   
        
     
    
           