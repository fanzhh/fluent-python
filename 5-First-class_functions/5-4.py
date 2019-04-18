# coding: utf-8
fruits = ['strawberry','fig','apple','cherry','raspberry','banana']
sorted(fruits, key=len)
get_ipython().magic('save 5-3.py 14-15')
def reverse(word):
    return word[::-1]
reverse('testing')
sorted(fruits,key=reverse)
