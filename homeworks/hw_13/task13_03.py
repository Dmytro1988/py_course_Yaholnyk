def get_real_floor(n):
    # code here
    if 13 >= n >= 1:
        return n - 1
    elif n >= 14:
        return n - 2
    else:
        return n

print(get_real_floor(1), 0)
print(get_real_floor(5), 4)
print(get_real_floor(15), 13)       