import random

secret_number =random.randint(1, 50)
i = 1
print("Компютер загадал число, у вас шесть попыток чтобы отгадать")
while i <= 6:
    a = int(input(str(i) + '-я попытка: '))
    if a > secret_number:
        print('Много')
    elif a < secret_number:
        print('Мало')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 6 попыток. Было загадано', secret_number )
