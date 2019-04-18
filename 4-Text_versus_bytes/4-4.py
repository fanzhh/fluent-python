# coding: utf-8
import struct
fmt = '<3s3sHH'
with open('tic.gif', 'rb') as fp:
    img = memoryview(fp.read())
    
header = img[:10]
header
bytes(header)
struct.unpack(fmt,header)
del header
del img
