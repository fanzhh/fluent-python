# coding: utf-8
# sorting a list of words by their reversed spelling using lambda.
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=lambda word: word[::-1])
