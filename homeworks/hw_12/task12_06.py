def move(position, roll):
    # your code here
    new_pos = position + (roll *2)
    return new_pos 


print(move(0, 4), 8)
print(move(3, 6), 15)
print((2, 5), 12) 


#In this game, the hero moves from left to right. The player rolls the dice and 
#moves the number of spaces indicated by the dice two times.
#Create a function for the terminal game that takes the current position of the 
#hero and the roll (1-6) and return the new position.