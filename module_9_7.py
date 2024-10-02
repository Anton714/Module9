def is_prime(func):
    def wrapper(*args):
        orig_res = func(*args)
        if orig_res > 1:
            k = 0
            for i in range(2, orig_res // 2 + 1):
                if (orig_res % i == 0):
                    k = k + 1
            if (k <= 0):
                return (f'{orig_res} \nПростое')
            else:
                return (f'{orig_res} \nСоставное')
        else:
            return (f'{orig_res} \nНе простое и не составное')

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
