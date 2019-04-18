# coding: utf-8
fp = open('cafe.txt','w',encoding='utf_8')
fp
fp.write('café')
fp.close()
fp
import os
os.stat('cafe.txt').st_size
fp2 = open('cafe.txt')
fp2
# encoding will be cp1252 on windows?
fp2.encoding
fp2.read()
fp3 = open('cafe.txt', encoding='utf_8')
fp3
fp3.read()
fp4 = open('cafe.txt', 'rb')
fp4
fp4.read()
