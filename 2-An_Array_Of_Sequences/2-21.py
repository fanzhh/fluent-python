# coding: utf-8
numbers = array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
len(memv)
memv[0]
memv_oct = memv.cast('8')
memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5]=4
numbers
