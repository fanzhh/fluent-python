# coding: utf-8
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)
factorial(42)
factorial.__doc__
type(factorial)
help(factorial)
