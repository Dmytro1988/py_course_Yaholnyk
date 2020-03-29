numbers=[1,2,3,6,8,9,4,5]
setnumbers= set(numbers)
if len(numbers) == len(setnumbers):
    print("Все элементы уникальны")
else:
    print("Есть одинаковые")