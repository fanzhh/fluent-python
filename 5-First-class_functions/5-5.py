# coding: utf-8
# list of factorials produced with map and filter compared to alternatives coded as list comprehensions
list(map(fact, range(6)))
[fact(n) for n in range(6)]
list(map(factorial,filter(lambda n: n%2, range(6))))
[factorial(n) for n in range(6) if n % 2]
