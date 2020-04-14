def find_longest(s):
    longest=[]
    for i in s.split(" "):
        longest.append(len(i))
    return max(longest)


print(find_longest("The quick white fox jumped around the massive dog"), 7)
print(find_longest("Take me to tinseltown with you"), 10)
print(find_longest("Sausage chops"), 7)    