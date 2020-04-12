def hero(bullets, dragons):
    n = int(bullets)/2
    if n > dragons or n == dragons:
        return True
    else:
        return False

print(hero(100, 40), True)
print(hero(1500, 751), False)
print(hero(0, 1), False)      

#A hero is on his way to the castle to complete his mission. However, 
#he's been told that the castle is surrounded with a couple of powerful dragons!
#each dragon takes 2 bullets to be defeated, our hero has no idea how many
#bullets he should carry.. Assuming he's gonna grab a specific given number 
#of bullets and move forward to fight another specific given number of dragons,
#will he survive?

#Return True if yes, False otherwise :)