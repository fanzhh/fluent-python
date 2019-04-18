# coding: utf-8
# sum of inters up to 99 performed with reduce and sum.
from functools import reduce
from operator import add
reduce(add, range(100))
sum(range(100))
