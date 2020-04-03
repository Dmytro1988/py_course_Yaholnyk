family = {
'gradpa': ('Alex', 76),
'grandma': ('Nona', 74),
'dad': ('Greg', 48),
'mom':('July', 45),
'son_older': ('Bob', 18),
'son_middle': ('Alex', 15),
'son_young' : ('Mark', 10)
}
lst_age = []
for values in family.values():
    lst_age.append(values[1])
print(lst_age)
max_val = max(lst_age)
print (max_val)
min_val = min(lst_age)
print (min_val)
print('Difference between oldest and yangest:\n'+ str (max_val - min_val))


