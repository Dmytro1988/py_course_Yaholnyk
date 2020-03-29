lst = ["sheep", "sheep", "sheep", "wolf", "sheep", "sheep"]
lst.reverse()
print(lst)
the_wolf_position = lst.index("wolf")
if the_wolf_position == 0:
    print('Pls go away and stop eating my sheep')
else:
    print("Oi! Sheep number " + str(the_wolf_position) + "! You are about to be eaten by a wolf!")
         
