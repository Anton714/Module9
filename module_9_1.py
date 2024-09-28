def apply_all_func(int_list, *functions):
    resalt = {}
    for func in functions:
        resalt [func.__name__] = func(int_list)
    return resalt


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))