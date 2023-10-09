from datetime import datetime


def func_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        f = func(*args, **kwargs)
        print(datetime.now() - start)
        return f
    return wrapper

@func_time
def foo():
    return "a+b"

lst = [25, 55, 78, 11, 15, 57, 100, 56, 58, 23, 45, 47, 43, 46, 567, 786, 6, 78, 678, 678, 2, 5]
target = 7

def my_func(lst: list):
    start = datetime.now()
    for i in range(len(lst) - 1):
        res = []
        a = target - lst[i]
        if a in lst:
            j = lst.index(a)
            res = [i, j]
            print(datetime.now() - start)
            break

    return res

def inner_cycle(lst: list):
    start = datetime.now()
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                print(datetime.now() - start)
                return [i, j]

print(my_func(lst))
print(inner_cycle(lst))