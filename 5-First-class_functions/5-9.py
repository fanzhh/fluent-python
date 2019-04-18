# coding: utf-8
class C: pass
obj = C()
def func(): pass
sorted(set(dir(func))-set(dir(obj)))
# listing attributes of functions that don't exist in plain instances.
