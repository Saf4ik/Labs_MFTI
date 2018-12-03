import sys

'''
def fac(x):
    if x == 1:
        return 1
    return fac(x-1) * x


print(fac(998))


print(sys.getrecursionlimit())

'''


def fib(x):
    if x == 0:
        return 0
    elif x <= 2:
        return 1
    elif x > 2:
        return fib(x-1) + fib(x-2)


print(fib(7))